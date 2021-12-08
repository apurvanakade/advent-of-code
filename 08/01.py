with open("./input_output.txt") as f:
    outputs = [line.strip().split() for line in f.readlines()]

transposed_outputs = list(zip(*outputs))

lengths_of_outputs = [[len(output) for output in row] for row in outputs]
lenghts_of_transposed_outputs = [[len(output) for output in i] for i in transposed_outputs]

count_of_1_4_7_8 = sum([lenghts_of_transposed_outputs[i].count(2) + lenghts_of_transposed_outputs[i].count(3) + lenghts_of_transposed_outputs[i].count(4) + lenghts_of_transposed_outputs[i].count(7) for i in range(4)])

print(count_of_1_4_7_8)