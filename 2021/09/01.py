import numpy as np

with open("./input.txt") as f:
  raw_input = [[int(d) for d in line.strip()] for line in f.readlines()]

input = np.array(raw_input)

paded_input = np.pad(input, 1, 'constant', constant_values=9)

low_points = []
total_risk = 0

for i in range(1, len(paded_input) - 1):
  for j in range(1, len(paded_input[0]) - 1):
    if paded_input[i][j] < paded_input[i - 1][j] and paded_input[i][j] < paded_input[i + 1][j] and paded_input[i][j] < paded_input[i][j - 1] and paded_input[i][j] < paded_input[i][j + 1]:
      low_points.append((i - 1, j - 1))
      total_risk += paded_input[i][j] + 1

with open("./low_points.txt", "w") as f:
  for p in low_points:
    f.write(f"{p[0]},{p[1]}\n")

with open("./paded_input.txt", "w") as f:
  for p in paded_input:
    f.write("".join(str(d) for d in p) + "\n")