import numpy as np

i=2
primes = []
while len(primes)<10001:
  factors = []
  for n in range(1,int(np.sqrt(i))+1):
    if i%n == 0:
      factors.append(n)
  if len(factors) == 1:
    primes.append(i)
  i +=1

print(max(primes))