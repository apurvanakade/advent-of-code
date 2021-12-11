with open("./input_input.txt") as f:
    inputs = [line.strip().split() for line in f.readlines()]

with open("./input_output.txt") as f:
    outputs = [line.strip().split() for line in f.readlines()]


sum_of_outputs = 0

# process each row one at a time
for i in range(len(inputs)):

  input = [set(j) for j in inputs[i]]

  wires = [{}] * 10

  # first find the wires for each number
  input_lengths = [len(i) for i in input]

  wires[1] = input[input_lengths.index(2)]
  wires[4] = input[input_lengths.index(4)]
  wires[7] = input[input_lengths.index(3)]
  wires[8] = input[input_lengths.index(7)]

  for inp in input:
    if len(inp) == 5 and wires[7].issubset(inp):
      wires[3] = inp
    elif len(inp) == 6: 
      if wires[4].issubset(inp):
        wires[9] = inp 
      elif not wires[1].issubset(inp):
        wires[6] = inp
      else:
        wires[0] = inp

  for j in range(10):
    inp = input[j]
    if len(inp) == 5:
      if inp.issubset(wires[6]):
        wires[5] = inp
      elif not wires[1].issubset(inp):
        wires[2] = inp

  # now we have the wires, we can calculate the output
  output = [set(out) for out in outputs[i]]
  sum_of_outputs += 1000 * wires.index(output[0]) + 100 * wires.index(output[1]) + 10 * wires.index(output[2]) + wires.index(output[3])

print(sum_of_outputs)

  