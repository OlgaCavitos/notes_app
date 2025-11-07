import socket

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

    print(f"\nUDP Client started. Sending to {host}:{port}")

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        while True:
            message = get_message()
            if message.lower() in ('exit', 'quit'):
                print("Exiting client.")
                break
            send_message(client_socket, host, port, message)
            receive_message(client_socket)


if __name__ == "__main__":
    run_client()