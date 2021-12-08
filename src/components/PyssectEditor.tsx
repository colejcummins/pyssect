import React from 'react';

import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import oneDark from 'react-syntax-highlighter/dist/esm/styles/hljs/atom-one-dark';

const PyssectEditor = ({text}: {text: string}): JSX.Element => {

  SyntaxHighlighter.registerLanguage('python', python);

  return (
    <div
      style={{
        width: '30%',
        height: '100%'
      }}
    >
      <SyntaxHighlighter
        customStyle={{ fontSize: '14px', padding: '5px', margin: '10px'}}
        language="python"
        style={oneDark}
      >
        {text}
      </SyntaxHighlighter>
    </div>
  );
}

export default React.memo(PyssectEditor);
