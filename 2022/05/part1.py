input_filename = './input.txt'
output_filename = './output1.txt'

overlaps = 0

with open(input_filename, 'r') as f:
  for line in f:
    range1, range2 = line.strip().split(',')
    lower1, upper1 = range1.split('-') 
    lower2, upper2 = range2.split('-') 

    if (int(lower1) <= int(lower2) and int(upper1) >= int(upper2)):
      print("type1: ", lower1, ':', upper1, 'and', lower2, ':', upper2, ":", overlaps)
      overlaps += 1
    elif (int(lower2) <= int(lower1) and int(upper2) >= int(upper1)):
      print("type2: ", lower1, ':', upper1, 'and', lower2, ':', upper2, ":", overlaps)
      overlaps += 1

print(overlaps)