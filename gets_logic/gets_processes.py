import multiprocessing as mp
import time
import requests


def download_content(url):
    response = requests.get(url)
    # print(f'Content {url} has length {len(response.content)}')


def processes_function():
    start_time = time.time()

    print('+ Starting process function...')

    URLS = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/comments/1',
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/users/1',
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
    ] * 10

    processes = []

    for url in URLS:
        p = mp.Process(target=download_content, args=(url,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end_time = time.time()

    print("End process function", end_time - start_time)


if __name__ == '__main__':
    processes_function()
