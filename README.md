# pyssect

## Cole Cummins

### Still a work in progress

Pyssect is a cfg and code flow visualizer built specifically for python.

*Graph:*
---

`python src/pyssectgraph/pyssect.py <input_file>`

Generates the control flow graph of the given python input file and prints to standard out

*Frontend:*
---

`npm start`

Starts the frontend web server

Unfortunately the backend is not yet connected to the frontend. To visualize a control flow graph simply copy and paste the output nodes of the graph generated into the props of the `PyssectGraph` component located in the src/components/Window.tsx file. To add text simply copy paste the input text into the props of the `PyssectEditor` component in that same file.


