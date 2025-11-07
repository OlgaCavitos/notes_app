import socket

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
    host = input("Enter host to bind (default 127.0.0.1): ").strip()
    port_input = input("Enter port to bind (default 65435): ").strip()
    port = int(port_input) if port_input.isdigit() else 65435

    with create_server_socket(host, port) as listen_socket:
        while True:
            request_data, client_address = listen_socket.recvfrom(1024)
            response = handle_request(request_data)
            listen_socket.sendto(response, client_address)
            print(f"Response sent to {client_address}\n")

if __name__ == "__main__":
    run_server()