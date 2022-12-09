import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '127.0.0.1'
server_port = 10001

buffer_size = 1024

messge = 'Hi client nice to connect ot you'

server_socket.bind((server_address, server_port))
print('server up and running at {}:{}'.format(server_address, server_port))

while True:
    print("\nWaiting to recive message...\n")

    data, address = server_socket.recvfrom(buffer_size)
    print ("Recived message from client at address: ",address)
    print("message;", data.decode())

    if data:
        server_socket.sendto(str.encode(messge), address)
        print("Replied:", messge)