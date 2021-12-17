import math

with open('input.txt', 'r') as f:
  left_end = int(f.readline().strip())
  right_end = int(f.readline().strip())
  top_end = int(f.readline().strip())
  bottom_end = int(f.readline().strip())


maximum_height = 0
num_possible_velocities = 0

for v_x in range(right_end + 1):
  for v_y in range(2*bottom_end, -2*bottom_end):    
    if (v_y + 1/2)**2 - 4*top_end < 0 or (v_y + 1/2)**2 - 4*top_end < 0:
      continue
    max_t = math.floor((v_y + 1/2) + math.sqrt((v_y + 1/2)**2 - 2*top_end))
    min_t = math.ceil((v_y + 1/2) + math.sqrt((v_y + 1/2)**2 - 2*bottom_end))
    for time in range(min_t, max_t + 1):
      t = min(time, v_x)
      x_at_time = t * v_x - t * (t - 1) / 2
      if x_at_time >= left_end and x_at_time <= right_end:
        maximum_height = max(maximum_height, 0, (v_y * (v_y + 1))/2)
        num_possible_velocities += 1
        break

print('num_possible_velocities = ', num_possible_velocities, 'maximum_height = ', maximum_height)