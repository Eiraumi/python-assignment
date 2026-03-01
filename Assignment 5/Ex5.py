import random

def approximate_pi(N):
    inside_circle = 0

    for _ in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            inside_circle += 1

    return 4 * inside_circle / N


if __name__ == "__main__":
    N = int(input("How many random points do you want to generate? "))
    pi_value = approximate_pi(N)
    print("Approximation of pi:", pi_value)
