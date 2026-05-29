import numpy as np

num = 600851475143
pfactors = []
for i in range(2, int(np.sqrt(num))):
  if num%i == 0:
    f_of_f = []
    for n in range(2, i):
      if i%n == 0:
        f_of_f.append(n)
    if len(f_of_f) == 0:
      pfactors.append(i)
print(pfactors)