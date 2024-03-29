
/* Pyssect Graph JSON types */

export interface Location {
  line: number;
  column: number;
}

export enum ControlEvent {
  False = "False",
  True = "True",
  Call = "Call",
  Return = "Return",
  Excepts = "Excepts",
  Break = "Break",
  Continue = "Continue",
  Yield = "Yield",
  Try = "Try",
  Finally = "Finally"
}

export enum ASTType {
  If,
  For,
  While,
  Try,
  FunctionDef,
  Default
}

/**
 * Represents a single Node in a Control Flow Graph, with a name, a `Location` start and end, a dictionary of parent
 * and child nodes, and a list of contents.
 *
 * AST nodes follow a naming convention of `<AST class>_<start line>_<start column>`, for example
 * `'If_5_2'`.
 */
export interface IPyssectNode {
  name: string;
  type?: ASTType;
  start?: Location;
  end?: Location;
  contents: string[];
  children: Record<string, ControlEvent>;
  parents: Record<string, ControlEvent | string>;
}

export interface FlatNode {
  name: string;
  ind: number;
  type?: ASTType;
  start?: Location;
  end?: Location;
  contents: string[];
}

export interface FlatEdge {
  id: string;
  source: string;
  target: string;
  transition?: ControlEvent;
}

export type FlatGraph = (FlatEdge | FlatNode)[];

export interface IPyssectGraph {
  name: string;
  root: string;
  nodes: Record<string, IPyssectNode>;
}

export interface IPyssectGraphDict {
  [key: string]: IPyssectGraph
}