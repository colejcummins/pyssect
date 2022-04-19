from pyssectgraph import PyssectNode, PyssectGraph, pyssect_dumps
import unittest


JSON_CFG_OUT = """{
  "name": "test",
  "root": "a",
  "cur": "a",
  "nodes": {
    "a": {
      "name": "a",
      "start": {
        "line": 0,
        "column": 0
      },
      "end": {
        "line": 0,
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
        "line": 0,
        "column": 0
      },
      "end": {
        "line": 0,
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

class CFGTest(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(CFGTest, self).__init__(*args, **kwargs)
    self.maxDiff = None

  def test_attach_child(self):
    node_a = PyssectNode(name='a')
    cfg = PyssectGraph(root='a', cur='a', nodes={'a': node_a})
    node_b = PyssectNode(name='b')
    cfg.attach_child(node_b)

    self.assertEqual(len(cfg.nodes), 2)
    self.assertEqual(PyssectGraph(root='a', cur='a', nodes={
      'a': PyssectNode(name='a', children={'b': ''}),
      'b': PyssectNode(name='b', parents={'a': ''})
    }), cfg)


  def test_insert_child(self):
    node_a = PyssectNode(name='a')
    node_b = PyssectNode(name='b')
    node_c = PyssectNode(name='c')
    node_d = PyssectNode(name='d')
    cfg = PyssectGraph('a', 'a', {'a': node_a})

    cfg.attach_child(node_c)
    cfg.attach_child(node_d)
    cfg.insert_child(node_b)

    self.assertEqual(len(cfg.nodes), 4)
    self.assertEqual(PyssectGraph('a', 'a', {
      'a': PyssectNode(name='a', children={'b': ''}),
      'b': PyssectNode(name='b', parents={'a': ''}, children={'c': '', 'd': ''}),
      'c': PyssectNode(name='c', parents={'b': ''}),
      'd': PyssectNode(name='d', parents={'b': ''})
    }), cfg)


  def test_merge_nodes(self):
    cfg = PyssectGraph('a', 'a', {
      'a': PyssectNode(name='a', children={'b': ''}, contents=['hello']),
      'b': PyssectNode(name='b', parents={'a': ''}, children={'c': '', 'd': ''}, contents=['world']),
      'c': PyssectNode(name='c', parents={'b': ''}),
      'd': PyssectNode(name='d', parents={'b': ''})
    })

    cfg.merge_nodes('a', 'b')

    self.assertEqual(len(cfg.nodes), 3)
    self.assertEqual(PyssectGraph('a', 'a', {
      'a': PyssectNode(name='a', children={'c': '', 'd': ''}, contents=['hello', 'world']),
      'c': PyssectNode(name='c', parents={'a': ''}),
      'd': PyssectNode(name='d', parents={'a': ''})
    }), cfg)


  def test_to_json_str(self):
    cfg = PyssectGraph('test', 'a', 'a', {
        'a': PyssectNode(name='a', children={'b': ''}),
        'b': PyssectNode(name='b', parents={'a': ''})
      })

    self.assertEqual(len(cfg.nodes), 2)
    self.assertEqual(JSON_CFG_OUT, pyssect_dumps(cfg))


if __name__ == '__main__':
  unittest.main()