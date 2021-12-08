import React from 'react';

import PyssectEditor from './PyssectEditor';
import PyssectGraph from './PyssectGraph';

const Window = () => {

  return (
    <div
      style={{
        width: '100vw',
        height: '100vh',

      }}
    >
      <div>Hello World</div>
      <PyssectEditor text={`import sys

from builders import builds_file
from serializers import pyssect_dumps

def main():
  cfg = builds_file(sys.argv[1])
  print(cfg)
  out = pyssect_dumps(cfg)
  print(out)

if __name__ == '__main__':
  main()`}/>
      <PyssectGraph
        name={'test'}
        root={'root'}
        nodes={{
            "root": {
              "name": "root",
              "type": "",
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
                "FunctionDef_6_0": ""
              },
              "contents": []
            },
            "FunctionDef_6_0": {
              "name": "FunctionDef_6_0",
              "type": "",
              "start": {
                "line": 6,
                "column": 0
              },
              "end": {
                "line": 10,
                "column": 12
              },
              "parents": {
                "root": ""
              },
              "children": {
                "If_12_0": ""
              },
              "contents": [
                "def main():\n    ..."
              ]
            },
            "If_12_0": {
              "name": "If_12_0",
              "type": "",
              "start": {
                "line": 12,
                "column": 0
              },
              "end": {
                "line": 13,
                "column": 8
              },
              "parents": {
                "FunctionDef_6_0": ""
              },
              "children": {
                "Expr_13_2": "True",
                "exit_If_12_0": ""
              },
              "contents": [
                "if __name__ == '__main__':\n    ..."
              ]
            },
            "Expr_13_2": {
              "name": "Expr_13_2",
              "type": "",
              "start": {
                "line": 13,
                "column": 2
              },
              "end": {
                "line": 13,
                "column": 8
              },
              "parents": {
                "If_12_0": "True"
              },
              "children": {
                "exit_If_12_0": ""
              },
              "contents": [
                "main()"
              ]
            },
            "exit_If_12_0": {
              "name": "exit_If_12_0",
              "type": "",
              "start": {
                "line": 13,
                "column": 8
              },
              "end": {
                "line": 13,
                "column": 8
              },
              "parents": {
                "Expr_13_2": "",
                "If_12_0": ""
              },
              "children": {},
              "contents": []
            }
          }}
      />
    </div>

  );


};

export default React.memo(Window);