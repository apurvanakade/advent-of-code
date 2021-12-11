with open("./input.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

increasing_count = 0
for i in range(len(lines)-1):
  increasing_count += 1 if lines[i] < lines[i+1] else 0

print(increasing_count)