input_filename = './input.txt'
output_filename = './output1.txt'

calories = 0
max_calories = 0

# read input.txt one line at a time
with open(input_filename, 'r') as f:
  for line in f:
    # parse the line
    line = line.strip()
    
    if line == '':
      if calories > max_calories:
        max_calories = calories

      calories = 0
    
    else:
      calories += int(line)
  

# output max_calories and argmax_calories to ./output.txt
with open(output_filename, 'w') as f:
  f.write('max_calories: ' + str(max_calories))




