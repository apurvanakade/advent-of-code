with open("./input.txt") as f:
    lines = [int(line.strip()) for line in f.readlines()]

increasing_window_count = 0
for i in range(len(lines)-3):
  increasing_window_count += 1 if lines[i] < lines[i+3] else 0

print(increasing_window_count)