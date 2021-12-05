with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

num_of_bits = len(lines[0]) #12
num_of_lines = len(lines) #1000

gamma = 0

for i in range(num_of_bits):
  if sum([int(digit[i]) for digit in lines]) < num_of_lines/2:
    gamma += 0  
  else: 
    gamma += 2**(num_of_bits - i - 1)
  
eplison = 2**num_of_bits - 1 - gamma

print(gamma * eplison)