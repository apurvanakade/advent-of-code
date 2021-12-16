import math

with open('input.txt', 'r') as f:
  inputs = ["{0:08b}".format(int(line.strip(), 16)) for line in f.readlines()]

for i,input in enumerate(inputs):
  inputs[i] = "0" * ((4 - len(input)) % 4) + input

class packet:
  def __init__(self, version, ID, literal = '', subpackets = []):
    self.version = version
    self.ID = ID
    self.literal = literal
    self.subpackets = subpackets

  def __str__(self):
    string = "Version: {0}, ID: {1}, Literal: {2}, Subpackets: {3}".format(self.version, self.ID, self.literal, len(self.subpackets))

    for i,subpacket in enumerate(self.subpackets):
      string += "\nSubpacket {0}: {1}".format(i, subpacket)
    
    return string

  def sum_of_versions(self):
    return self.version + sum([subpacket.sum_of_versions() for subpacket in self.subpackets])

  def calculate(self):
    if self.ID == 0:
      function = sum
    elif self.ID == 1:
      function = math.prod 
    elif self.ID == 2:
      function = min 
    elif self.ID == 3:
      function = max
    elif self.ID == 4:
      return self.literal
    elif self.ID == 5:
      return 1 if self.subpackets[0].calculate() > self.subpackets[1].calculate() else 0
    elif self.ID == 6:
      return 1 if self.subpackets[0].calculate() < self.subpackets[1].calculate() else 0
    elif self.ID == 7:
      return 1 if self.subpackets[0].calculate() == self.subpackets[1].calculate() else 0

    return function([subpacket.calculate() for subpacket in self.subpackets])
      
def parse_string_with_meta(input, max_parsed = float('inf')):
  packets = []
  num_parsed = 0
  while True:
    if input =='' or int(input) == 0 or num_parsed >= max_parsed:
      return packets, input

    version = int(input[0:3], 2)
    ID = int(input[3:6], 2)

    if ID == 4:
      literal, input = parse_literal(input[6:])
      packets.append(packet(version, ID, int(literal, 2)))

    else:
      
      mode = input[6]

      if mode == '0':
        length_of_subpackets = int(input[7:22], 2)
        subpackets, _ = parse_string_with_meta(input[22 : 22 + length_of_subpackets])
        packets.append(packet(version, ID, literal = '', subpackets = subpackets))
        input = input[22 + length_of_subpackets:]

      elif mode == '1':
        num_of_subpackets = int(input[7:18], 2)
        subpackets, input = parse_string_with_meta(input[18:], num_of_subpackets)
        packets.append(packet(version, ID, literal='', subpackets=subpackets))

    num_parsed += 1



def parse_literal(input):

  literal = []
  
  while len(input) > 4:
    
    start_bit = input[0]
    literal = literal + [input[1:5]]
    input = input[5:]
    if start_bit == '0':
        literal = "".join(literal)
        return literal, input
  

packets, _ = parse_string_with_meta(inputs[0])

print(packets[0].calculate())