from node import PyssectNode, ControlEvent, Location
from graph import PyssectGraph
from typing import Set, List
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

def _flatten_ast_node(node: ast.AST) -> ast.AST:
  """Turns an AST node with nested nodes into a flattened node for string representation."""
  l = ast.Expr(value=ast.Ellipsis())

  if isinstance(node, ast.Try):
    flat_handlers = [ast.ExceptHandler(name=handler.name, type=handler.type, body=[l]) for handler in node.handlers]
    return ast.Try([l], flat_handlers, [l] if node.orelse else [], [l] if node.finalbody else [])

  if hasattr(node, 'body') and not isinstance(node, ast.ExceptHandler):
    node.__setattr__('body', [l])
  if hasattr(node, 'orelse'):
    node.__setattr__('orelse', [l])
  if hasattr(node, 'finalbody'):
    node.__setattr__('finalbody', [l])
  return node

def pyssect_dumps(obj, indent:int=2, pyssect_node_keys: List[str]=[]) -> str:
  """Returns a json string representation of the Control Flow Graph. ast.unparse only works in python 3.9 and above.

  If `pyssect_node_keys` is set to anything but an empty array, `pyssect_dumps` will include only the keys specified
  when serializing a `PyssectNode`
  """

  def _default(obj):
    if type(obj) in [PyssectNode, PyssectGraph, Location]:
      if isinstance(obj, PyssectNode) and pyssect_node_keys:
        return {key: obj[key] for key in pyssect_node_keys}
      return obj.__dict__
    if isinstance(obj, Set):
      return list(obj)
    if isinstance(obj, ControlEvent):
      return obj.value
    if isinstance(obj, ast.AST):
      return ast.unparse(_flatten_ast_node(obj)).split('\n')
    return json.JSONEncoder.default(obj)

  return json.dumps(obj, default=_default, indent=indent)