expr = input()
balanced = True
stack = []

for symbol in expr:
    if symbol in '[{(':
        stack.append(symbol)
    elif symbol in ']})':
        if len(stack) == 0:
            balanced = False
            break

        opening_symbol = stack.pop()

        if symbol == ']' and opening_symbol == '[':
            continue
        elif symbol == '}' and opening_symbol == '{':
            continue
        elif symbol == ')' and opening_symbol == '(':
            continue
        else:
            balanced = False
            break

if balanced and len(stack) == 0:
    print('YES')
else:
    print('NO')

# shorter:
# if f'{opening_symbol}{symbol}' not in ['[]', '{}', '()']:
#   balanced = False
