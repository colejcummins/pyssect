import React from 'react';
import styled from 'styled-components';
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import purple from 'react-syntax-highlighter/dist/esm/styles/hljs/shades-of-purple';
import { ASTType, Location } from './types';


const StyledPyssectNode = styled.div`
  display:inline-block;
  padding-right: 10px;
  background: rgb(45, 43, 87);
  border-radius: 5px;
`;


interface PyssectNodeProps {
  start: Location
  astType: ASTType
  content: string
}


const PyssectNode: React.FC<PyssectNodeProps> = props => {
  const {
    astType,
    start,
    content
  } = props;

  SyntaxHighlighter.registerLanguage('python', python);

  return (
    <StyledPyssectNode>
      <SyntaxHighlighter
        customStyle={{ 'font-size': '10px' }}
        language="python"
        showLineNumbers={true}
        startingLineNumber={start.line}
        style={purple}
      >
        {content}
      </SyntaxHighlighter>
    </StyledPyssectNode>
  );
}

export default PyssectNode