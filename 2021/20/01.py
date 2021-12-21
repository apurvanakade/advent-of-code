import numpy as np

with open('input.txt', 'r') as f:
  mask = [1 if char == '#' else 0 for char in f.readline().strip()]
  f.readline()
  image = [[1 if char == '#' else 0 for char in line.strip()] for line in f.readlines()]

image = np.array(image)

for _ in range(25):
  image = np.pad(image, 2, mode='constant', constant_values=0)
  enhanced_image = np.zeros(image.shape)

  for i in range(1, len(image) - 1):
    for j in range(1, len(image[i]) - 1):
      surround_seq = np.append(image[i-1][j-1:j+2], np.append(image[i][j-1:j+2], image[i+1][j-1:j+2]))
      bit = int(surround_seq.dot(2**np.arange(surround_seq.size)[::-1]))
      enhanced_image[i][j] = mask[bit]
  image = enhanced_image
  image = image[1: -1, 1:-1]

  ##############################################################

  image = np.pad(image, 2, mode='constant', constant_values=1)
  enhanced_image = np.zeros(image.shape)

  for i in range(1, len(image) - 1):
    for j in range(1, len(image[i]) - 1):
      surround_seq = np.append(
          image[i-1][j-1:j+2], np.append(image[i][j-1:j+2], image[i+1][j-1:j+2]))
      bit = int(surround_seq.dot(2**np.arange(surround_seq.size)[::-1]))
      enhanced_image[i][j] = mask[bit]
  image = enhanced_image
  image = image[1: -1, 1:-1]

with open('output.txt', 'w') as f:
  for row in image:
    f.write(''.join(['#' if bit else '.' for bit in row]) + '\n')

print(np.sum(image))
