with open('input_sample.txt', 'r') as f:
  input = [line.strip() for line in f.readlines()]

permutations = []
for i in [0, 1, 2]:
  for j in [0, 1, 2]:
    for k in [0, 1, 2]:
      if i != j and j != k and k != i:
        permutations.append([i, j, k])

orientations = []
for a in [1, -1]:
  for b in [1, -1]:
    for c in [1, -1]:
      orientations.append([a, b, c])


def change_coords(S, shift, permutation = [0, 1, 2], orientation = (1, 1, 1)):
  new_S = set()
  for s in S:
    new_S.add(((s[permutation[0]] - shift[permutation[0]]) * orientation[0], (s[permutation[1]] -
              shift[permutation[1]]) * orientation[1], (s[permutation[2]] - shift[permutation[2]]) * orientation[2]))
  return new_S

scanner_data = []
current_scanner_data = []
for line in input:
  if not line == '':
    if 'scanner' in line:
      scanner_data.append(current_scanner_data)
      current_scanner_data = set()
    else:
      current_scanner_data.add((int(line.split(',')[0]), int(line.split(',')[1]), int(line.split(',')[2])))
scanner_data.append(current_scanner_data)
scanner_data = scanner_data[1:]

def try_overlap(scanner_data):
  for i in range(len(scanner_data)):
    for coords1 in scanner_data[i]:
      new_data1 = change_coords(scanner_data[i], coords1)
      for j in range(i + 1, len(scanner_data)):
        for coords2 in scanner_data[j]:
          for permutation in permutations:
            for orientation in orientations:
              new_data2 = change_coords(scanner_data[j], coords2, permutation, orientation)
              intersection = new_data1.intersection(new_data2)
              if len(intersection) > 11:
                return i, j, new_data1.union(new_data2)
  return None, None


while len(scanner_data) > 1:
  i, j, union = try_overlap(scanner_data)
  scanner_data.remove(scanner_data[j])
  scanner_data.remove(scanner_data[i])
  scanner_data.insert(0, union)
  print(len(scanner_data), len(scanner_data[0]))
  
print(len(scanner_data[0]))

with open('output_sample.txt', 'w') as f:
  for (x, y, z) in scanner_data[0]:
    f.write(str(x) + ',' + str(y) + ',' + str(z) + '\n')

pairwise_distances = []

for coords1 in scanner_data[0]:
  for coords2 in scanner_data[0]:
    pairwise_distances.append(abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1]) + abs(coords1[2] - coords2[2]))

print(max(pairwise_distances))