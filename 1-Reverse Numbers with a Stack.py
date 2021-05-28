string = input().split()
stack = []

for i in range(len(string)):
    stack.append(string.pop())

print(" ".join(stack))
