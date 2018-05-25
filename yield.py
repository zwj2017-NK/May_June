class Fab(object):
  def __init__(self, max):
    self.max = max
    self.n, self.a, self.b = 0, 0, 1
    print 'Hello,world!'

  def __iter__(self):
    print 'Haha'
    return self

  def next(self):
    if self.n < self.max:
      r = self.b
      self.a, self.b = self.b, self.a + self.b
      self.n = self.n + 1
      return r
    raise StopIteration()
for n in Fab(5):
  print n  


def fab(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n = n + 1

for n in fab(5):
  print n  

from inspect import isgeneratorfunction
if isgeneratorfunction(fab):
  print 'fab is a generator function!'

import types
if not isinstance(fab, types.GeneratorType):
  print 'fab is a generator function, not a generator!'
if isinstance(fab(5), typesGeneratorType):
  print 'fab is a generator function, not a generator!'

from collections import Iterable
if not isinstance(fab, Iterable)
  print 'fab cannot be iterable!'
if isinstance(fab(5), Iterable):
  print 'fab(5) can be iterable!'

def read_file(fpath):
  BLOCK_SIZE = 1024
  with open(fpath, 'rb') as f:
    while True:
      block = f.read(BLOCK_SIZE)
      if block:
	yield block
      else:
	return


