import threading
import time
import requests


def threading_function():
    start_time = time.time()

    print('+ Starting threading function...')

    def download_content(url):
        response = requests.get(url)
        # print(f'Content {url} has length {len(response.content)}')

    urls = [
        'https://jsonplaceholder.typicode.com/posts/1',
        'https://jsonplaceholder.typicode.com/comments/1',
        'https://jsonplaceholder.typicode.com/todos/1',
        'https://jsonplaceholder.typicode.com/users/1',
        'https://jsonplaceholder.typicode.com/posts',
        'https://jsonplaceholder.typicode.com/comments',
        'https://jsonplaceholder.typicode.com/albums',
        'https://jsonplaceholder.typicode.com/photos',
    ] * 10

    threads = []

    for url in urls:
        t = threading.Thread(target=download_content, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end_time = time.time()

    print("End threading function", end_time - start_time)


if __name__ == '__main__':
    threading_function()
