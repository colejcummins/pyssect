import pdb
from typing import Any
import bdb
import sys

def arbitrary_fun(a, b):
  a += b
  b += a
  return a + b

def other_arbitrary_fun():
  print(arbitrary_fun)
  a = 2
  b = 3
  print(arbitrary_fun(a, b))


def dispatch_function(frame: bdb.FrameType, event: str, arg: Any):

  pass


def main():
  # pdb.run('other_arbitrary_fun()')
  debugger = bdb.Bdb()
  sys.settrace

  debugger.trace_dispatch()

if __name__ == '__main__':
  main()