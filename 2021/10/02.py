with open('input.txt') as f:
    lines = [line.strip() for line in f.readlines()]

illegal_chars = {
  '(' : 1, 
  '[' : 2, 
  '{' : 3, 
  '<' : 4}

scores = []

for line in lines:
  illegal_line = False
  stack = []
  for char in line:
    if char == '(' or char == '[' or char == '{' or char == '<':
      stack.append(char)
    elif char == ')' or char == ']' or char == '}' or char == '>':
      top = stack.pop()
      if (top == '(' and not char == ')') or (top == '[' and not char == ']') or (top == '{' and not char == '}') or (top == '<' and not char == '>'):
        illegal_line = True
        break
  
  if not illegal_line:
    score = 0
    for char in reversed(stack):
      score = score * 5 + illegal_chars[char]
    scores.append(score)

scores.sort()
# print(len(scores)) #47
print(scores[23])