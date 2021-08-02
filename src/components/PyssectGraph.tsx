import React, { useEffect, useState } from "react";
import ReactFlow, { Elements } from "react-flow-renderer";
import { IPyssectGraph } from './types'

import { buildFlow } from './helpers/builders';


const PyssectGraph: React.FC<IPyssectGraph> = props => {
  let [elements, setElements] = useState<Elements>([]);

  useEffect(() => {
    setElements(buildFlow(props));
  }, []);

  return (
    <ReactFlow
      elements={elements}
    />
  );
};

export default PyssectGraph;