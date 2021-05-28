from collections import deque

total = int(input())
queue = deque()
orders = input().split()
orders_complete = []

for order in orders:
    queue.append(int(order))

max_order = max(queue)
print(max_order)

for i in range(len(queue)):
    current_order = queue[0]
    if current_order <= total:
        orders_complete.append(queue.popleft())
        total = total - current_order
        if len(orders_complete) == len(orders):
            print("Orders complete")
    else:
        print("Orders left:", ' '.join([str(i) for i in queue]))
        break

