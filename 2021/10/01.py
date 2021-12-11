with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

illegal_chars = {
  ')' : 3, 
  ']' : 57, 
  '}' : 1197, 
  '>' : 25137}

score = 0

for line in lines:
  stack = []
  for char in line:
    if char == '(' or char == '[' or char == '{' or char == '<':
      stack.append(char)
    elif char == ')' or char == ']' or char == '}' or char == '>':
      top = stack.pop()
      if (top == '(' and not char == ')') or (top == '[' and not char == ']') or (top == '{' and not char == '}') or (top == '<' and not char == '>'):
        score += illegal_chars[char]
        break

print(score)