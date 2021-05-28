n = int(input())
stack = []

for i in range(n):
    command = input().split()
    if command[0] == "1": # push element to the stack
        stack.append(int(command[1]))
    elif command[0] == "2": # delete
        if len(stack) > 0:
            stack.pop()
    elif command[0] == "3": # max element
        if len(stack) > 0:
            print(max(stack))
    elif command[0] == "4": # min element
        if len(stack) > 0:
            print(min(stack))

reversed_nums = []

for i in range(len(stack)):
    reversed_nums.append(str(stack.pop()))

print(', '.join(reversed_nums))