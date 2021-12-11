with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

horizontal_position = 0
depth = 0

for line in lines:
  direction = line.split()[0]
  distance = int(line.split()[1])
  if direction == "forward":
    horizontal_position += distance
  elif direction == "down":
    depth += distance
  else:  # direction == "up"
    depth -= distance

print(horizontal_position * depth)
    

