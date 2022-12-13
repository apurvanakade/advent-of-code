input_filename = './input.txt'
output_filename = './output1.txt'

priority = 0

with open(input_filename, 'r') as f:
  for line in f:

    length = len(line)

    first_half = line[0:length//2]
    second_half = line[length//2:length]

    first_set = set(first_half)
    second_set = set(second_half)
    
    intersection = first_set.intersection(second_set).pop()

    if intersection.islower():
      priority += ord(intersection) - ord('a') + 1
    else:
      priority += ord(intersection) - ord('A') + 27

print(priority)

