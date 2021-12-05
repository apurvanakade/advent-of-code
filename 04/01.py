with open("./input.txt") as f:
  draws = [int(draw) for draw in f.readlines(1)[0].strip().split(",")]
  
  largest_number = max(draws) #99
  smallest_number = min(draws) #0

  board_numbers = [line.strip() for line in f.readlines()]

already_drawn = [False]*(largest_number-smallest_number+1)

print(largest_number, smallest_number, (already_drawn))
