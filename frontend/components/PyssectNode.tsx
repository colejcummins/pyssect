import React from 'react';
import { Handle, Position } from 'react-flow-renderer';

import { IPyssectNode, ControlEvent } from '../lib/types';
import {PythonHighlighter} from './PythonHighlighter'
import theme from '../theme';

interface HandlesProps {
  name: string;
  nodes: Record<string, ControlEvent | string>;
  position: Position;
}

const Handles = React.memo(({name, nodes, position}: HandlesProps): JSX.Element => {
  return (
    <React.Fragment>
      {Object.entries(nodes).map(([_key, value]) => {
        return (
          <Handle
            id={`handle-${name}-${value.toString() || "default"}`}
            type={position === Position.Top ? "target" : "source"}
            position={position}
            isConnectable={false}
            style={{
              border: '0px',
              background: theme.colors.white,
            }}
          />
        );
      })}
    </React.Fragment>
  );
});

const PyssectNode = React.memo((props: IPyssectNode): JSX.Element => {
  const {start, contents, children, parents, name} = props;

  return (
    <div
      style={{
        display: 'flex',
        backgroundColor: theme.colors.gray.gray80,
        borderRadius: theme.radii.default,
      }}
    >
      {parents ? <Handles name={name} nodes={parents} position={Position.Top} /> : null}
      {contents && contents.length > 0 ? <PythonHighlighter text={contents.join('\n')} start={start}/> : null}
      {children ? <Handles name={name} nodes={children} position={Position.Bottom} /> : null}
    </div>
  );
})

export default PyssectNode;