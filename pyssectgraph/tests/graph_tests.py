from graph import PyssectGraph
from node import PyssectNode, ControlEvent
from serializers import pyssect_dumps
from uuid import uuid4
import unittest

JSON_CFG_OUT = """{
  "name": "test",
  "root": "a",
  "cur": "a",
  "nodes": {
    "a": {
      "name": "a",
      "start": {
        "line": 1,
        "column": 0
      },
      "end": {
        "line": 1,
        "column": 0
      },
      "parents": {},
      "children": {
        "b": ""
      },
      "contents": []
    },
    "b": {
      "name": "b",
      "start": {
        "line": 1,
        "column": 0
      },
      "end": {
        "line": 1,
        "column": 0
      },
      "parents": {
        "a": ""
      },
      "children": {},
      "contents": []
    }
  }
}"""

class GraphTests(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(GraphTests, self).__init__(*args, **kwargs)
    self.maxDiff = None

  def test_attach_child(self):
    node_a = PyssectNode(name='a')
    cfg = PyssectGraph(name='__main__', root='a', cur='a', nodes={'a': node_a})
    node_b = PyssectNode(name='b')
    cfg.attach_child(node_b, ControlEvent.ONTRUE)

    self.assertEqual(len(cfg.nodes), 2)
    self.assertEqual(PyssectGraph(name='__main__', root='a', cur='a', nodes={
      'a': PyssectNode(name='a', children={'b': ControlEvent.ONTRUE}),
      'b': PyssectNode(name='b', parents={'a': ControlEvent.ONTRUE})
    }), cfg)

  def test_insert_child(self):
    node_a = PyssectNode('a')
    node_b = PyssectNode('b')
    node_c = PyssectNode('c')
    node_d = PyssectNode('d')
    cfg = PyssectGraph('__main__', 'a', 'a', {'a': node_a})

    cfg.attach_child(node_c, ControlEvent.ONTRUE)
    cfg.attach_child(node_d, ControlEvent.ONTRUE)
    cfg.insert_child(node_b, ControlEvent.ONTRUE)

    self.assertEqual(len(cfg.nodes), 4)
    self.assertEqual(PyssectGraph('__main__', 'a', 'a', {
      'a': PyssectNode(name='a', children={'b': ControlEvent.ONTRUE}),
      'b': PyssectNode(name='b', parents={'a': ControlEvent.ONTRUE}, children={'c': ControlEvent.ONTRUE, 'd': ControlEvent.ONTRUE}),
      'c': PyssectNode(name='c', parents={'b': ControlEvent.ONTRUE}),
      'd': PyssectNode(name='d', parents={'b': ControlEvent.ONTRUE})
    }), cfg)

  def test_merge_nodes(self):
    node_a = PyssectNode('a', contents=["hello"])
    node_b = PyssectNode('b', contents=['world'])
    node_c = PyssectNode('c')
    node_d = PyssectNode('d')
    cfg = PyssectGraph('__main__')

    cfg.attach_child(node_a)
    cfg.attach_child(node_b, ControlEvent.ONTRUE)
    cfg.go_to('b')
    cfg.attach_child(node_c, ControlEvent.ONTRUE)
    cfg.attach_child(node_d, ControlEvent.ONFALSE)

    cfg.merge_nodes(node_a, node_b)

    self.assertEqual(len(cfg.nodes), 3)
    self.assertEqual(PyssectGraph('__main__', 'a', 'b', {
      'a': PyssectNode('a', children={'c': ControlEvent.ONTRUE, 'd': ControlEvent.ONFALSE}, contents=['hello', 'world']),
      'c': PyssectNode('c', parents={'a': ControlEvent.ONTRUE}),
      'd': PyssectNode('d', parents={'a': ControlEvent.ONFALSE})
    }), cfg)

  def test_rename_node(self):
    node_a = PyssectNode('a')
    node_b = PyssectNode('b')
    node_c = PyssectNode('c')
    cfg = PyssectGraph('__main__')

    cfg.attach_child(node_a)
    cfg.attach_child(node_b, ControlEvent.ONTRUE)
    cfg.go_to('b')
    cfg.attach_child(node_c, ControlEvent.ONTRUE)

    cfg.rename_node(node_b, 'new')

    self.assertEqual(PyssectGraph('__main__', 'a', 'new', {
      'a': PyssectNode('a', children={'new': ControlEvent.ONTRUE}),
      'new': PyssectNode('new', parents={'a': ControlEvent.ONTRUE}, children={'c': ControlEvent.ONTRUE}),
      'c': PyssectNode('c', parents={'new': ControlEvent.ONTRUE})
    }), cfg)

  def test_to_json_str(self):
    cfg = PyssectGraph('test', 'a', 'a', {
        'a': PyssectNode(name='a', children={'b': ControlEvent.PASS}),
        'b': PyssectNode(name='b', parents={'a': ControlEvent.PASS})
      })

    self.assertEqual(len(cfg.nodes), 2)
    self.assertEqual(JSON_CFG_OUT, pyssect_dumps(cfg))

if __name__ == '__main__':
  unittest.main()