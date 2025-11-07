#Task 1 A shared counter

import threading

counter = 0
rounds = 100_000
lock = threading.Lock()

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:
                counter += 1

if __name__ == "__main__":
    t1 = Counter()
    t2 = Counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Final counter value:", counter)



import threading
import time

counter = 0
rounds = 100_000
lock = threading.Lock()

class Counter(threading.Thread):
    def run(self):
        global counter
        for _ in range(rounds):
            with lock:
                counter += 1

if __name__ == "__main__":
    t1 = Counter()
    t2 = Counter()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Final counter value:", counter)





#Task 3
import requests
import json
import concurrent.futures
from threading import Lock

class RedditCommentDownloader:
    def __init__(self, subreddit, limit=100, max_pages=3):
        self.subreddit = subreddit
        self.limit = limit
        self.max_pages = max_pages
        self.headers = {"User-Agent": "CommentCollector/1.0 (by u/example_user)"}
        self.base_url = f"https://www.reddit.com/r/{subreddit}/comments.json"
        self.comments = []
        self.lock = Lock()  # to protect shared data when writing

    def fetch_page(self, after=None):
        params = {"limit": self.limit}
        if after:
            params["after"] = after

        response = requests.get(self.base_url, headers=self.headers, params=params, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch page (status {response.status_code})")
            return None

        data = response.json().get("data", {})
        posts = data.get("children", [])
        next_after = data.get("after")

        comments = []
        for post in posts:
            d = post.get("data", {})
            comments.append({
                "id": d.get("id"),
                "author": d.get("author"),
                "body": d.get("body"),
                "created_utc": d.get("created_utc"),
            })

        return comments, next_after

    def get_comments(self):
        after_tokens = [None]  # the "after" tokens for pagination
        all_pages = []

        # First, fetch pages sequentially to get pagination tokens
        # because Reddit API requires chaining "after" tokens
        for _ in range(self.max_pages):
            result = self.fetch_page(after_tokens[-1])
            if not result:
                break
            comments, after = result
            if not after:
                break
            after_tokens.append(after)
            all_pages.append(comments)

        # Now, download all these pages in parallel for speed
        print(f"Fetching {len(after_tokens)} pages in parallel...")

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            for after in after_tokens:
                futures.append(executor.submit(self.fetch_page, after))

            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                if result:
                    comments, _ = result
                    with self.lock:
                        self.comments.extend(comments)

        print(f"✅ Total comments received: {len(self.comments)}")

    def save_to_file(self):
        if not self.comments:
            print("No comments to save.")
            return

        self.comments.sort(key=lambda c: c["created_utc"] or 0)
        filename = f"{self.subreddit}_comments.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.comments, f, indent=4, ensure_ascii=False)
        print(f"💾 Saved {len(self.comments)} comments to {filename}")

    def run(self):
        self.get_comments()
        self.save_to_file()


def main():
    subreddit = input("Enter subreddit name (e.g., python): ").strip()
    if not subreddit:
        print("No subreddit data.")
        return

    downloader = RedditCommentDownloader(subreddit=subreddit, limit=100, max_pages=5)
    downloader.run()


if __name__ == "__main__":
    main()