with open('input_sample.txt', 'r') as f:
  input = [[int(character) for character in line.strip()] for line in f.readlines()]

vertices = [(i,j) for i in range(len(input)) for j in range(len(input[0]))]
start_vertex = vertices[0]
end_vertex = vertices[-1]

shortest_distance = {}

for vertex in vertices:
  shortest_distance[vertex] = float('inf')

shortest_distance[start_vertex] = 0

unvisited = set(vertices)

while len(unvisited) > 0:

  x, y = min(unvisited, key=lambda vertex: shortest_distance[vertex])

  unvisited.remove((x, y))

  neighbors = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}
  for (i, j) in neighbors:
    if i < 0 or j < 0 or i >= len(input[0]) or j >= len(input):
      continue
    if (i, j) in unvisited:
      shortest_distance[(i, j)] = min(shortest_distance[(i,j)], shortest_distance[(x, y)] + input[i][j])

print(shortest_distance[end_vertex])
