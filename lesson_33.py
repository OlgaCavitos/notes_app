# import requests
#
# email = 'Jayne_Kuhic@sydney.com'
# def get_email_post(email):
#     URL_1 = "https://jsonplaceholder.typicode.com/comments?postId=1"
#     response = requests.get(URL_1)
#     if response.status_code == 200:
#         comments = response.json()
#
#         user_comments = [com for com in comments if com['email'] == email]
#
#     return user_comments
#
# print(get_email_post(email))

#Task 1
import requests

def download_robots_txt(url):
    if not url.startswith("http"):
        url = "https://" + url

    # Ensure robots.txt path is appended
    if not url.endswith("/robots.txt"):
        if url.endswith("/"):
            url += "robots.txt"
        else:
            url += "/robots.txt"
    print(f"Downloading robots.txt from: {url}")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print(f"Successfully downloaded ({len(response.text)} bytes)")
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading robots.txt: {e}")
        return None


def save_to_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved to file: {filename}")
    except Exception as e:
        print(f" Error saving to file: {e}")


def main():
    print("Sites examples to select: wikipedia.org, twitter.com")
    sites_input = input("\nEnter one or more website domains (comma-separated): ").strip()

    if not sites_input:
        print("No websites entered. Exiting.")
        return

    # Split by commas and remove extra spaces
    sites = [site.strip() for site in sites_input.split(",") if site.strip()]

    # Process each site
    for site in sites:
        content = download_robots_txt(site)
        if content:
            domain = site.replace("https://", "").replace("http://", "").split("/")[0]
            filename = f"{domain}_robots.txt"
            save_to_file(filename, content)
        else:
            print(f"Skipping {site} due to error.\n")

if __name__ == "__main__":
    main()



#Task2
import requests
import json

class RedditCommentDownloader:

    def __init__(self, subreddit, limit=100, max_pages=3):
        self.subreddit = subreddit
        self.limit = limit
        self.max_pages = max_pages
        self.headers={"User-Agent": "CommentCollector/1.0 (by u/example_user)"}
        self.base_url = f"https://www.reddit.com/r/{subreddit}/comments.json"
        self.comments=[]

    def get_comments(self):
        after = None

        for page in range(self.max_pages):
            params = {"limit": self.limit}
            if after:
                params["after"] = after
            response = requests.get(self.base_url, headers=self.headers, params=params)

            if response.status_code != 200:
                break

            data = response.json().get("data", {})
            posts = data.get("children", [])
            if not posts:
                break

            for post in posts:
                d = post.get("data", {})
                self.comments.append({
                    "id": d.get("id"),
                    "author": d.get("author"),
                    "body": d.get("body"),
                    "created_time": d.get("created_time"),
                })

            after = data.get("after")
            if not after:
                break

        print(f"Total comments received: {len(self.comments)}")

    def save_to_file(self):
        if not self.comments:
            print("No comments to save.")
            return

        self.comments.sort(key=lambda c: c["created_time"] or 0)

        filename = f"{self.subreddit}_comments.json"
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.comments, f, indent=4, ensure_ascii=False)
            print(f"Saved {len(self.comments)} comments to {filename}")

    def run(self):
        self.get_comments()
        self.save_to_file()

def main():
    subreddit = input("Enter subreddit name (e.g., python): ").strip()
    if not subreddit:
        print("No subreddit data.")
        return

    downloader = RedditCommentDownloader(subreddit=subreddit, limit=1000, max_pages=10)
    downloader.run()

if __name__ == "__main__":
    main()