import socket

def form_ring(members):
    sorted_binary_ring = sorted([socket.inet_aton(member) for member in members])
    sorted_ip_ring= [socket.inet_ntoa(node) for node in sorted_binary_ring]
    return sorted_ip_ring

members = ['192.168.0.1', '192.168.0.3', '192.168.0.41', '192.168.0.56', '192.168.0.5']
ring = form_ring(members=members)
print(ring)

def get_neighbour(ring, current_node_ip, direction='left'):
    current_node_index = ring.index(current_node_ip) if current_node_ip in ring else -1
    if current_node_index != -1:
        if direction == 'left':
            if current_node_index + 1 == len(ring):
                return ring[0]
            else:
                return ring[current_node_index + 1]
        else:
            if current_node_index == 0:
                return ring[len(ring)-1]
            else:
                return ring[current_node_index -1]
    else:
        return None

ring = ['192.168.0.1', '192.168.0.3', '192.168.0.41', '192.168.0.56', '192.168.0.5']
neighbour = get_neighbour(ring, '192.168.0.41', 'right')
print(neighbour)


# LaLann Chang Roberts
election_message = {
    "mid" : '',
    "isLeader" : False
}

print("\nWaiting to receive election message...\n")

data, address = ring_socket.recvfrom(buffer_size)

if election_message['isLeader']:
    leader_uid = election_message['mid']

    participant = False
    ring_socket.sendto(json.dumps(election_message), neighbour)

if election_message['mid'] < my_uid and not participant:
    new_election_message = {
        "mid" : my_uid,
        "isLeader" : False
    }

    participant = True

    ring_socket.sendto(json.dumps(election_message), neighbour)

elif election_message['mid'] > my_uid:
    participant = True
    ring_socket.sendto(json.dumps(election_message), neighbour)
elif election_message['mid'] == my_uid:
    leader_uid = my_uid
    new_election_message = {
        "mid" : my_uid,
        "isLeader" : True
    }

    participant = False