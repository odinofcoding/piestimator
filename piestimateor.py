import random


def estimate_pi(n):
    n_pointcircle = 0
    n_pointtotal = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            n_pointcircle += 1
        n_pointtotal += 1

    return 4 * n_pointcircle / n_pointtotal


print(estimate_pi())
