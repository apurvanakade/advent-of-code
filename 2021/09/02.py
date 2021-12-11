import numpy as np

with open("./paded_input.txt") as f:
  paded_input = [[int(d) for d in line.strip()] for line in f.readlines()]

with open("./low_points.txt") as f:
  low_points = [[int(coords) for coords in line.strip().split(",")] for line in f.readlines()]

labels = [[0]*(len(paded_input[0])-1) for i in range(len(paded_input)-1)]
current_label = 1
label_counts = [0] * (len(low_points) + 1)

# do a BFS to find the labels starting at each low point and ending at a 9
for low_point in low_points:
  labels[low_point[0]][low_point[1]] = current_label
  label_counts[current_label] = 1
  queue = [low_point]
  while len(queue) > 0:
    current_point = queue.pop(0)
    # look at the neigbours of the current point
    neighbours = [
      [current_point[0]+1, current_point[1]], 
      [current_point[0]-1, current_point[1]], 
      [current_point[0], current_point[1]+1], 
      [current_point[0], current_point[1]-1]]
    for neighbour in neighbours:
      if labels[neighbour[0]][neighbour[1]] == 0 and paded_input[neighbour[0] + 1][neighbour[1] + 1] != 9:
        labels[neighbour[0]][neighbour[1]] = current_label
        queue.append(neighbour)
        label_counts[current_label] += 1
  current_label += 1

label_counts.sort(reverse=True)
print(label_counts[0]*label_counts[1]*label_counts[2])