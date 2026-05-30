from math import isqrt

number = 0
i = 1
while True:
    number += i
    i += 1
    factor_count = 0
    for a in range(1,isqrt(number)+1):
        if number%a == 0:
            factor_count += 1
    if factor_count > 250:
        print(number)
        break