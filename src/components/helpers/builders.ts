import { ArrowHeadType, Edge, Elements } from 'react-flow-renderer';

import { IPyssectGraph, IPyssectNode } from "../types";
import { walkGraph } from "./traverse";
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
  for (let node of walkGraph(graph)) {
    depths[node.depth || 0] = (depths[node.depth || 0] || 0) + 1
  }
  return depths;
}

export function buildFlow(graph: IPyssectGraph): Elements {
  const depths = getDepths(graph);
  return Array.from(walkGraph(graph)).flatMap((node, ind) => {
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


