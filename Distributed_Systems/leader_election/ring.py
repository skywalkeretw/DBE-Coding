import socket

def form_ring(members):
    sorted_binary_ring = sorted([socket.inet_aton(member) for member in members])
    sorted_ip_ring= [socket.inet_ntoa(node) for node in sorted_binary_ring]
    return sorted_ip_ring

members = ['192.168.0.1', '192.168.0.3', '192.168.0.41', '192.168.0.56', '192.168.0.5']
ring = form_ring(members=members)
print(ring)