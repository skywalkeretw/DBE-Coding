import socket
from multiprocessing import Process
import os

buffer_size = 1024

def send_message(s_address, s_port):
    # Create a UDP Socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Message sent to server
    message = 'Hi From ' +  str(os.getpid())

    # Send Data
    client_socket.sendto(str.encode(message),(s_address, s_port))
    print('Send to Server: ', message)

    # Recive response from Server
    print('Waiting for response...')
    data, server = client_socket.recvfrom(buffer_size)
    print('Recived message: ', data.decode())

if __name__ == '__main__':
    print("hello")
    server_address = '127.0.0.1'
    server_port = 10001

    for i in range(3):
        p = Process(target=send_message, args=(server_address, server_port))
        p.start()
        p.join()