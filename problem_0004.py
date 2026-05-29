def is_palindrome(num):
  s = str(num)
  for i in range(len(s)):
    if str(num)[i] != str(num)[-(i+1)]:
      return False
  return True

best = 0
for a in range(100,1000):
  for b in range (a,1000):
    product = a*b
    if is_palindrome(product):
      best = max(best, product)

print(f"The largest palindrome made from the product of two 3-digit numbers is {best}")