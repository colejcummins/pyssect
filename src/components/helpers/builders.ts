import { IPyssectGraph, IPyssectNode } from "../types";
import { walkGraph } from "./traverse";
import { Elements } from 'react-flow-renderer';


export function buildFlow(graph: IPyssectGraph): Elements {
  return Array.from(walkGraph(graph)).flatMap((node, ind) =>
    [
      {
        id: node.name,
        type: 'pyssectNode',
        data: {
          node
        },
        position: { x: ind * 80, y: ind * 80 }
      }, ...Object.entries(node.children).map(([key, value]) => ({
        id: `${node.name}-${key}`,
        source: node.name,
        target: key,
        sourceHandle: value.toString(),
        targetHandle: value.toString(),
        label: value
      }))
    ]
  )
}


