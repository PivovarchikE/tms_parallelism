import random
import time


def sequentially_function():
    start_time = time.time()

    print('+ Starting sequentially function...')

    def monte_carlo_pi(n):
        inside = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if x * x + y * y <= 1:
                inside += 1
        return 4 * inside / n

    result = monte_carlo_pi(15000000)

    end_time = time.time()

    print(f"Result: {result}")
    print("End sequentially function", end_time - start_time)


if __name__ == '__main__':
    sequentially_function()
