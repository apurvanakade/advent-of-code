input_filename = './input.txt'
output_filename = './output1.txt'

priority = 0

with open(input_filename, 'r') as f:
  while True:
    line1 = f.readline().strip()
    line2 = f.readline().strip()
    line3 = f.readline().strip()

    if not line3:
      break

    set1 = set(line1)
    set2 = set(line2)
    set3 = set(line3)

    intersection = set1.intersection(set2).intersection(set3).pop()

    if intersection.islower():
      priority += ord(intersection) - ord('a') + 1
    else:
      priority += ord(intersection) - ord('A') + 27

print(priority)