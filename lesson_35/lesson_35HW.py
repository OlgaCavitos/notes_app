#Task 1

import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time
NUMBERS = [
   2,  # prime
   1099726899285419,
   1570341764013157,  # prime
   1637027521802551,  # prime
   1880450821379411,  # prime
   1893530391196711,  # prime
   2447109360961063,  # prime
   3,  # prime
   2772290760589219,  # prime
   3033700317376073,  # prime
   4350190374376723,
   4350190491008389,  # prime
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,  # prime
]


# Utility function
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(5, limit + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True



#Concurrent Implementations
def filter_primes_threadpool(numbers):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]

def filter_primes_processpool(numbers):
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime, numbers))
    return [num for num, prime in zip(numbers, results) if prime]


# Performance Comparison
def main():
    print("Filtering primes using ThreadPoolExecutor...")
    start = time.perf_counter()
    primes_threads = filter_primes_threadpool(NUMBERS)
    end = time.perf_counter()
    print(f"ThreadPoolExecutor primes: {primes_threads}")
    print(f"Time taken threads: {end - start:.4f} seconds\n")

    print("Filtering primes by using ProcessPoolExecutor...")
    start = time.perf_counter()
    primes_processes = filter_primes_processpool(NUMBERS)
    end = time.perf_counter()
    print(f"ProcessPoolExecutor primes: {primes_processes}")
    print(f"Time taken processes: {end - start:.4f} seconds\n")

    # Verify results are identical
    assert primes_threads == primes_processes, "Results differ!"

if __name__ == "__main__":
    main()


#Task 2

import requests
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

class RedditCommentDownloader:

    def __init__(self, subreddit, limit=100, max_pages=3):
        self.subreddit = subreddit
        self.limit = limit
        self.max_pages = max_pages
        self.headers = {"User-Agent": "CommentCollector/1.0 (by u/example_user)"}
        self.base_url = f"https://www.reddit.com/r/{subreddit}/comments.json"
        self.comments = []

    def fetch_page(self, after=None):
        params = {"limit": self.limit}
        if after:
            params["after"] = after

        response = requests.get(self.base_url, headers=self.headers, params=params)
        if response.status_code != 200:
            return [], None

        data = response.json().get("data", {})
        posts = data.get("children", [])
        comments = []

        for post in posts:
            d = post.get("data", {})
            comments.append({
                "id": d.get("id"),
                "author": d.get("author"),
                "body": d.get("body"),
                "created_utc": d.get("created_utc"),
            })

        return comments, data.get("after")

    def get_comments_concurrent(self):
        after = None
        futures = []

        with ThreadPoolExecutor(max_workers=5) as executor:
            for _ in range(self.max_pages):
                futures.append(executor.submit(self.fetch_page, after))
                comments, after = futures[-1].result()
                self.comments.extend(comments)
                if not after:
                    break

        print(f"Total comments received: {len(self.comments)}")

    def save_to_file(self):
        if not self.comments:
            print("No comments to save.")
            return

        self.comments.sort(key=lambda c: c["created_utc"] or 0)
        filename = f"{self.subreddit}_comments.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.comments, f, indent=4, ensure_ascii=False)
            print(f"Saved {len(self.comments)} comments to {filename}")

    def run(self):
        self.get_comments_concurrent()
        self.save_to_file()


def main():
    subreddit = input("Enter subreddit name (python or SQL): ").strip()
    if not subreddit:
        print("No subreddit data.")
        return

    downloader = RedditCommentDownloader(subreddit=subreddit, limit=100, max_pages=5)
    downloader.run()


if __name__ == "__main__":
    main()


#Task 3 Echo server with multiprocessing

import socket
import multiprocessing

def handle_client(conn, addr):
    print(f"Connection from {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"Client {addr} disconnected")
                break
            print(f"Received from {addr}: {data.decode().strip()}")
            conn.sendall(data)  # Echo back
            print(f"Sent back to {addr}")
    except ConnectionResetError:
        print(f"Connection reset by {addr}")
    finally:
        conn.close()



def main():
    host = input("Enter host to bind (default 127.0.0.1): ").strip() or "127.0.0.1"
    port_input = input("Enter port to bind (default 65435): ").strip()
    port = int(port_input) if port_input.isdigit() else 65435

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        server_sock.listen()
        print(f"Multiprocessing Echo Server running on {host}:{port}")

        while True:
            conn, addr = server_sock.accept()
            process = multiprocessing.Process(target=handle_client, args=(conn, addr))
            process.daemon = True
            process.start()



if __name__ == "__main__":
    main()