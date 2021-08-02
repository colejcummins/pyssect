import { IPyssectGraph, IPyssectNode } from "../types";
import { walkGraph } from "./traverse";
import { Elements } from 'react-flow-renderer';


export function buildFlow(graph: IPyssectGraph): Elements {
  return Array.from(walkGraph(graph)).flatMap((node, ind) =>
    [
      {
        id: node.name,
        type: 'default',
        data: { text: node.contents },
        position: { x: ind * 40, y: ind * 40 }
      }, ...Object.entries(node.children).map(([key, value]) => ({
        id: `${node.name}-${key}`,
        source: node.name,
        target: key,
        label: value
      }))
    ]
  )
}


