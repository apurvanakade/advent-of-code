input_filename = './input.txt'
output_filename = './output1.txt'

plays = {
  'A' : 1,
  'B' : 2,
  'C' : 3,
  'X' : 1,
  'Y' : 2,
  'Z' : 3
}

win_scores = [
  [3, 0, 6],
  [6, 3, 0],
  [0, 6, 3]
]

score = 0

# read input.txt one line at a time
with open(input_filename, 'r') as f:
  for line in f:
    first, second = line.split()
    play1 = plays[first]
    play2 = plays[second]

    score += play2 + win_scores[play2 - 1][play1 - 1]

print(score)





