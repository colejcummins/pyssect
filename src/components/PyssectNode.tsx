import React from 'react';
import styled from 'styled-components';

import { Handle, Position } from 'react-flow-renderer';

import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import oneDark from 'react-syntax-highlighter/dist/esm/styles/hljs/atom-one-dark';

import { ASTType, IPyssectNode, Location } from './types';
import theme from '../theme';

interface PyssectNodeProps {
  node: IPyssectNode
}

const StyledHighlighterWrapper = styled.div`
  background-color: ${theme.colors.darkGray};
  border: 2px solid ${theme.colors.lightGray};
  display: flex;
  border-radius: 4px;
`;

const PyssectNode = ({data}: {data: PyssectNodeProps}): JSX.Element => {
  const {start, type, contents, children, parents} = data.node;

  SyntaxHighlighter.registerLanguage('python', python);

  return (
    <StyledHighlighterWrapper>
      {Object.entries(parents).map(([_key, value]) => {
        <Handle
          id={value.toString()}
          type="target"
          position={Position.Top}
          isConnectable={false}
        />
      })}
      <SyntaxHighlighter
        customStyle={{ fontSize: '14px', padding: '5px', margin: '10px'}}
        language="python"
        showLineNumbers={start ? true : false}
        startingLineNumber={start?.line ?? 1}
        style={oneDark}
      >
        {contents}
      </SyntaxHighlighter>
      {Object.entries(children).map(([_key, value]) => {
        <Handle
          id={value.toString()}
          type="source"
          position={Position.Bottom}
          isConnectable={false}
        />
      })}
    </StyledHighlighterWrapper>
  );
}

export default React.memo(PyssectNode);