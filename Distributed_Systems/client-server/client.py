import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '127.0.0.1'
server_port = 10001

buffer_size = 4096

messge = 'Hi Server nice to connect ot you'

client_socket.sendto(messge.encode(), (server_address, server_port))
print('Sent to server: ', messge)

print("waiting for response form server")
data, address = client_socket.recvfrom(buffer_size)

print("message from server", data.decode())