with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

horizontal_position = 0
depth = 0
aim = 0

for line in lines:
  direction = line.split()[0]
  distance = int(line.split()[1])
  if direction == "forward":
    horizontal_position += distance
    depth += aim * distance
  elif direction == "down":
    aim += distance
  else: # direction == "up"
    aim -= distance

print(horizontal_position * depth)
    

