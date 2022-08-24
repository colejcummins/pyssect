import React from 'react';
import { Light as SyntaxHighlighter } from 'react-syntax-highlighter';
import python from 'react-syntax-highlighter/dist/esm/languages/hljs/python';
import oneDark from 'react-syntax-highlighter/dist/esm/styles/hljs/atom-one-dark';

import theme from '../theme';
import { Location } from '../lib/types';

SyntaxHighlighter.registerLanguage('python', python);

export const PythonHighlighter = React.memo(({text, start}: {text: string, start?: Location}) => {
  return (
    <SyntaxHighlighter
      customStyle={{
        fontSize: theme.fontSizes.large,
        padding: theme.spacing.s5,
        margin: theme.spacing.s10,
        background: theme.colors.gray[1]
      }}
      language="python"
      style={oneDark}
      showLineNumbers={true}
      startingLineNumber={start?.line ?? 1}
    >
      {text}
    </SyntaxHighlighter>
  );
});