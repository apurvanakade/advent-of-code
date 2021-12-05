class Board:

  seen = [[False] * 5] * 5
  row_sums = [False] * 5
  col_sums = [False] * 5

  def __init__(self):
    self.entries = [[0] * 5] * 5

  def __init__(self, raw_entries):
    self.entries = [[int(j) for j in i.split()] for i in raw_entries]

  def __str__(self):
    return '\n'.join([' '.join([str(j) for j in i]) for i in self.entries])


with open("./input.txt") as f:
  draws = [int(draw) for draw in f.readlines(1)[0].strip().split(",")]

  largest_number = max(draws) #99
  smallest_number = min(draws) #0

  boards_raw = [line.strip() for line in f.readlines()]

# already_drawn = [False]*(largest_number-smallest_number+1)
# b1 = Board(boards_raw[1:5])

boards = [Board(boards_raw[i+1:i+6]) for i in range(0, len(boards_raw), 6)]

print(boards[0])
