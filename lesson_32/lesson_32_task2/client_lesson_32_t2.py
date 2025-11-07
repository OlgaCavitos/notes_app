import socket


class CaesarClient:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        print(f"Connected to server {self.host}:{self.port}")

    def send_message(self, message):
        self.socket.sendall(message.encode())

    def receive_message(self):
        return self.socket.recv(1024).decode()

    def run(self):
        try:
            self.connect()
            key = input("Enter encryption key (integer): ").strip()
            self.send_message(key)

            response = self.receive_message()
            print("Server:", response.strip())

            if not response.startswith("200"):
                print("Server rejected the key. Exiting.")
                return

            message = input("Enter text to encrypt: ").strip()
            self.send_message(message)

            encrypted = self.receive_message()
            print("\nServer response:", encrypted)

            if encrypted.startswith("200"):
                body = encrypted.split("\n", 1)[1] if "\n" in encrypted else ""
                print("Encrypted text:", body.strip())

        except Exception as e:
            print(f"Error: {e}")
        finally:
            if self.socket:
                self.socket.close()
                print("Connection closed.")


if __name__ == "__main__":
    host = input("Enter server host (default 127.0.0.1): ").strip() or "127.0.0.1"
    port_input = input("Enter server port (default 65432): ").strip()
    port = int(port_input) if port_input.isdigit() else 65432

    print(f"\nConnecting with settings:")
    print(f" - Host: {host}")
    print(f" - Port: {port}")
    print("=" * 30)

    client = CaesarClient(host, port)
    client.run()