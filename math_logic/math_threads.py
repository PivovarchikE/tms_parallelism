import threading
import time
import random


def threading_function(total_points=15000000, num_of_threads=10):
    start_time = time.time()

    print('+ Starting threading function...')

    points_on_thread = total_points // num_of_threads

    def monte_carlo_pi(n):
        inside = 0
        for _ in range(n):
            x = random.random()
            y = random.random()
            if x * x + y * y <= 1:
                inside += 1
        return inside

    threads = []

    results = [0] * num_of_threads

    def result_collector(i):
        results[i] = monte_carlo_pi(points_on_thread)

    for i in range(num_of_threads):
        t = threading.Thread(target=result_collector, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    total_inside = sum(results)
    pi_estimate = 4 * total_inside / total_points

    end_time = time.time()

    print(f"Result: {pi_estimate}")
    print("End threading function", end_time - start_time)


if __name__ == '__main__':
    threading_function()
