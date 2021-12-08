import { PyssectNode } from './components/PyssectNode';
import PyssectGraph from './components/PyssectGraph';
import Window from './components/Window';
import { ASTType } from './components/types';

function App() {
  return (
    <div
      style={{
        width: '100vw',
        height: '100vh'
      }}
    >
      <PyssectGraph
        name="test"
        root="root"
        nodes={{
          "root": {
            "name": "root",
            "contents": [],
            "children": {
              "While_2_0": ""
            },
            "parents": {}
          },
          "While_2_0": {
            "name": "While_2_0",
            "contents": [
              "while x < 10:"
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
            "name": "If_3_2",
            "contents": [
              "if x == 5:"
            ],
            "children": {
              "Continue_4_4": "",
              "exit_If_3_2": ""
            },
            "parents": {
              "While_2_0": "True"
            }
          },
          "Continue_4_4": {
            "name": "Continue_4_4",
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
            "name": "exit_If_3_2",
            "contents": [],
            "children": {
              "If_5_2": "True"
            },
            "parents": {
              "If_3_2": ""
            }
          },
          "If_5_2": {
            "name": "If_5_2",
            "contents": [
              "if x == 1:"
            ],
            "children": {
              "AugAssign_6_4": "True",
              "exit_If_5_2": ""
            },
            "parents": {
              "exit_If_3_2": "True"
            }
          },
          "AugAssign_6_4": {
            "name": "AugAssign_6_4",
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
            "name": "Break_7_4",
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
            "name": "exit_While_2_0",
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
            "name": "exit_If_5_2",
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
        }}
      />
    </div>
  );
}

export default App;
