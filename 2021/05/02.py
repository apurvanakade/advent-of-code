import numpy as np

with open("./input.txt") as f:
  raw_input = [line.strip().split(" -> ") for line in f.readlines()]

start_coordinates = [(0,0)] * len(raw_input)
end_coordinates = [(0, 0)] * len(raw_input)
directions = ['d'] * len(raw_input)

grid = np.zeros((1000, 1000))
count = 0
for i in range(len(raw_input)):
  start_coordinates[i] = (int(raw_input[i][0].split(",")[0]), int(raw_input[i][0].split(",")[1]))
  end_coordinates[i] = (int(raw_input[i][1].split(",")[0]), int(raw_input[i][1].split(",")[1]))
  if (start_coordinates[i][0] == end_coordinates[i][0]):
    directions[i] = 'h'
    for j in range(min(start_coordinates[i][1], end_coordinates[i][1]), max(start_coordinates[i][1], end_coordinates[i][1]) + 1):
      grid[start_coordinates[i][0], j] += 1
  elif (start_coordinates[i][1] == end_coordinates[i][1]):
    directions[i] = 'v'
    for j in range(min(start_coordinates[i][0], end_coordinates[i][0]), max(start_coordinates[i][0], end_coordinates[i][0]) + 1):
      grid[j, start_coordinates[i][1]] += 1
  else:
    if (start_coordinates[i][0] < end_coordinates[i][0]) and (start_coordinates[i][1] < end_coordinates[i][1]):
      # print("right up")
      for j in range(start_coordinates[i][0], end_coordinates[i][0] + 1):
          grid[j, start_coordinates[i][1] + (j - start_coordinates[i][0])] += 1
    elif (start_coordinates[i][0] > end_coordinates[i][0]) and (start_coordinates[i][1] < end_coordinates[i][1]):
      # print("left up")
      for j in range(end_coordinates[i][0], start_coordinates[i][0] + 1):
          grid[j, start_coordinates[i][1] - (j - start_coordinates[i][0])] += 1
    elif (start_coordinates[i][0] < end_coordinates[i][0]) and (start_coordinates[i][1] > end_coordinates[i][1]):
      # print("right down")
      for j in range(start_coordinates[i][0], end_coordinates[i][0] + 1):
          grid[j, start_coordinates[i][1] - (j - start_coordinates[i][0])] += 1
    elif (start_coordinates[i][0] > end_coordinates[i][0]) and (start_coordinates[i][1] > end_coordinates[i][1]):
      # print("left down")
      for j in range(end_coordinates[i][0], start_coordinates[i][0] + 1):
          grid[j, start_coordinates[i][1] + (j - start_coordinates[i][0])] += 1

count = 0
for i in range(1000):
  for j in range(1000):
    if (grid[i, j] > 1):
      count += 1

print(count)