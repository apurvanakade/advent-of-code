input_filename = './input.txt'
output_filename = './output2.txt'

calories = 0
max_calories = [0, 0, 0]

# read input.txt one line at a time
with open(input_filename, 'r') as f:
  for line in f:
    # parse the line
    line = line.strip()
    
    if line == '':
      # append calories to max_calories
      max_calories.append(calories)
      # sort max_calories
      max_calories.sort()
      # remove the smallest element
      max_calories.pop(0)

      calories = 0
    
    else:
      calories += int(line)
  
  # append calories to max_calories
  max_calories.append(calories)
  # sort max_calories
  max_calories.sort()
  # remove the smallest element
  max_calories.pop(0)

  calories = 0
  

# output max_calories and argmax_calories to ./output.txt
with open(output_filename, 'w') as f:
  f.write('max_calories: ' + str(max_calories) + '\n' + 
  'total_max_calories: ' + str(sum(max_calories)))




