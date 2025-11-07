import socket
from threading import Thread

HOST='127.0.0.1'
PORT = 65432

clinets_conn={}
clinets_name={}


def init_server():
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.lisee(5)


def run_chat_server():
    server=init_server()


if __name__ == "__main__":
    run_chat_server()