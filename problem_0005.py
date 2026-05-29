number = 20
flag = False
while flag == False:
  if all(number%i == 0 for i in range(1,21)):
    print(number)
    flag = True
    break
  else:
    number += 20