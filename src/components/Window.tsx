import React from 'react';

import PyssectEditor from './PyssectEditor';
import PyssectGraph from './PyssectGraph';

const Window = () => {

  return (
    <div
      style={{
        width: '100vw',
        height: '100vh',
        display: 'flex'
      }}
    >
      <PyssectGraph
        name={'test'}
        root={'root'}
        nodes={{
          "root": {
            "name": "root",
            "type": "Assign",
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
              "x = 0"
            ]
          },
          "While_2_0": {
            "name": "While_2_0",
            "type": "",
            "start": {
              "line": 2,
              "column": 0
            },
            "end": {
              "line": 7,
              "column": 12
            },
            "parents": {
              "root": "",
              "Continue_7_4": "continue",
              "If_6_2": ""
            },
            "children": {
              "AugAssign_3_2": "True",
              "exit_While_2_0": ""
            },
            "contents": [
              "while x > 10:\n    ..."
            ]
          },
          "AugAssign_3_2": {
            "name": "AugAssign_3_2",
            "type": "",
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
              "If_4_2": ""
            },
            "contents": [
              "x += 1"
            ]
          },
          "If_4_2": {
            "name": "If_4_2",
            "type": "",
            "start": {
              "line": 4,
              "column": 2
            },
            "end": {
              "line": 5,
              "column": 10
            },
            "parents": {
              "AugAssign_3_2": ""
            },
            "children": {
              "AugAssign_5_4": "True",
              "If_6_2": ""
            },
            "contents": [
              "if x % 2 == 0:\n    ..."
            ]
          },
          "AugAssign_5_4": {
            "name": "AugAssign_5_4",
            "type": "",
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
              "If_6_2": ""
            },
            "contents": [
              "x *= 2"
            ]
          },
          "If_6_2": {
            "name": "If_6_2",
            "type": "",
            "start": {
              "line": 6,
              "column": 2
            },
            "end": {
              "line": 7,
              "column": 12
            },
            "parents": {
              "AugAssign_5_4": "",
              "If_4_2": ""
            },
            "children": {
              "Continue_7_4": "",
              "While_2_0": ""
            },
            "contents": [
              "if x == 7:\n    ..."
            ]
          },
          "Continue_7_4": {
            "name": "Continue_7_4",
            "type": "",
            "start": {
              "line": 7,
              "column": 4
            },
            "end": {
              "line": 7,
              "column": 12
            },
            "parents": {
              "If_6_2": ""
            },
            "children": {
              "While_2_0": "continue"
            },
            "contents": [
              "continue"
            ]
          },
          "exit_While_2_0": {
            "name": "exit_While_2_0",
            "type": "Expr",
            "start": {
              "line": 7,
              "column": 12
            },
            "end": {
              "line": 8,
              "column": 8
            },
            "parents": {
              "While_2_0": ""
            },
            "children": {},
            "contents": [
              "print(x)"
            ]
          }
        }}
      />
      <PyssectEditor text={`x = 0
while x > 10:
  x += 1
  if x % 2 == 0:
    x *= 2
  if x == 7:
    continue
print(x)`}/>
    </div>

  );


};

export default React.memo(Window);