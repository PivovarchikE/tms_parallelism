import multiprocessing as mp
import time
import random


def monte_carlo_pi(n):
    inside = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside += 1
    return inside


def result_collector(n, q):
    result = monte_carlo_pi(n)
    q.put(result)


def processes_function(total_points=15000000, num_of_processes=10):
    start_time = time.time()

    print('+ Starting process function...')

    points_on_process = total_points // num_of_processes

    processes = []
    q = mp.Queue()

    for _ in range(num_of_processes):
        p = mp.Process(target=result_collector, args=(points_on_process, q))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    results = [q.get() for _ in range(num_of_processes)]

    total_inside = sum(results)
    pi_estimate = 4 * total_inside / total_points

    end_time = time.time()

    print(f"Result: {pi_estimate}")
    print("End process function", end_time - start_time)


if __name__ == '__main__':
    processes_function()
