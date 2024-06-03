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
    self.assertEqual(BASIC_TRY_JSON, self._prog_to_json(BASIC_TRY, False)['__main__']['nodes'])

  def test_try_with_finally_else(self):
    self.assertEqual(TRY_WITH_FINALLY_ELSE_JSON, self._prog_to_json(TRY_WITH_FINALLY_ELSE, False)['__main__']['nodes'])

  def test_function_and_class_collisions(self):
    self.assertEqual(FUNCTION_AND_CLASS_COLLISIONS_JSON, self._prog_to_json(FUNCTION_AND_CLASS_COLLISIONS))

  def _prog_to_json(self, prog: str, clean:bool = True) -> Dict[str, Any]:
    return json.loads(pyssect_dumps(builds(prog, clean)))

SMALL = "x = 1"
SMALL_JSON = {
  "Assign_1_0": {
    "name": "Assign_1_0",
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
  "Assign_1_0": {
    "name": "Assign_1_0",
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
      "If_2_0": ""
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
      "Assign_1_0": ""
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
      "line": 3,
      "column": 8,
    },
    "end": {
      "line": 4,
      "column": 6
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
  "Assign_1_0": {
    "name": "Assign_1_0",
    "start": {
      "line": 1,
      "column": 0,
    },
    "end": {
      "line": 1,
      "column": 5
    },
    "contents": [
      "x = 0"
    ],
    "children": {
      "Return_2_0": ""
    },
    "parents": {}
  },
  "Return_2_0": {
    "name": "Return_2_0",
    "start": {
      "line": 2,
      "column": 0,
    },
    "end": {
      "line": 2,
      "column": 8
    },
    "contents": [
      "return x"
    ],
    "children": {},
    "parents": {
      "Assign_1_0": ""
    }
  }
}

IF_AND_RETURN = """if x > 3:
  if x < 2:
    return 0
  return 1
return 2
"""
IF_AND_RETURN_JSON = {
  "If_1_0": {
    "name": "If_1_0",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 4,
      "column": 10
    },
    "parents": {},
    "children": {
      "If_2_2": "True",
      "Return_5_0": ""
    },
    "contents": [
      "if x > 3:\n    ..."
    ]
  },
  "If_2_2": {
    "name": "If_2_2",
    "start": {
      "line": 2,
      "column": 2
    },
    "end": {
      "line": 3,
      "column": 12
    },
    "parents": {
      "If_1_0": "True"
    },
    "children": {
      "Return_3_4": "True",
      "Return_4_2": ""
    },
    "contents": [
      "if x < 2:\n    ..."
    ]
  },
  "Return_3_4": {
    "name": "Return_3_4",
    "start": {
      "line": 3,
      "column": 4
    },
    "end": {
      "line": 3,
      "column": 12
    },
    "parents": {
      "If_2_2": "True"
    },
    "children": {},
    "contents": [
      "return 0"
    ]
  },
  "Return_4_2": {
    "name": "Return_4_2",
    "start": {
      "line": 4,
      "column": 2
    },
    "end": {
      "line": 4,
      "column": 10
    },
    "parents": {
      "If_2_2": ""
    },
    "children": {},
    "contents": [
      "return 1"
    ]
  },
  "Return_5_0": {
    "name": "Return_5_0",
    "start": {
      "line": 5,
      "column": 0
    },
    "end": {
      "line": 5,
      "column": 8
    },
    "parents": {
      "If_1_0": ""
    },
    "children": {},
    "contents": [
      "return 2"
    ]
  }
}

BASIC_WHILE="""x = 1
while x < 5:
  x += 1
x = 2
"""
BASIC_WHILE_JSON = {
  "Assign_1_0": {
    "name": "Assign_1_0",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 1,
      "column": 5
    },
    "parents": {},
    "children": {
      "While_2_0": ""
    },
    "contents": [
      "x = 1"
    ]
  },
  "While_2_0": {
    "name": "While_2_0",
    "start": {
      "line": 2,
      "column": 0
    },
    "end": {
      "line": 3,
      "column": 8
    },
    "parents": {
      "Assign_1_0": "",
      "AugAssign_3_2": ""
    },
    "children": {
      "AugAssign_3_2": "True",
      "exit_While_2_0": ""
    },
    "contents": [
      "while x < 5:\n    ..."
    ]
  },
  "AugAssign_3_2": {
    "name": "AugAssign_3_2",
    "start": {
      "line": 3,
      "column": 2
    },
    "end": {
      "line": 3,
      "column": 8
    },
    "parents": {
      "While_2_0": "True"
    },
    "children": {
      "While_2_0": ""
    },
    "contents": [
      "x += 1"
    ]
  },
  "exit_While_2_0": {
    "name": "exit_While_2_0",
    "start": {
      "line": 3,
      "column": 8
    },
    "end": {
      "line": 4,
      "column": 5
    },
    "parents": {
      "While_2_0": ""
    },
    "children": {},
    "contents": [
      "x = 2"
    ]
  }
}

WHILE_BREAK_CONTINUE ="""while x < 10:
  if x == 5:
    continue
  if x == 1:
    x += 2
    break
  x += 1
x += 2
"""
WHILE_BREAK_CONTINUE_JSON = {
  "While_1_0": {
    "name": "While_1_0",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 7,
      "column": 8
    },
    "parents": {
      "Continue_3_4": "continue",
      "exit_If_4_2": ""
    },
    "children": {
      "If_2_2": "True",
      "exit_While_1_0": ""
    },
    "contents": [
      "while x < 10:\n    ..."
    ]
  },
  "If_2_2": {
    "name": "If_2_2",
    "start": {
      "line": 2,
      "column": 2
    },
    "end": {
      "line": 3,
      "column": 12
    },
    "parents": {
      "While_1_0": "True"
    },
    "children": {
      "Continue_3_4": "",
      "If_4_2": ""
    },
    "contents": [
      "if x == 5:\n    ..."
    ]
  },
  "Continue_3_4": {
    "name": "Continue_3_4",
    "start": {
      "line": 3,
      "column": 4
    },
    "end": {
      "line": 3,
      "column": 12
    },
    "parents": {
      "If_2_2": ""
    },
    "children": {
      "While_1_0": "continue"
    },
    "contents": [
      "continue"
    ]
  },
  "If_4_2": {
    "name": "If_4_2",
    "start": {
      "line": 4,
      "column": 2
    },
    "end": {
      "line": 6,
      "column": 9
    },
    "parents": {
      "If_2_2": ""
    },
    "children": {
      "AugAssign_5_4": "True",
      "exit_If_4_2": ""
    },
    "contents": [
      "if x == 1:\n    ..."
    ]
  },
  "AugAssign_5_4": {
    "name": "AugAssign_5_4",
    "start": {
      "line": 5,
      "column": 4
    },
    "end": {
      "line": 5,
      "column": 10
    },
    "parents": {
      "If_4_2": "True"
    },
    "children": {
      "Break_6_4": ""
    },
    "contents": [
      "x += 2"
    ]
  },
  "Break_6_4": {
    "name": "Break_6_4",
    "start": {
      "line": 6,
      "column": 4
    },
    "end": {
      "line": 6,
      "column": 9
    },
    "parents": {
      "AugAssign_5_4": ""
    },
    "children": {
      "exit_While_1_0": "break"
    },
    "contents": [
      "break"
    ]
  },
  "exit_While_1_0": {
    "name": "exit_While_1_0",
    "start": {
      "line": 7,
      "column": 8
    },
    "end": {
      "line": 8,
      "column": 6
    },
    "parents": {
      "Break_6_4": "break",
      "While_1_0": ""
    },
    "children": {},
    "contents": [
      "x += 2"
    ]
  },
  "exit_If_4_2": {
    "name": "exit_If_4_2",
    "start": {
      "line": 6,
      "column": 9
    },
    "end": {
      "line": 7,
      "column": 8
    },
    "parents": {
      "If_4_2": ""
    },
    "children": {
      "While_1_0": ""
    },
    "contents": [
      "x += 1"
    ]
  }
}

BASIC_TRY = """try:
  x += 1
except ArithmeticError as e:
  print(x)
"""
BASIC_TRY_JSON = {
  "Try_1_0": {
    "name": "Try_1_0",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 4,
      "column": 10
    },
    "parents": {},
    "children": {
      "AugAssign_2_2": "try"
    },
    "contents": [
      "try:\n    ...\nexcept ArithmeticError as e:\n    ..."
    ]
  },
  "AugAssign_2_2": {
    "name": "AugAssign_2_2",
    "start": {
      "line": 2,
      "column": 2
    },
    "end": {
      "line": 2,
      "column": 8
    },
    "parents": {
      "Try_1_0": "try"
    },
    "children": {
      "Expr_4_2": "excepts",
      "exit_Try_1_0": ""
    },
    "contents": [
      "x += 1"
    ]
  },
  "Expr_4_2": {
    "name": "Expr_4_2",
    "start": {
      "line": 4,
      "column": 2
    },
    "end": {
      "line": 4,
      "column": 10
    },
    "parents": {
      "AugAssign_2_2": "excepts"
    },
    "children": {
      "exit_Try_1_0": ""
    },
    "contents": [
      "print(x)"
    ]
  },
  "exit_Try_1_0": {
    "name": "exit_Try_1_0",
    "start": {
      "line": 4,
      "column": 10
    },
    "end": {
      "line": 4,
      "column": 10
    },
    "parents": {
      "AugAssign_2_2": "",
      "Expr_4_2": ""
    },
    "children": {},
    "contents": []
  }
}

TRY_WITH_FINALLY_ELSE = """try:
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
TRY_WITH_FINALLY_ELSE_JSON =  {
  "Try_1_0": {
    "name": "Try_1_0",
    "start": {
      "line": 1,
      "column": 0
    },
    "end": {
      "line": 10,
      "column": 18
    },
    "parents": {},
    "children": {
      "AugAssign_2_2": "try"
    },
    "contents": [
      "try:\n    ...\nexcept ArithmeticError:\n    ...\nexcept Exception:\n    ...\nelse:\n    ...\nfinally:\n    ..."
    ]
  },
  "AugAssign_2_2": {
    "name": "AugAssign_2_2",
    "start": {
      "line": 2,
      "column": 2
    },
    "end": {
      "line": 2,
      "column": 8
    },
    "parents": {
      "Try_1_0": "try"
    },
    "children": {
      "Expr_4_2": "excepts",
      "Expr_6_2": "excepts",
      "Expr_8_2": "False"
    },
    "contents": [
      "x += 1"
    ]
  },
  "Expr_4_2": {
    "name": "Expr_4_2",
    "start": {
      "line": 4,
      "column": 2
    },
    "end": {
      "line": 4,
      "column": 21
    },
    "parents": {
      "AugAssign_2_2": "excepts"
    },
    "children": {
      "Expr_10_2": "finally"
    },
    "contents": [
      "print('arithmetic')"
    ]
  },
  "Expr_6_2": {
    "name": "Expr_6_2",
    "start": {
      "line": 6,
      "column": 2
    },
    "end": {
      "line": 6,
      "column": 20
    },
    "parents": {
      "AugAssign_2_2": "excepts"
    },
    "children": {
      "Expr_10_2": "finally"
    },
    "contents": [
      "print('exception')"
    ]
  },
  "Expr_8_2": {
    "name": "Expr_8_2",
    "start": {
      "line": 8,
      "column": 2
    },
    "end": {
      "line": 8,
      "column": 15
    },
    "parents": {
      "AugAssign_2_2": "False"
    },
    "children": {
      "Expr_10_2": "finally"
    },
    "contents": [
      "print('else')"
    ]
  },
  "exit_Try_1_0": {
    "name": "exit_Try_1_0",
    "start": {
      "line": 10,
      "column": 18
    },
    "end": {
      "line": 10,
      "column": 18
    },
    "parents": {
      "Expr_10_2": ""
    },
    "children": {},
    "contents": []
  },
  "Expr_10_2": {
    "name": "Expr_10_2",
    "start": {
      "line": 10,
      "column": 2
    },
    "end": {
      "line": 10,
      "column": 18
    },
    "parents": {
      "Expr_8_2": "finally",
      "Expr_4_2": "finally",
      "Expr_6_2": "finally"
    },
    "children": {
      "exit_Try_1_0": ""
    },
    "contents": [
      "print('finally')"
    ]
  }
}

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
          "def nice(self):\n    ..."
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
          "def bar():\n    ..."
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
          "def foo_bar():\n    ..."
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
          "def baz():\n    ..."
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
          "def nice():\n    ..."
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
          "def nice():\n    ..."
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
