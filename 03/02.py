with open("./input.txt") as f:
    lines = [line.strip() for line in f.readlines()]


num_of_bits = len(lines[0]) #12

most_common_ith_bit = 0
filtered_lines = lines
oxygen_generator_rating = 0
for i in range(num_of_bits):
  if len(filtered_lines) == 1:
    break
  most_common_ith_bit = 0 if sum([int(digit[i]) for digit in filtered_lines]) < len(filtered_lines)/2 else 1
  filtered_lines = [line for line in filtered_lines if int(line[i]) == most_common_ith_bit]

oxygen_generator_rating = int(filtered_lines[0], 2)

least_common_ith_bit = 0
filtered_lines = lines
co2_scrubber_rating = 0
for i in range(num_of_bits):
  print(len(filtered_lines))
  if len(filtered_lines) == 1:
    break
  least_common_ith_bit = 1 if sum([int(digit[i]) for digit in filtered_lines]) < len(filtered_lines)/2 else 0
  filtered_lines = [line for line in filtered_lines if int(line[i]) == least_common_ith_bit]

co2_scrubber_rating = int(filtered_lines[0], 2)

print(oxygen_generator_rating * co2_scrubber_rating)
