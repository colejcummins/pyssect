
/* Pyssect Graph JSON types */

export interface Location {
  line: number;
  column: number;
}


export enum ControlEvent {
  False,
  True,
  Call,
  Return,
  Excepts,
  Break,
  Continue,
  Yield,
  Try,
  Finally
}


export enum ASTType {
  If,
  For,
  While,
  Try,
  FunctionDef,
  Default
}


export interface IPyssectNode {
  name: string;
  type?: ASTType;
  start?: Location;
  end?: Location;
  contents: any[];
  children: { [key: string]: ControlEvent };
  parents: { [key: string]: ControlEvent };
}


export interface IPyssectGraph {
  name: string;
  root: string;
  nodes: { [key: string]: IPyssectNode };
}


export interface IPyssectGraphDict {
  [key: string]: IPyssectGraph
}