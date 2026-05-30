
max_steps = 0
max_stepper = 0
for i in range(1,1000000):
    n=i
    steps = 0
    while n > 1:
        if n%2 == 0:
            n = n / 2
            steps += 1
        else:
            n = 3*n + 1
            steps += 1
    if steps > max_steps:
        max_steps = steps
        max_stepper = i

print(max_stepper)