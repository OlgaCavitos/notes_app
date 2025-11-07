# #Task2
# import requests
# import json
#
# class RedditCommentDownloader:
#
#     def __init__(self, subreddit, limit=100, max_pages=3):
#         self.subreddit = subreddit
#         self.limit = limit
#         self.max_pages = max_pages
#         self.headers={"User-Agent": "CommentCollector/1.0 (by u/example_user)"}
#         self.base_url = f"https://www.reddit.com/r/{subreddit}/comments.json"
#         self.comments=[]
#
#     def get_comments(self):
#         after = None
#
#         for page in range(self.max_pages):
#             params = {"limit": self.limit}
#             if after:
#                 params["after"] = after
#             response = requests.get(self.base_url, headers=self.headers, params=params)
#
#             if response.status_code != 200:
#                 break
#
#             data = response.json().get("data", {})
#             posts = data.get("children", [])
#             if not posts:
#                 break
#
#             for post in posts:
#                 d = post.get("data", {})
#                 self.comments.append({
#                     "id": d.get("id"),
#                     "author": d.get("author"),
#                     "body": d.get("body"),
#                     "created_utc": d.get("created_utc"),
#                 })
#
#             after = data.get("after")
#             if not after:
#                 break
#
#         print(f"Total comments received: {len(self.comments)}")
#
#     def save_to_file(self):
#         if not self.comments:
#             print("No comments to save.")
#             return
#
#         self.comments.sort(key=lambda c: c["created_utc"] or 0)
#
#         filename = f"{self.subreddit}_comments.json"
#         with open(filename, "w", encoding="utf-8") as f:
#             json.dump(self.comments, f, indent=4, ensure_ascii=False)
#             print(f"Saved {len(self.comments)} comments to {filename}")
#
#     def run(self):
#         self.get_comments()
#         self.save_to_file()
#
# def main():
#     subreddit = input("Enter subreddit name (e.g., python): ").strip()
#     if not subreddit:
#         print("No subreddit data.")
#         return
#
#     downloader = RedditCommentDownloader(subreddit=subreddit, limit=100, max_pages=5)
#     downloader.run()
#
# if __name__ == "__main__":
#     main()

#Task3


import socket

# -------------------- SERVER Part --------------------
def create_server_socket(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    return sock


def handle_request(request_data):
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    return http_response


def run_server():
    host = input("Enter host to bind (default 127.0.0.1): ").strip() or "127.0.0.1"
    port_input = input("Enter port to bind (default 65435): ").strip()
    port = int(port_input) if port_input.isdigit() else 65435

    with create_server_socket(host, port) as listen_socket:
        while True:
            request_data, client_address = listen_socket.recvfrom(1024)
            response = handle_request(request_data)
            listen_socket.sendto(response, client_address)


# -------------------- CLIENT FUNCTIONS --------------------
def send_message(sock, host, port, message):
    sock.sendto(message.encode('utf-8'), (host, port))


def receive_message(sock, buffer_size=4096):
    response, server_address = sock.recvfrom(buffer_size)
    decoded = response.decode('utf-8')
    return decoded


def get_message():
    msg = input("\nEnter your message (press Enter for default, 'exit' to quit): ")
    if not msg.strip():
        msg = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
    return msg


def run_client():
    host = input("Enter server host (default 127.0.0.1): ").strip() or "127.0.0.1"
    port_input = input("Enter server port (default 65435): ").strip()
    port = int(port_input) if port_input.isdigit() else 65435

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            message = get_message()
            if message.lower() in ('exit', 'quit'):
                break
            send_message(client_socket, host, port, message)
            receive_message(client_socket)


def main():
    print("=== UDP CLIENT/SERVER APPLICATION ===")
    mode = input("Enter mode ('server' or 'client'): ").strip().lower()

    if mode == 'server':
        run_server()
    elif mode == 'client':
        run_client()
    else:
        print("Invalid mode. Please enter 'server' or 'client'.")

if __name__ == "__main__":
    main()