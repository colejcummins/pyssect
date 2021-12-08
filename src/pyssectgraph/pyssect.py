import sys

from builders import builds_file
from serializers import pyssect_dumps

def main():
  cfg = builds_file(sys.argv[1])
  print(cfg)
  out = pyssect_dumps(cfg)
  print(out)

if __name__ == '__main__':
  main()