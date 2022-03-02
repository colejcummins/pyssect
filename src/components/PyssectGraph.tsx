import React, { useEffect, useState } from "react";
import ReactFlow, { Elements, MiniMap, Background, BackgroundVariant } from "react-flow-renderer";

import { IPyssectGraph } from './types'
import PyssectNode from './PyssectNode';
import { buildFlow } from './helpers/builders';
import theme from "../theme";

const PyssectGraph: React.FC<IPyssectGraph> = props => {
  let [elements, setElements] = useState<Elements>([]);

  console.log(props);
  useEffect(() => {
    let flow = buildFlow(props);
    console.log(flow);
    setElements(flow);
  }, []);

  return (
    <div style={{width: '70%', height: '100%', backgroundColor: theme.colors.black}}>
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
          nodeColor={theme.colors.darkGray}
        />
        <Background
          variant={BackgroundVariant.Dots}
          color={theme.colors.gray}
          gap={10}
          size={0.5}
        />
      </ReactFlow>
    </div>
  );
};

export default PyssectGraph;