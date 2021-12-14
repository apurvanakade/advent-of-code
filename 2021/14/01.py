with open('input.txt', 'r') as f:
  polymer = f.readline().strip()
  rules = [line.strip().split(' -> ') for line in f.readlines()]

for step in range(10):
  new_polymer = polymer[0]
  for i in range(len(polymer) - 1):
    for rule in rules:
      if rule[0] == polymer[i:i+2]:
        new_polymer = new_polymer + rule[1]
    new_polymer = new_polymer + polymer[i+1]
  polymer = new_polymer

elements = set(polymer)
num_of_occurences = [polymer.count(element) for element in elements]

print(max(num_of_occurences) - min(num_of_occurences))

# print(polymer)
print(elements)

