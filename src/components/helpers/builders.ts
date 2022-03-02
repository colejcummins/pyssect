import { ArrowHeadType, Edge, Elements } from 'react-flow-renderer';

import { IPyssectGraph, IPyssectNode } from "../types";
import { breadthFirstWalkGraph, depthFirstWalkGraph } from "./traverse";
import theme from "../../theme";

function buildEdges(node: IPyssectNode): Edge[] {
  return node.children ? Object.entries(node.children).map(([key, value]): Edge => ({
    id: `${node.name}-${key}`,
    source: node.name,
    target: key,
    arrowHeadType: ArrowHeadType.ArrowClosed,
    sourceHandle: `handle-${node.name}-${value.toString() || "default"}`,
    targetHandle: `handle-${key}-${value.toString() || "default"}`,
    label: value,
    style: {
      stroke: theme.colors.white,
    },
    labelBgStyle: {
      fill: theme.colors.black
    },
    labelStyle: {
      fill: theme.colors.white,
      fontSize: '12px'
    }
  })) : [];
}

function getDepths(graph: IPyssectGraph): Record<number, number> {
  const depths: Record<number, number> = {}
  for (let node of depthFirstWalkGraph(graph)) {
    console.log(node);
  }
  return depths;
}

export function buildFlow(graph: IPyssectGraph): Elements {
  return Array.from(breadthFirstWalkGraph(graph)).flatMap((node, ind) => {
    return [
        {
          id: node.name,
          type: 'pyssectNode',
          data: {
            node
          },
          position: { x: 100, y: ind * 100 }
        }, ...buildEdges(node)
      ]
    }
  )
}
