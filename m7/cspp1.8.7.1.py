def a(x):
   '''
   x: int or float.
   '''
   return x + 1

def b(x):
   '''
   x: int or float.
   '''
   return x + 1.0
  
def c(x, y):
   '''
   x: int or float. 
   y: int or float.
   '''
   return x + y

def d(x, y):
   '''
   x: Can be of any type.
   y: Can be of any type.
   '''
   return x > y

def e(x, y, z):
   '''
   x: Can be of any type.
   y: Can be of any type.
   z: Can be of any type.
   '''
   return x >= y and x <= z

def f(x, y):
   '''
   x: int or float.
   y: int or float
   '''
   x + y - 2  

def main():
    print(a(6))
    type(a(6))
    print(a(-5.3))
    type(a(-5.3))
    print(a(a(a(6)))
    type(a(a(a(6))))
    print(c(a(1), b(1)))
    type(c(a(1), b(1)))
    print(d('apple', 11.1))
    type(d('apple', 11.1))
    print(e(a(3), b(4), c(3, 4)))
    type(e(a(3), b(4), c(3, 4)))
    print(f)
    type(f)
if __name__ == '__main__':
   main()

