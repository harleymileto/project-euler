from math import prod

def isTriplet(trip):
  if trip[0]**2 + trip[1]**2 == trip[2]**2:
    return True
  else:
    return False

triplets = [(a, b, 1000-a-b) for a in range(1,999) for b in range(a,999) if a<b<1000-a-b]
for trip in triplets:
  if isTriplet(trip) == True:
    print(prod(trip))