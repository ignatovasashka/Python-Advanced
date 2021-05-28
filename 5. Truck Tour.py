from collections import deque

queue = deque()
n = int(input())
for _ in range(n):
    pump = input().split()
    queue.append([int(pump[0]), int(pump[1])])

for i in range(n):
    fuel_tank = 0
    pumps_travelled = 0

    for pump in queue:
        fuel, distance = pump[0], pump[1]
        fuel_tank += fuel

        if fuel_tank < distance:
            #print('breaking at', i)
            break
        fuel_tank -= distance
        pumps_travelled += 1

    if pumps_travelled == len(queue):
        print(i)
        break

    queue.rotate(-1)
