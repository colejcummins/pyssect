import { ControlEvent, IPyssectGraph, IPyssectNode } from "../types";

const EVENTS: (string | ControlEvent)[] = ["True", "False", "try", "excepts", "finally"];

function sortChildrenByEvent(a: [string, string | ControlEvent], b: [string, string | ControlEvent]) {
  return EVENTS.indexOf(a[1]) - EVENTS.indexOf(b[1])
}

export function* walkChildNodes(node: IPyssectNode, graph: IPyssectGraph) {
  for (const [key, _] of Object.entries(node.children).sort(sortChildrenByEvent)) {
    yield graph.nodes[key]
  }
}

export function* breadthFirstWalkGraph(graph: IPyssectGraph) {
  yield* traverseGraph(graph, (ns) => ns.shift())
}

export function* depthFirstWalkGraph(graph: IPyssectGraph) {
  yield* traverseGraph(graph, (ns) => ns.pop())
}

function* traverseGraph(graph: IPyssectGraph, expose: (ns: IPyssectNode[]) => IPyssectNode | undefined) {
  let nodes: IPyssectNode[] = [graph.nodes[graph.root]]
  let visited = new Set<IPyssectNode>()
  while (nodes.length > 0) {
    let node = expose(nodes) as IPyssectNode
    if (!visited.has(node)) {
      visited.add(node)
      yield node
      if (node.children) {
        nodes.push(...walkChildNodes(node, graph))
      }
    }
  }
}

