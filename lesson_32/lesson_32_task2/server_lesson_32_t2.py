import socket

class CaesarServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None

    @staticmethod
    def encrypt(text, key):
        result = ""
        for char in text:
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result

    def start_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)
        print(f"Server started on {self.host or '0.0.0.0'}:{self.port}")

    def send_response(self, connection, code, message):
        response = f"{code} {self.status_message(code)}\n{message}\n"
        connection.sendall(response.encode())

    @staticmethod
    def status_message(code):
        messages = {
            200: "OK",
            400: "Bad Request",
            404: "Not Found",
            503: "Service Unavailable",
        }
        return messages.get(code, "Unknown Status")

    def handle_client(self, connection, client_address):
        try:
            print(f"Connection from {client_address}")

            key_data = connection.recv(1024).decode().strip()
            if not key_data.isdigit():
                print("Invalid key received.")
                self.send_response(connection, 400, "Invalid key. Expected an integer.")
                return

            key = int(key_data)
            print(f"Encryption key received: {key}")


            self.send_response(connection, 200, "Key accepted. Send text to encrypt.")

            data = connection.recv(1024)
            if not data:
                print("No text received.")
                self.send_response(connection, 404, "No text provided for encryption.")
                return

            text = data.decode().strip()
            print(f"Received text: {text}")

            try:
                encrypted = self.encrypt(text, key)
                print(f"Encrypted text: {encrypted}")
                self.send_response(connection, 200, encrypted)
            except Exception as e:
                print(f"Encryption failed: {e}")
                self.send_response(connection, 503, f"Encryption error: {e}")

        finally:
            connection.close()
            print(f"Connection with {client_address} closed.\n")

    def run(self):
        self.start_server()
        try:
            while True:
                print("Waiting for a connection...")
                conn, addr = self.server_socket.accept()
                self.handle_client(conn, addr)
        except KeyboardInterrupt:
            print("\nServer stopped manually.")
        finally:
            if self.server_socket:
                self.server_socket.close()
                print("Server socket closed.")


if __name__ == "__main__":
    host = input("Enter host to bind 127.0.0.1: ").strip()
    port_input = input("Enter port to bind (default 65432): ").strip()
    port = int(port_input) if port_input.isdigit() else 65432

    print(f"\nStarting server with settings:")
    print(f" - Host: {host or '0.0.0.0'}")
    print(f" - Port: {port}")
    print("=" * 30)

    server = CaesarServer(host, port)
    server.run()