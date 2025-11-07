import requests
import time

def fetch_url(session, url):
    """Fetch the contents of a URL using the provided session."""
    response = session.get(url)
    return response.text


def main():
    urls = [
        "https://example.com/",
        "https://example.org/",
        "https://example.net/"
    ]

    start_time = time.time()
    responses = []

    # Create a session for connection pooling
    with requests.Session() as session:
        for url in urls:
            html = fetch_url(session, url)
            responses.append(html)
            print(f"Got response from {url}: {len(html)} bytes")

    print(f"Total time: {time.time() - start_time:.2f} seconds")


if __name__ == "__main__":
    main()