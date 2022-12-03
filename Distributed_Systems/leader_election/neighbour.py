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