import logo from './logo.svg';
import './App.css';

import { PyssectNode } from './components/PyssectNode';
import PyssectGraph from './components/PyssectGraph';
import { ASTType } from './components/types';

function App() {
  return (
    <PyssectGraph
      name={'test'}
      root={'root'}
      nodes={{"root": {
        "name": "root",
        "type": "Assign",
        "start": {
          "line": 1,
          "column": 0
        },
        "end": {
          "line": 2,
          "column": 5
        },
        "parents": {},
        "children": {
          "If_3_0": ""
        },
        "contents": [
          "x = 1"
        ]
      },
      "If_3_0": {
        "name": "If_3_0",
        "type": "",
        "start": {
          "line": 3,
          "column": 0
        },
        "end": {
          "line": 4,
          "column": 8
        },
        "parents": {
          "root": ""
        },
        "children": {
          "AugAssign_4_2": "True",
          "exit_If_3_0": ""
        },
        "contents": [
          "if x < 4:\n    ..."
        ]
      },
      "AugAssign_4_2": {
        "name": "AugAssign_4_2",
        "type": "",
        "start": {
          "line": 4,
          "column": 2
        },
        "end": {
          "line": 4,
          "column": 8
        },
        "parents": {
          "If_3_0": "True"
        },
        "children": {
          "exit_If_3_0": ""
        },
        "contents": [
          "x += 2"
        ]
      },
      "exit_If_3_0": {
        "name": "exit_If_3_0",
        "type": "AugAssign",
        "start": {
          "line": 4,
          "column": 8
        },
        "end": {
          "line": 5,
          "column": 6
        },
        "parents": {
          "AugAssign_4_2": "",
          "If_3_0": ""
        },
        "children": {},
        "contents": [
          "x -= 1"
        ]
      }
    }}
    />
  );
}

export default App;
