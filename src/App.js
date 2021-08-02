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
      nodes={{
        "root": {
          "name": "root",
          "contents": [
            "x = 1"
          ],
          "children": {
            "While_3_0": ""
          },
          "parents": {}
        },
        "While_3_0": {
          "name": "While_3_0",
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
          "name": "AugAssign_4_2",
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
          "name": "exit_While_3_0",
          "contents": [
            "x = 2"
          ],
          "children": {},
          "parents": {
            "While_3_0": ""
          }
        }
      }}
    />
  );
}

export default App;
