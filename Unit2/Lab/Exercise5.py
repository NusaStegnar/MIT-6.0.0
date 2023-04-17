def foo(x, y = 5):
    def bar(x):
        return x + 1
    return bar(y * 2)
foo(3)
# output = 11

def foo(x, y = 5):
   def bar(x):
      return x + 1
   return bar(y * 2)
          
foo(3, 0)
# output = 1

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3, x)

foo(2)
# output = 5

def foo (x):
   def bar (z, x = 0):
      return z + x
   return bar(3)

foo(5)
# output = 3
