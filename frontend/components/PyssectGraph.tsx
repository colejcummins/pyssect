import React, { useEffect, useState } from "react";
import ReactFlow, { Elements, MiniMap, Background, BackgroundVariant } from "react-flow-renderer";

import { IPyssectGraph } from '../lib/types'
import PyssectNode from './PyssectNode';
import { buildFlow } from '../lib/builders';
import theme from "../theme";

const PyssectGraph = ({graph}: {graph: IPyssectGraph}): JSX.Element => {
  let [elements, setElements] = useState<Elements>([]);

  useEffect(() => {
    const getGraph = async () => {
      setElements(await buildFlow(graph));
    }
    getGraph();
  }, [graph]);

  return (
    <div style={{width: '70%', height: '100%', backgroundColor: theme.colors.gray[0]}}>
      <ReactFlow
        onLoad={(instance) => instance.fitView()}
        elements={elements}
        nodeTypes={{
          'pyssectNode': PyssectNode
        }}
        snapToGrid={true}
        snapGrid={[10, 10]}
      >
        <MiniMap
          nodeColor={theme.colors.gray[1]}
          maskColor={`${theme.colors.gray[2]}20`}
          style={{
            background: theme.colors.gray[0],
          }}
        />
        <Background
          variant={BackgroundVariant.Dots}
          color={theme.colors.gray[1]}
          gap={10}
          size={0.5}
        />
      </ReactFlow>
    </div>
  );
};

export default PyssectGraph;