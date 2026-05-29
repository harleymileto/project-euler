sum_square = 0
unsquare_sum = 0
for i in range(1,101):
  sum_square += i**2
  unsquare_sum += i
square_sum = unsquare_sum**2
difference = square_sum - sum_square
print(difference)