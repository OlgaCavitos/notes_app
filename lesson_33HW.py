#Task 1

import requests
def download_robots_txt(url):
    if not url.startswith("http"):
        url = "https://" + url

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
    sites_input = input("\nEnter website: ").strip()

    if not sites_input:
        print("No websites entered. Exit")
        return

    sites = [site.strip() for site in sites_input.split(",") if site.strip()]

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

    def run(self):
        self.get_comments()
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



#Task3

import datetime
import requests
import json


class WeatherApp:
    def __init__(self):
        self.output_file = "weather.txt"
        self.base_url = "https://wttr.in"

    def get_weather(self, city: str) -> str:
        try:
            url = f"{self.base_url}/{city}?format=j1"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return f"[ERROR] Unable to fetch data for '{city}' (HTTP {response.status_code})"

            data = response.json()

            real_city = data["nearest_area"][0]["areaName"][0]["value"]

            if real_city.lower() != city.lower():
                return f"[WARNING] No exact match found for '{city}'. Closest location: {real_city}"


            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            weather_desc = current["weatherDesc"][0]["value"]
            humidity = current["humidity"]
            wind_speed = current["windspeedKmph"]

            result = (
                f"City: {real_city}\n"
                f"Weather: {weather_desc}\n"
                f"Temperature: {temp_c} °C\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_speed} km/h\n"
                f"Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
            return result

        except requests.RequestException as err:
            return f"[ERROR] Network issue: {err}"
        except Exception as err:
            return f"[ERROR] Unexpected issue: {err}"

    def save_to_file(self, text: str):
        with open(self.output_file, "a", encoding="utf-8") as f:
            f.write(text + "\n" + "-" * 40 + "\n")

    def run(self):
        print("Weather App")
        print("Select a city name to get current weather data")
        print("Type 'exit' to quit.\n")

        while True:
            city = input("Enter city name: ").strip()
            if city.lower() in ("exit", "quit"):
                break

            if not city:
                print("Please enter a city name.\n")
                continue

            result = self.get_weather(city)
            print("\n" + result + "\n")


            if not result.startswith(("[ERROR]", "[WARNING]")):
                self.save_to_file(result)
                print(f"Weather data saved to '{self.output_file}'\n")

if __name__ == "__main__":
    WeatherApp().run()