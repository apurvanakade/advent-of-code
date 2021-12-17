with open('input.txt', 'r') as f:
  target_x_left_end = int(f.readline().strip())
  target_x_right_end = int(f.readline().strip())
  target_y_top_end = int(f.readline().strip())
  target_y_bottom_end = int(f.readline().strip())


maximum_height = 0
possible_velocities = set()

for v_x in range(target_x_right_end + 1):
  for v_y in range(2*target_y_bottom_end, -2*target_y_bottom_end):
    for time in range(1, 300):
      y_at_time = (time) * v_y - time * (time - 1) /2
      t = min(time, v_x)
      x_at_time = (t) * v_x - t * (t - 1) / 2

      if x_at_time >= target_x_left_end and x_at_time <= target_x_right_end and y_at_time >= target_y_top_end and y_at_time <= target_y_bottom_end:
        possible_velocities.add((v_x, v_y))
        maximum_height = max(maximum_height, 0, (v_y * (v_y + 1))/2)

print('possible_velocities = ', len(possible_velocities), 'maximum_height = ', maximum_height)