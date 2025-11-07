import math
import asyncio
import time


class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    async def fibonacci(self, n, memo=None):
        if memo is None:
            memo = {}
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in memo:
            return memo[n]
        else:
            memo[n] = await self.fibonacci(n-1, memo) + await self.fibonacci(n-2, memo)
            return memo[n]

    async def factorial(self, n):
        return math.factorial(n)

    async def square(self, n):
        return n ** 2

    async def cube(self, n):
        return n ** 3

    async def check_async(self):
        tasks = []
        tasks.append(asyncio.gather(*[self.fibonacci(n) for n in self.numbers]))
        tasks.append(asyncio.gather(*[self.factorial(n) for n in self.numbers]))
        tasks.append(asyncio.gather(*[self.square(n) for n in self.numbers]))
        tasks.append(asyncio.gather(*[self.cube(n) for n in self.numbers]))

        # Run all tasks concurrently
        fib_list, fact_list, square_list, cube_list = await asyncio.gather(*tasks)
        return {
            "Fibonacci": fib_list,
            "Factorial": fact_list,
            "Squares": square_list,
            "Cubes": cube_list
        }



if __name__ == "__main__":
    numbers = list(range(1, 11))
    calc = Calculator(numbers)

    start_time = time.time()
    results = asyncio.run(calc.check_async())
    end_time = time.time()

    for key, value in results.items():
        print(f"{key}: {value}")

    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")


#Task 1 multiprocessing

import math
from multiprocessing import Pool, cpu_count



def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

def factorial(n):
    return math.factorial(n)

def square(n):
    return n ** 2

def cube(n):
    return n ** 3




class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def compute_all(self):
        with Pool(processes=cpu_count()) as pool:
            fib_list = pool.map(fibonacci, self.numbers)
            fact_list = pool.map(factorial, self.numbers)
            square_list = pool.map(square, self.numbers)
            cube_list = pool.map(cube, self.numbers)

        return {
            "Fibonacci": fib_list,
            "Factorial": fact_list,
            "Squares": square_list,
            "Cubes": cube_list
        }



if __name__ == "__main__":
    import time

    numbers = list(range(1, 11))
    calc = Calculator(numbers)

    start_time = time.time()
    results = calc.compute_all()
    end_time = time.time()

    for key, value in results.items():
        print(f"{key}: {value}")

    print(f"\nExecution Time: {end_time - start_time:.6f} seconds")



#Task2

import asyncio
import aiohttp
import json

class RedditCommentDownloader:
    def __init__(self, subreddit, limit=100, max_pages=3):
        self.subreddit = subreddit
        self.limit = limit
        self.max_pages = max_pages
        self.headers = {"User-Agent": "CommentCollector/1.0 (by u/example_user)"}
        self.base_url = f"https://www.reddit.com/r/{subreddit}/comments.json"
        self.comments = []

    async def fetch_page(self, session, after=None):
        params = {"limit": self.limit}
        if after:
            params["after"] = after

        async with session.get(self.base_url, headers=self.headers, params=params) as response:
            if response.status != 200:
                print(f"Failed to fetch page: status {response.status}")
                return None
            data = await response.json()
            return data.get("data", {})

    async def get_comments(self):
        async with aiohttp.ClientSession() as session:
            after = None
            for page in range(self.max_pages):
                data = await self.fetch_page(session, after)
                if not data:
                    break

                posts = data.get("children", [])
                if not posts:
                    break

                for post in posts:
                    d = post.get("data", {})
                    self.comments.append({
                        "id": d.get("id"),
                        "author": d.get("author"),
                        "body": d.get("body"),
                        "created_utc": d.get("created_utc"),
                    })

                after = data.get("after")
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

    async def run_async(self):
        await self.get_comments()
        self.save_to_file()

def main():
    subreddit = input("Enter subreddit name (python or SQL): ").strip()
    if not subreddit:
        print("No subreddit data.")
        return

    downloader = RedditCommentDownloader(subreddit=subreddit, limit=100, max_pages=5)
    asyncio.run(downloader.run_async())

if __name__ == "__main__":
    main()



#Task3

import asyncio

async def handle_client(reader, writer):
    addr = writer.get_extra_info("text")
    print(f"Connection established with {addr}")

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                print(f" Client {addr} disconnected")
                break

            message = data.decode().strip()
            print(f"Received from {addr}: {message}")


            writer.write(data)
            await writer.drain()
            print(f" Sent back to {addr}\n")

    except ConnectionResetError:
        print(f"Connection reset by {addr}")
    finally:
        writer.close()
        await writer.wait_closed()
        print(f"Connection closed with {addr}")


async def main():
    host = input("Enter host to bind (default 127.0.0.1): ").strip() or "127.0.0.1"
    port_input = input("Enter port to bind (default 65435): ").strip()
    port = int(port_input) if port_input.isdigit() else 65435

    server = await asyncio.start_server(handle_client, host, port)
    addr = server.sockets[0].getsockname()
    print(f"Asyncio Echo Server running on {addr}")


    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped manually.")