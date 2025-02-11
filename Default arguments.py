# default arguments = A default value for certain paramenters
#                     default is used when that argument is omitted
#                     make your functions more flexible reduces # of arguments
#                     1. positional, 2. DEFAULT 3. keyboard 4. arbitrary


import time

def count (end, start = 0):
      for x in range(start, end+1):
          print(x)
          time.sleep(1)
      print("D0NE!")

count(0)
