import React, { useEffect, useState } from "react";
import ReactFlow, { Elements } from "react-flow-renderer";

import { IPyssectGraph } from './types'
import PyssectNode from './PyssectNode';
import { buildFlow } from './helpers/builders';
import theme from "../theme";

const PyssectGraph: React.FC<IPyssectGraph> = props => {
  let [elements, setElements] = useState<Elements>([]);

  useEffect(() => {
    let flow = buildFlow(props);
    setElements(flow);
  }, []);

  const onLoad = (reactFlowInstance: any) => {
    console.log('flow loaded:', reactFlowInstance);
    reactFlowInstance.fitView();
  };


  return (
    <div style={{width: '100%', height: '100%', backgroundColor: theme.colors.black}}>
      <ReactFlow
        onLoad={onLoad}
        elements={elements}
        nodeTypes={{
          'pyssectNode': PyssectNode
        }}
      />
    </div>
  );
};

export default PyssectGraph;