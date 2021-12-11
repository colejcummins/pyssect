import React, { useEffect, useState } from "react";
import ReactFlow, { Elements, MiniMap } from "react-flow-renderer";

import { IPyssectGraph } from './types'
import PyssectNode from './PyssectNode';
import { buildFlow } from './helpers/builders';
import theme from "../theme";

const PyssectGraph: React.FC<IPyssectGraph> = props => {
  let [elements, setElements] = useState<Elements>([]);

  useEffect(() => {
    let flow = buildFlow(props);
    console.log(flow);
    setElements(flow);
  }, []);

  const onLoad = (reactFlowInstance: any) => {
    console.log('flow loaded:', reactFlowInstance);
    reactFlowInstance.fitView();
  };


  return (
    <div style={{width: '70%', height: '100%', backgroundColor: theme.colors.black}}>
      <ReactFlow
        onLoad={onLoad}
        elements={elements}
        nodeTypes={{
          'pyssectNode': PyssectNode
        }}
        snapToGrid={true}
        snapGrid={[10, 10]}
      >
        <MiniMap />
      </ReactFlow>
    </div>
  );
};

export default PyssectGraph;