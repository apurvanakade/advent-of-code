import numpy as np

with open('input.txt', 'r') as f:
  polymer = f.readline().strip()
  rules = [line.strip().split(' -> ') for line in f.readlines()]

start_letter = polymer[0]
end_letter = polymer[-1]

elements = set()

for rule in rules:
  elements.add(rule[0][0])
  elements.add(rule[0][1])
  elements.add(rule[1])

pairs = [i + j for i in elements for j in elements]

rules_matrix = [[0] * len(pairs) for _ in range(len(pairs))]

for rule in rules:
  rule_input = rule[0]
  rule_output = rule[1]
  first_new_pair = rule_input[0] + rule_output
  second_new_pair = rule_output + rule_input[1]

  rules_matrix[pairs.index(rule_input)][pairs.index(first_new_pair)] += 1
  rules_matrix[pairs.index(rule_input)][pairs.index(second_new_pair)] += 1


polymer_pairs_vector = [0] * len(pairs)

for i in range(len(polymer) - 1):
  polymer_pairs_vector[pairs.index(polymer[i:i+2])] += 1

for step in range(40):
  new_polymer_pairs_vector = [0] * len(pairs)
  for i in range(len(polymer_pairs_vector)):
    for j in range(len(polymer_pairs_vector)):
      new_polymer_pairs_vector[j] += polymer_pairs_vector[i] * rules_matrix[i][j]
  polymer_pairs_vector = new_polymer_pairs_vector.copy()


occurences = {}
for element in elements:
  occurences[element] = 0

occurences[start_letter] = 1
occurences[end_letter] += 1

for pair in pairs:
  occurences[pair[0]] += polymer_pairs_vector[pairs.index(pair)]
  occurences[pair[1]] += polymer_pairs_vector[pairs.index(pair)]

max_occurence = max(occurences.values())
min_occurence = min(occurences.values())

print((max_occurence - min_occurence)/2)
