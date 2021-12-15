import heapq as hp

with open('input.txt', 'r') as f:
  input = [[int(character) for character in line.strip()] for line in f.readlines()]

width = len(input[0])
height = len(input)

def pad_input(i, j):
  return (input[i % height][j % width] - 1 + (i // height + (j // width))) % 9 + 1

paded_input = [[pad_input(i, j) for j in range(5 * width)] for i in range(5 * height)]
input = paded_input
width *= 5
height *= 5


start_vertex = (0, 0)
end_vertex = (height - 1, width - 1)

shortest_distance = {}

heap = []
unvisited = set()

for i in range(height):
  for j in range(width):
    shortest_distance[(i, j)] = float('inf')
    unvisited.add((i, j))

shortest_distance[start_vertex] = 0
hp.heappush(heap, (shortest_distance[start_vertex], start_vertex))

while len(unvisited) > 0:

  min_distance, (x, y) = hp.heappop(heap)

  unvisited.remove((x, y))

  neighbors = {(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)}

  for (i, j) in neighbors:
    if i < 0 or j < 0 or i >= len(input[0]) or j >= len(input):
      continue
    if (i, j) in unvisited:
      test_distance = shortest_distance[(x, y)] + input[i][j]
      if test_distance < shortest_distance[(i, j)]:
        shortest_distance[(i, j)] = test_distance
        hp.heappush(heap, (test_distance, (i, j)))

print(shortest_distance[end_vertex])