with open('input.txt', 'r') as f:
  connections = [line.strip() for line in f.readlines()]

vertex_set = set()

for connection in connections:
  node1, node2 = connection.split('-')
  vertex_set.add(node1)
  vertex_set.add(node2)

vertices = list(vertex_set)
start_node = vertices.index('start')
end_node = vertices.index('end')
large_vertices = [vertex.isupper() for vertex in vertices]

is_connected = [[False] * len(vertices) for _ in range(len(vertices))]

for connection in connections:
  node1, node2 = connection.split('-')
  node1_index = vertices.index(node1)
  node2_index = vertices.index(node2)
  is_connected[node1_index][node2_index] = True
  is_connected[node2_index][node1_index] = True

def DFS(current_node, path, num_paths):

  new_paths = 0
  neighbors = [v for v in range(len(vertices)) if is_connected[current_node][v]]

  for neighbor in neighbors:
    if neighbor == end_node:
      new_paths += 1 
    elif large_vertices[neighbor] or not neighbor in path:
      path.append(neighbor) 
      new_paths += DFS(neighbor, path, num_paths)
      path.pop()

  return num_paths + new_paths

print(DFS (start_node, [start_node], 0))


# print(vertices)