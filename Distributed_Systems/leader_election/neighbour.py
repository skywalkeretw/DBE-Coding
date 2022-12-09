# def get_neighbour(ring, current_node_ip, direction='left'):
#     current_node_index = ring.index(current_node_ip) if current_node_ip in ring else -1
#     if current_node_index != -1:
#         if direction == 'left':
#             if current_node_index + 1 == len(ring):
#                 return ring[0]
#             else:
#                 return ring[current_node_index + 1]
#         else:
#             if current_node_index == 0:
#                 return ring[len(ring)-1]
#             else:
#                 return ring[current_node_index -1]
#     else:
#         return None

# ring = ['192.168.0.1', '192.168.0.3', '192.168.0.41', '192.168.0.56', '192.168.0.5']
# neighbour = get_neighbour(ring, '192.168.0.41', 'right')
# print(neighbour)

participants = [{'id': '945c222f-5d8b-4ad8-b71e-ce6a0f6b455a', 'ip': '192.168.178.30'}, {'id': '14ede406-ccde-48f4-b05d-62cae9fd0bda', 'ip': '192.168.178.70'}]


tom_index = next((index for (index, d) in enumerate(participants) if d["id"] == "14ede406-ccde-48f4-b05d-62cae9fd0bda"), -1)
print(tom_index)

