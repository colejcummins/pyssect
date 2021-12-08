import pdb
from typing import Any
from types import FrameType
import dis
import bdb
import sys
import subprocess

def arbitrary_fun(a, b):
  a += b
  b += a
  return a + b

def other_arbitrary_fun():
  print(1)
  print(2)
  print(arbitrary_fun(a, b))


def dispatch_function(frame: FrameType, event: str, arg: Any):
  print(f'frame: {frame}')
  print(f'event: {event}')
  pass

PYTHON_PROGRAM = """
if __name__ == '__main__':
  print(10)
  print(20)
"""

def main():
  subprocess.run(['python', '-m', 'pdb', 'src/pyssectgraph/tests/cfg_test.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
  # pdb.run('other_arbitrary_fun()')
  pass

if __name__ == '__main__':
  main()