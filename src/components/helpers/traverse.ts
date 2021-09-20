import { IPyssectGraph, IPyssectNode } from "../types";


export function* walkChildNodes(node: IPyssectNode, graph: IPyssectGraph) {
  for (const key of Object.keys(node.children)) {
    yield graph.nodes[key]
  }
}


export function* walkGraph(graph: IPyssectGraph) {
  let nodes: IPyssectNode[] = [graph.nodes[graph.root]]
  let visited = new Set<IPyssectNode>()
  while (nodes.length > 0) {
    let node = nodes.shift() as IPyssectNode
    if (!visited.has(node)) {
      visited.add(node)
      yield node
      nodes.push(...walkChildNodes(node, graph))
    }
  }
}