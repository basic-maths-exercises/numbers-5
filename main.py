import numpy as np

def convertToBase( N, base ) :
  # Your code goes here
  number = np.zeros(7)
  for i in range(7) :
     ppp = base**(6-i)
     number[i] = np.floor( N / ppp )
     N = N - number[i]*ppp
  return number

# This will print some output that will allow you to test your function
for b in range(2,10) :
  for n in range(10) :
    print("The number", n, "in base", b, "is", convertToBase(n,b) )
