coords = set()
instructions = []

with open('./input.txt', 'r') as f:
  line = f.readline().strip()
  while line:
    try:
      x, y = line.split(',')
      coords.add((int(x), int(y)))
    except:
      _, _, instruction = line.split(' ')
      instructions.append((instruction.split('=')[0], int(instruction.split('=')[1])))
    line = f.readline().strip()

new_coords = set()

for axis, length in instructions:
  max_x = 0
  max_y = 0
  
  if axis == 'x':
    for x, y in coords: 
      max_y = max(max_y, y)
      if x < length:
        new_coords.add((x, y))
        max_x = max(max_x, x)
      else:
        new_coords.add((2 * length - x, y))
        max_x = max(max_x, 2 * length - x)
  elif axis == 'y':
    for x, y in coords: 
      max_x = max(max_x, x)
      if y < length:
        new_coords.add((x, y))
        max_y = max(max_y, y)
      else:
        new_coords.add((x, 2 * length - y))
        max_y = max(max_y, 2 * length - y)
  
  coords = new_coords.copy()
  new_coords = set()

grid = [['.' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

for x, y in coords:
  grid[y][x] = '█'

for row in grid:
  print(''.join(row))