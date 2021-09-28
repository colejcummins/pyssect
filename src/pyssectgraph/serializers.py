from node import PyssectNode, ControlEvent, Location
from graph import PyssectGraph
from typing import Set, Dict
import ast
import json


def pyssect_loads(str: str):
  """Takes in a JSON string and returns a corresponding Control Flow Graph, Node, or Location"""

  def _object_hook(obj):
    # TODO implement strict rules for json conversion, with errors
    if 'name' in obj and 'cur' in obj and 'root' in obj:
      return PyssectGraph(**obj)
    if 'line' in obj and 'column' in obj:
      return Location(obj['line'], obj['column'])
    if 'parents' in obj and 'children' in obj:
      return PyssectNode(**obj)
    return obj

  return json.loads(str, object_hook=_object_hook)


def _ast_no_recurse(node: ast.AST) -> ast.AST:
  """Turns an AST node with nested nodes into a flattened node for string representation."""
  l = ast.Expr(value=ast.Ellipsis())
  if hasattr(node, 'body') and not isinstance(node, ast.ExceptHandler):
    node.__setattr__('body', [l])
  if hasattr(node, 'orelse'):
    node.__setattr__('orelse', [l] if node.orelse else [])
  if hasattr(node, 'finalbody'):
    node.__setattr__('finalbody', [l] if node.finalbody else [])
  return node


def _try_no_recurse(node: ast.Try) -> ast.AST:
  l = ast.Expr(value=ast.Ellipsis())
  return ast.Try(
    [l],
    [ast.ExceptHandler(name=handler.name, type=handler.type, body=[l]) for handler in node.handlers],
    [l] if node.orelse else [],
    [l] if node.finalbody else []
  )



def pyssect_dumps(obj, indent: int=2, simple: bool = False) -> str:
  """Returns a json string representation of the Control Flow Graph. Unparsing Control Flow Graphs only works in
  python 3.9.
  """

  def _default(obj):
    if type(obj) in [PyssectNode, PyssectGraph, Location]:
      if simple and isinstance(obj, PyssectNode):
        return {
          'contents': obj.contents,
          'children': obj.children,
          'parents': obj.parents
        }
      return obj.__dict__
    if isinstance(obj, Set):
      return list(obj)
    if isinstance(obj, ControlEvent):
      return obj.value
    if isinstance(obj, ast.AST):
      if isinstance(obj, ast.Try):
        return ast.unparse(_try_no_recurse(obj))
      return ast.unparse(_ast_no_recurse(obj))
    return json.JSONEncoder.default(obj)

  return json.dumps(obj, default=_default, indent=indent)