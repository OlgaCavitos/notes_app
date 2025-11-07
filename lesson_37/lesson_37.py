import socket
from threading import Thread

HOST=''
PORT=65435

#argparse
owner_name='usr_test'

users={}

def read_message(server):
    while True:
        data=server.recv(1024)
        #data > user_name: message



def run_receive_server():
    thread=Thread(target=read_message, args=(server,),daemon=True)
    thread.start()

def run_chating(server):
    data=None
    while data.upper()!='exit'

        user=input("Send to: =>")
        message=input("Enter message: =>")

        data_to_send=f"{user}:{message} if message else"
        server.sendall(data.encode())
        data=data_to_send.upper()

def run_char(owner_name=owner_name,host=HOST,port=PORT):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.connect((host, port))
        server.send(owner_name.encode())


        run_receive_thread(server)
        run_chating(server)





if __name__ == "__main__":
    #parse
    run_chat(owner_name=owner_name,host=HOST,port=PORT)
