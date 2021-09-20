import pdb


def arbitrary_fun(a, b):
  a += b
  b += a
  return a + b

def other_arbitrary_fun():
  print(arbitrary_fun)
  a = 2
  b = 3
  print(arbitrary_fun(a, b))


def main():
  pdb.run('other_arbitrary_fun()')

if __name__ == '__main__':
  main()