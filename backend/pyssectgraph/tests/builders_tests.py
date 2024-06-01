from builders import builds
from serializers import pyssect_dumps
from typing import Dict, Any
import json
import unittest

class BuildersTests(unittest.TestCase):
  def __init__(self, *args, **kwargs):
    super(BuildersTests, self).__init__(*args, **kwargs)
    self.maxDiff = None

  def test_small(self):
    self.assertEqual(SMALL_JSON, self._prog_to_json(SMALL)['__main__']['nodes'])

  def test_basic_if(self):
    self.assertEqual(BASIC_IF_JSON, self._prog_to_json(BASIC_IF)['__main__']['nodes'])

  def test_basic_return(self):
    self.assertEqual(BASIC_RETURN_JSON, self._prog_to_json(BASIC_RETURN)['__main__']['nodes'])

  def test_if_and_return(self):
    self.assertEqual(IF_AND_RETURN_JSON, self._prog_to_json(IF_AND_RETURN)['__main__']['nodes'])

  def test_basic_while(self):
    self.assertEqual(BASIC_WHILE_JSON, self._prog_to_json(BASIC_WHILE)['__main__']['nodes'])

  def test_while_break_continue(self):
    self.assertEqual(WHILE_BREAK_CONTINUE_JSON, self._prog_to_json(WHILE_BREAK_CONTINUE)['__main__']['nodes'])

  def test_basic_try(self):
    self.assertEqual({}, self._prog_to_json(BASIC_TRY)['__main__']['nodes'])

  def test_function_and_class_collisions(self):
    self.assertEqual(FUNCTION_AND_CLASS_COLLISIONS_JSON, self._prog_to_json(FUNCTION_AND_CLASS_COLLISIONS))

  def _prog_to_json(self, prog: str) -> Dict[str, Any]:
    # print(pyssect_dumps(builds(prog, True)))
    return json.loads(pyssect_dumps(builds(prog, True)))

SMALL = "x = 1"
SMALL_JSON = {
  "root": {
    "name": "root",
    "children": {},
    "start": {
      "line": 1,
      "column": 0,
    },
    "end": {
      "line": 1,
      "column": 5,
    },
    "contents": [
      "x = 1"
    ],
    "parents": {}
  }
}

BASIC_IF = """x = 1
if x < 4:
  x += 2
x -= 1
"""
BASIC_IF_JSON = {
  "root": {
    "name": "root",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 1,
      "column": 5,
    },
    "contents": [
      "x = 1"
    ],
    "children": {
      "If_3_0": ""
    },
    "parents": {}
  },
  "If_2_0": {
    "name": "If_2_0",
    "start": {
      "line": 2,
      "column": 0
    },
    "end": {
      "line": 3,
      "column": 8,
    },
    "contents": [
      "if x < 4:\n    ..."
    ],
    "children": {
      "AugAssign_3_2": "True",
      "exit_If_2_0": ""
    },
    "parents": {
      "root": ""
    }
  },
  "AugAssign_3_2": {
    "name": "AugAssign_3_2",
    "start": {
      "line": 3,
      "column": 2,
    },
    "end": {
      "line": 3,
      "column": 8,
    },
    "contents": [
      "x += 2"
    ],
    "children": {
      "exit_If_2_0": ""
    },
    "parents": {
      "If_2_0": "True"
    }
  },
  "exit_If_2_0": {
    "name": "exit_If_2_0",
    "start": {
      "line": 4,
      "column": 0,
    },
    "contents": [
      "x -= 1"
    ],
    "children": {},
    "parents": {
      "AugAssign_3_2": "",
      "If_2_0": ""
    }
  }
}

BASIC_RETURN = """x = 0
return x
x += 1
"""
BASIC_RETURN_JSON = {
  "root": {
    "contents": [
      "x = 0"
    ],
    "children": {
      "Return_3_0": ""
    },
    "parents": {}
  },
  "Return_3_0": {
    "contents": [
      "return x"
    ],
    "children": {},
    "parents": {
      "root": ""
    }
  }
}

IF_AND_RETURN = """
if x > 3:
  if x < 2:
    return 0
  return 1
return 2
"""
IF_AND_RETURN_JSON = {
  "root": {
    "contents": [],
    "children": {
      "If_2_0": ""
    },
    "parents": {}
  },
  "If_2_0": {
    "contents": [
      "if x > 3:\n    ..."
    ],
    "children": {
      "If_3_2": "True",
      "exit_If_2_0": ""
    },
    "parents": {
      "root": ""
    }
  },
  "If_3_2": {
    "contents": [
      "if x < 2:\n    ..."
    ],
    "children": {
      "Return_4_4": "",
      "exit_If_3_2": ""
    },
    "parents": {
      "If_2_0": "True"
    }
  },
  "Return_4_4": {
    "contents": [
      "return 0"
    ],
    "children": {},
    "parents": {
      "If_3_2": ""
    }
  },
  "exit_If_3_2": {
    "contents": [],
    "children": {
      "Return_5_2": ""
    },
    "parents": {
      "If_3_2": ""
    }
  },
  "Return_5_2": {
    "contents": [
      "return 1"
    ],
    "children": {},
    "parents": {
      "exit_If_3_2": ""
    }
  },
  "exit_If_2_0": {
    "contents": [],
    "children": {
      "Return_6_0": ""
    },
    "parents": {
      "If_2_0": ""
    }
  },
  "Return_6_0": {
    "contents": [
      "return 2"
    ],
    "children": {},
    "parents": {
      "exit_If_2_0": ""
    }
  }
}

BASIC_WHILE="""
x = 1
while x < 5:
  x += 1
x = 2
"""
BASIC_WHILE_JSON = {
  "root": {
    "contents": [
      "x = 1"
    ],
    "children": {
      "While_3_0": ""
    },
    "parents": {}
  },
  "While_3_0": {
    "contents": [
      "while x < 5:\n    ..."
    ],
    "children": {
      "AugAssign_4_2": "True",
      "exit_While_3_0": ""
    },
    "parents": {
      "root": "",
      "AugAssign_4_2": ""
    }
  },
  "AugAssign_4_2": {
    "contents": [
      "x += 1"
    ],
    "children": {
      "While_3_0": ""
    },
    "parents": {
      "While_3_0": "True"
    }
  },
  "exit_While_3_0": {
    "contents": [
      "x = 2"
    ],
    "children": {},
    "parents": {
      "While_3_0": ""
    }
  }
}

WHILE_BREAK_CONTINUE ="""
while x < 10:
  if x == 5:
    continue
  if x == 1:
    x += 2
    break
  x += 1
x += 2
"""
WHILE_BREAK_CONTINUE_JSON = {
  "root": {
    "contents": [],
    "children": {
      "While_2_0": ""
    },
    "parents": {}
  },
  "While_2_0": {
    "contents": [
      "while x < 10:\n    ..."
    ],
    "children": {
      "If_3_2": "True",
      "exit_While_2_0": ""
    },
    "parents": {
      "root": "",
      "Continue_4_4": "continue",
      "exit_If_5_2": ""
    }
  },
  "If_3_2": {
    "contents": [
      "if x == 5:\n    ..."
    ],
    "children": {
      "Continue_4_4": "",
      "exit_If_3_2": ""
    },
    "parents": {
      "While_2_0": ""
    }
  },
  "Continue_4_4": {
    "contents": [
      "continue"
    ],
    "children": {
      "While_2_0": "continue"
    },
    "parents": {
      "If_3_2": ""
    }
  },
  "exit_If_3_2": {
    "contents": [],
    "children": {
      "If_5_2": ""
    },
    "parents": {
      "If_3_2": ""
    }
  },
  "If_5_2": {
    "contents": [
      "if x == 1:\n    ..."
    ],
    "children": {
      "AugAssign_6_4": "True",
      "exit_If_5_2": ""
    },
    "parents": {
      "exit_If_3_2": ""
    }
  },
  "AugAssign_6_4": {
    "contents": [
      "x += 2"
    ],
    "children": {
      "Break_7_4": ""
    },
    "parents": {
      "If_5_2": "True"
    }
  },
  "Break_7_4": {
    "contents": [
      "break"
    ],
    "children": {
      "exit_While_2_0": "break"
    },
    "parents": {
      "AugAssign_6_4": ""
    }
  },
  "exit_While_2_0": {
    "contents": [
      "x += 2"
    ],
    "children": {},
    "parents": {
      "Break_7_4": "break",
      "While_2_0": ""
    }
  },
  "exit_If_5_2": {
    "contents": [
      "x += 1"
    ],
    "children": {
      "While_2_0": ""
    },
    "parents": {
      "If_5_2": ""
    }
  }
}

BASIC_TRY = """try:
  x += 1
except ArithmeticError as e:
  print(x)
"""

TRY_WITH_FINALLY_ELSE = """
try:
  x += 1
except ArithmeticError:
  print("arithmetic")
except Exception:
  print("exception")
else:
  print("else")
finally:
  print("finally")
"""

FUNCTION_AND_CLASS_COLLISIONS = """class Foo():
  def nice(self):
    print(1)

def bar():
  def baz():
    def nice():
      print(2)

def foo_bar():
  def nice():
    print(3)
"""
FUNCTION_AND_CLASS_COLLISIONS_JSON = {
  "__main__": {
    "name": "__main__",
    "root": "FunctionDef_2_2",
    "cur": "FunctionDef_10_0",
    "nodes": {
      "FunctionDef_2_2": {
        "name": "FunctionDef_2_2",
        "start": {
          "line": 2,
          "column": 2
        },
        "end": {
          "line": 3,
          "column": 12
        },
        "parents": {},
        "children": {
          "FunctionDef_5_0": ""
        },
        "contents": [
          "def nice(self):\n    \"\"\"...\"\"\""
        ]
      },
      "FunctionDef_5_0": {
        "name": "FunctionDef_5_0",
        "start": {
          "line": 5,
          "column": 0
        },
        "end": {
          "line": 8,
          "column": 14
        },
        "parents": {
          "FunctionDef_2_2": ""
        },
        "children": {
          "FunctionDef_10_0": ""
        },
        "contents": [
          "def bar():\n    \"\"\"...\"\"\""
        ]
      },
      "FunctionDef_10_0": {
        "name": "FunctionDef_10_0",
        "start": {
          "line": 10,
          "column": 0
        },
        "end": {
          "line": 12,
          "column": 12
        },
        "parents": {
          "FunctionDef_5_0": ""
        },
        "children": {},
        "contents": [
          "def foo_bar():\n    \"\"\"...\"\"\""
        ]
      }
    }
  },
  "Foo_nice": {
    "name": "Foo_nice",
    "root": "Expr_3_4",
    "cur": "Expr_3_4",
    "nodes": {
      "Expr_3_4": {
        "name": "Expr_3_4",
        "start": {
          "line": 3,
          "column": 4
        },
        "end": {
          "line": 3,
          "column": 12
        },
        "parents": {},
        "children": {},
        "contents": [
          "print(1)"
        ]
      }
    }
  },
  "bar": {
    "name": "bar",
    "root": "FunctionDef_6_2",
    "cur": "FunctionDef_6_2",
    "nodes": {
      "FunctionDef_6_2": {
        "name": "FunctionDef_6_2",
        "start": {
          "line": 6,
          "column": 2
        },
        "end": {
          "line": 8,
          "column": 14
        },
        "parents": {},
        "children": {},
        "contents": [
          "def baz():\n    \"\"\"...\"\"\""
        ]
      }
    }
  },
  "bar_baz": {
    "name": "bar_baz",
    "root": "FunctionDef_7_4",
    "cur": "FunctionDef_7_4",
    "nodes": {
      "FunctionDef_7_4": {
        "name": "FunctionDef_7_4",
        "start": {
          "line": 7,
          "column": 4
        },
        "end": {
          "line": 8,
          "column": 14
        },
        "parents": {},
        "children": {},
        "contents": [
          "def nice():\n    \"\"\"...\"\"\""
        ]
      }
    }
  },
  "bar_baz_nice": {
    "name": "bar_baz_nice",
    "root": "Expr_8_6",
    "cur": "Expr_8_6",
    "nodes": {
      "Expr_8_6": {
        "name": "Expr_8_6",
        "start": {
          "line": 8,
          "column": 6
        },
        "end": {
          "line": 8,
          "column": 14
        },
        "parents": {},
        "children": {},
        "contents": [
          "print(2)"
        ]
      }
    }
  },
  "foo_bar": {
    "name": "foo_bar",
    "root": "FunctionDef_11_2",
    "cur": "FunctionDef_11_2",
    "nodes": {
      "FunctionDef_11_2": {
        "name": "FunctionDef_11_2",
        "start": {
          "line": 11,
          "column": 2
        },
        "end": {
          "line": 12,
          "column": 12
        },
        "parents": {},
        "children": {},
        "contents": [
          "def nice():\n    \"\"\"...\"\"\""
        ]
      }
    }
  },
  "foo_bar_nice": {
    "name": "foo_bar_nice",
    "root": "Expr_12_4",
    "cur": "Expr_12_4",
    "nodes": {
      "Expr_12_4": {
        "name": "Expr_12_4",
        "start": {
          "line": 12,
          "column": 4
        },
        "end": {
          "line": 12,
          "column": 12
        },
        "parents": {},
        "children": {},
        "contents": [
          "print(3)"
        ]
      }
    }
  }
}

if __name__ == '__main__':
  unittest.main()
