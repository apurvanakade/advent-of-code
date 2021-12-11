class Board:

  def __init__(self, raw_entries):
    self.entries = [[int(j) for j in i.split()] for i in raw_entries]
    self.seen = [[False, False, False, False, False], [False, False, False, False, False], [
        False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
    self.row_sums = [False] * 5
    self.col_sums = [False] * 5
    self.bingo = False
    self.final_draw = -1
    self.final_turn = -1

  def __str__(self):
    return '\n'.join([' '.join([str(j) for j in i]) for i in self.entries])

  def update(self, draw, i):
    
    if self.bingo:
      return self.bingo

    self.final_draw = draw
    self.final_turn = i

    for i in range(5):
      for j in range(5):
        if self.entries[i][j] == draw:
          self.seen[i][j] = True
          self.row_sums[i] = all(self.seen[i])
          self.col_sums[j] = self.seen[0][j] and self.seen[1][j] and self.seen[2][j] and self.seen[3][j] and self.seen[4][j]
          self.bingo = self.bingo or self.row_sums[i] or self.col_sums[j]
    return self.bingo

  def final_score(self):
    sum = 0
    for i in range(5):
      for j in range(5):
        if not self.seen[i][j]:
          sum += self.entries[i][j]
    return sum * self.final_draw

with open("./input.txt") as f:
  draws = [int(draw) for draw in f.readlines(1)[0].strip().split(",")]

  largest_number = max(draws) #99
  smallest_number = min(draws) #0

  boards_raw = [line.strip() for line in f.readlines()]

already_drawn = [False]*(largest_number-smallest_number+1)

boards = [Board(boards_raw[i+1:i+6]) for i in range(0, len(boards_raw), 6)]

for i in range(len(draws)):
  draw = draws[i] 
  if not already_drawn[draw]:
    already_drawn[draw] = True
    for board in boards:
      board.update(draw, i)
    
# for board in boards:
#   if(board.bingo):
#     print(board.final_score(), board.final_draw, board.final_turn)

final_scores = [(board.final_score(), board.final_turn) for board in boards if board.bingo]

print(max(final_scores, key=lambda x:x[1]))