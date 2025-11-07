
# import socket
#
# def encrypt(text, s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]
#         # Encrypt uppercase characters
#         if char.isupper():
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         # Encrypt lowercase characters
#         elif char.islower():
#             result += chr((ord(char) + s - 97) % 26 + 97)
#         else:
#             result += char  # Leave non-letters unchanged
#     return result
#
#
# # Create a TCP/IP socket
# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# # Bind the socket to the port
# server_address = ('localhost', 65432)
# print(f"Starting up on {server_address[0]} port {server_address[1]}")
# sock.bind(server_address)
#
# # Listen for incoming connections
# sock.listen(1)
#
# while True:
#     print("Waiting for a connection...")
#     connection, client_address = sock.accept()
#     try:
#         print("Connection from", client_address)
#
#         # Step 1: Receive the key (first message)
#         key_data = connection.recv(1024).decode().strip()
#         if not key_data.isdigit():
#             print("Invalid key received.")
#             connection.sendall(b"ERROR: Invalid key. Please send an integer.\n")
#             connection.close()
#             continue
#         key = int(key_data)
#         print(f"Encryption key received: {key}")
#
#         # Step 2: Notify client
#         connection.sendall(b"Key received. Send text to encrypt.\n")
#
#         # Step 3: Receive and encrypt text
#         while True:
#             data = connection.recv(1024)
#             if not data:
#                 print("No more data from", client_address)
#                 break
#
#             text = data.decode()
#             print(f"Received text: {text}")
#
#             encrypted_text = encrypt(text, key)
#             print(f"Encrypted text: {encrypted_text}")
#
#             # Step 4: Send encrypted text back
#             connection.sendall(encrypted_text.encode())
#
#     finally:
#         connection.close()
#         print("Connection closed.\n")



# import time
#
# import requests
#
# def main():
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.perf_counter()
#     download_all_sites(sites)
#     duration = time.perf_counter() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")
#
# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)
#
# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} bytes from {url}")
#
# if __name__ == "__main__":
#     main()


# class Dates:
#     def __init__(self, date):
#         self.date = date
#
#     def getDate(self):
#         return self.date
#
#     @staticmethod
#     def toDashDate(date):
#         return date.replace("/", "-")
#
#
# class DatesWithSlashes(Dates):
#     def getDate(self):
#         return Dates.toDashDate(self.date)
#
#
# date = Dates("15-12-2016")
# dateFromDB = DatesWithSlashes("15/12/2016")
#
# if (date.getDate() == dateFromDB.getDate()):
#     print("Equal")
# else:
#     print("Unequal")
#
#
# import threading
# print(threading.active_count())


# import asyncio
#
# async def tcp_client():
#     reader, writer = await asyncio.open_connection("127.0.0.1", 65435)
#     writer.write(b"hello server\n")
#     await writer.drain()
#     data = await reader.read(1024)
#     print(f"Received: {data.decode().strip()}")
#     writer.close()
#     await writer.wait_closed()
#
# asyncio.run(tcp_client())

