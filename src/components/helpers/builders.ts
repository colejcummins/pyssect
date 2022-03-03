import { ArrowHeadType, Edge, Elements } from 'react-flow-renderer';
import ELK, {ElkEdge, ElkNode} from 'elkjs/lib/elk.bundled.js';

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
      fill: theme.colors.gray.gray100
    },
    labelStyle: {
      fill: theme.colors.white,
      fontSize: '12px'
    }
  })) : [];
}

function layoutEdges(node: IPyssectNode) {
  return node.children ? Object.entries(node.children).map(([key, _value]) => ({
    id: `${node.name}-${key}`,
    source: node.name,
    target: key,
  })) : []
}

function layoutPositions(graph: IPyssectGraph) {
  const children: ElkNode[] = [];
  const edges = [];
  let ind = 0;
  for (let node of breadthFirstWalkGraph(graph)) {
    children.push({
      id: node.name,
      // TODO - add more accurate dimensions
      width: 150,
      height: Math.max((node.contents.length * 30) + 30, 100),
      layoutOptions: {
        partition: ind.toString(),
      }
    });
    edges.push(...layoutEdges(node));
    ind += 1;
  }

  const elkGraph = {
    id: 'root',
    children: children,
    edges: edges
  }

  return (new ELK()).layout(elkGraph, {
    layoutOptions: {
			algorithm: 'layered',
      'elk.direction': 'DOWN',
      'partitioning.activate': 'true',
      nodeSpacing: '10',
    }
  })
}

export async function buildFlow(graph: IPyssectGraph) {
  const positions = await layoutPositions(graph);
  const children = Object.fromEntries(
    positions.children!.map(e => [e.id, {x: e.x!, y: e.y!}])
  );

  return Array.from(breadthFirstWalkGraph(graph)).flatMap((node, ind) => {
    return [
        {
          id: node.name,
          type: 'pyssectNode',
          data: {
            node
          },
          position: { x: children[node.name].x, y: children[node.name].y }
        }, ...buildEdges(node)
      ]
    }
  )
}
