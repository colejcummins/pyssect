import React from 'react';
import { Handle, Position } from 'react-flow-renderer';

import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import oneDark from 'react-syntax-highlighter/dist/esm/styles/hljs/atom-one-dark';

import { ASTType, IPyssectNode, Location, ControlEvent } from './types';
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
  const {start, type, contents, children, parents, name} = props;

  SyntaxHighlighter.registerLanguage('python', python);

  return (
    <div
      style={{
        backgroundColor: theme.colors.gray.gray80,
        display: 'flex',
        borderRadius: '4px',
      }}
    >
      {parents ? <Handles name={name} nodes={parents} position={Position.Top} /> : null}
      {contents && contents.length > 0 ? (
        <SyntaxHighlighter
          customStyle={{ fontSize: '15px', padding: '5px', margin: '10px', background: theme.colors.gray.gray80}}
          language="python"
          showLineNumbers={start ? true : false}
          startingLineNumber={start?.line ?? 1}
          style={oneDark}
        >
          {contents}
        </SyntaxHighlighter>
      ) : null}
      {children ? <Handles name={name} nodes={children} position={Position.Bottom} /> : null}
    </div>
  );
})

export default PyssectNode;