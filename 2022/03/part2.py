input_filename = './input.txt'
output_filename = './output1.txt'

plays = {
  'A' : 0,
  'B' : 1,
  'C' : 2,
  'X' : -1,
  'Y' : 0,
  'Z' : 1
}

score = 0

# read input.txt one line at a time
with open(input_filename, 'r') as f:
  for line in f:
    first, second = line.split()
    play1 = plays[first]
    strategy = plays[second]

    play2 = ((play1 + strategy) % 3)

    score += (play2 + 1) + (1 + plays[second]) * 3

print( score)





