import socket
from multiprocessing import Process
import os

class Server(Process):
    def __init__(self, server_socket, received_data, client_address):
        super().__init__()
        self.server_socket = server_socket
        self.received_data = received_data
        self.client_address = client_address

    def run(self):
        msg = 'Hi' + self.client_address[0] + ":" + str(self.client_address[1]) + 'Server with proccess ID: ' + str(os.getpid())

        self.server_socket.sendto(str.encode(msg), self.client_address)
        print("Sent to client:", msg)


if __name__ == '__main__':

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    server_address = '127.0.0.1'
    server_port = 10001

    buffer_size = 1024


    server_socket.bind((server_address, server_port))
    print('server up and running at {}:{}'.format(server_address, server_port))
    
    while True:

        data, address = server_socket.recvfrom(buffer_size)
        print('server up and running at {}:{}'.format(server_address, server_port))
        print("message;", data.decode())

        p = Server(server_socket, data, address)
        p.start()
        p.join()