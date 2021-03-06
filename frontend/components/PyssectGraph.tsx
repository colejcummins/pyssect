import React, { useEffect, useState, useCallback } from "react";
import ReactFlow, { Elements, MiniMap, Background, BackgroundVariant } from "react-flow-renderer";

import { IPyssectGraph } from './types'
import PyssectNode from './PyssectNode';
import { buildFlow } from './helpers/builders';
import theme from "../theme";

const PyssectGraph = ({graph}: {graph: IPyssectGraph}): JSX.Element => {
  let [elements, setElements] = useState<Elements>([]);

  const fetchGraph = useCallback(async () => {
    let flow = await buildFlow(graph);
    setElements(flow);
  }, []);

  useEffect(() => {
    fetchGraph();
  }, [fetchGraph]);

  return (
    <div style={{width: '70%', height: '100%', backgroundColor: theme.colors.gray.gray100}}>
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
          nodeColor={theme.colors.gray.gray60}
          maskColor={`${theme.colors.gray.gray20}20`}
          style={{
            background: theme.colors.gray.gray100,
          }}
        />
        <Background
          variant={BackgroundVariant.Dots}
          color={theme.colors.gray.gray60}
          gap={10}
          size={0.5}
        />
      </ReactFlow>
    </div>
  );
};

export default PyssectGraph;