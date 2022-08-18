import React from 'react';

import theme from '../theme';
import {PythonHighlighter} from './PythonHighlighter';

const PyssectEditor = ({text}: {text: string}): JSX.Element => {

  return (
    <div
      style={{
        width: '30%',
        height: '100%',
        backgroundColor: theme.colors.gray.gray80,
      }}
    >
      <PythonHighlighter
        text={text}
      />
    </div>
  );
}

export default React.memo(PyssectEditor);
