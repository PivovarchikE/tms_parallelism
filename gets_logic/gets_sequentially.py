import time
import requests


def sequentially_function():
    start_time = time.time()

    print('+ Starting sequentially function...')

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

    for url in urls:
        response = requests.get(url)

    end_time = time.time()

    print("End sequentially function", end_time - start_time)


if __name__ == '__main__':
    sequentially_function()
