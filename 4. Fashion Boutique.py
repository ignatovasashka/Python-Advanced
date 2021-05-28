box = []

for clothing in input().split():
    box.append(int(clothing))

rack_capacity = int(input())

number_of_racks = 1
current_sum_value = 0
for i in range(len(box)):
    current_clothing_value = box.pop()
    if current_clothing_value + current_sum_value > rack_capacity:
        number_of_racks += 1
        current_sum_value = 0
    current_sum_value += current_clothing_value

print(number_of_racks)