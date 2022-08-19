import { ArrowHeadType, Edge } from 'react-flow-renderer';
import ELK, {ElkNode, LayoutOptions, ElkEdge} from 'elkjs/lib/elk.bundled.js';

import { IPyssectGraph, IPyssectNode, FlatGraph, FlatEdge, ControlEvent } from "./types";
import { breadthFirstWalkGraph } from "./traverse";
import theme from "../theme";

// TODO: Implement better layouting options for elk
const defaultLayoutOptions = {
  algorithm: 'layered',
  'elk.direction': 'DOWN',
  'partitioning.activate': 'true',
  nodeSpacing: '10',
}

/**
 * Returns the longest string length in a list of strings, used for calculating node size
 */
function getLongestString(contents: string[]) {
  return contents.reduce((a, b) => a.length > b.length ? a : b).length
}

export function flattenEdges(node: IPyssectNode): FlatEdge[] {
  return node.children ? Object.entries(node.children).map(([key, value]) => (
    {
      id: `${node.name}-${key}`,
      source: node.name,
      target: key,
      transition: ControlEvent[value],
    }
  )): [];
}

/**
 * Flattens the graph from a list of nodes with children, to a list of nodes and edges
 */
export function flattenGraph(graph: IPyssectGraph): FlatGraph {
  return Array.from(breadthFirstWalkGraph(graph)).flatMap((node, ind) => {
    const {children, parents, ...flattened} = node;
    return [
      {...flattened, ind},
      ...flattenEdges(node)
    ]
  });
}

function layoutPositions(graph: FlatGraph, layoutOptions: LayoutOptions = {}) {
  const edges: ElkEdge[] = [];
  const children: ElkNode[] = [];
  for (let node of graph) {
    if ("ind" in node) {
      children.push({
        id: node.name,
        // TODO: add more accurate dimensions
        width: Math.max((getLongestString(node.contents) * 20) + 30, 100),
        height: Math.max((node.contents.length * 20) + 30, 100),
        layoutOptions: {
          partition: node.ind.toString(),
        }
      });
    } else {
      const {transition, ...vals} = node;
      edges.push({...vals})
    }
  }

  return (new ELK()).layout({
    id: 'root',
    children: children,
    edges: edges
  }, {layoutOptions: {...defaultLayoutOptions, ...layoutOptions}})
}

function buildEdge(edge: FlatEdge): Edge {
  const {id, source, target, transition} = edge
  return {
    id,
    source,
    target,
    arrowHeadType: ArrowHeadType.ArrowClosed,
    sourceHandle: `handle-${source}-${transition || "default"}`,
    targetHandle: `handle-${target}-${transition || "default"}`,
    label: transition,
    style: {
      stroke: theme.colors.white,
    },
    labelBgStyle: {
      fill: theme.colors.gray.gray100
    },
    labelStyle: {
      fill: theme.colors.white,
      fontSize: theme.fontSizes.default,
    }
  }
}

export async function buildFlow(graph: IPyssectGraph) {
  const flatGraph = flattenGraph(graph);
  const positions = await layoutPositions(flatGraph);
  const children = Object.fromEntries(
    positions.children!.map(e => [e.id, {x: e.x!, y: e.y!}])
  );

  return flatGraph.map((node) => {
    if ("ind" in node) {
      return {
        id: node.name,
        type: "pyssectNode",
        data: {...node},
        position: { x: children[node.name].x, y: children[node.name].y }
      }
    } else {
      return buildEdge(node)
    }
  })
}
