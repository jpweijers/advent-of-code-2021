inputs = open('input.txt', 'r')

# Part 1
# horizontal_pos = 0
# depth_pos = 0
# for i in inputs:
#     direction = i.split(' ')[0]
#     amount = int(i.split(' ')[1])
#     if direction == 'forward':
#         horizontal_pos += amount
#     elif direction == 'down':
#         depth_pos += amount
#     elif direction == 'up':
#         depth_pos -= amount

# print(horizontal_pos * depth_pos)

# Part 2
horizontal_pos = 0
depth_pos = 0
aim = 0
for i in inputs:
    direction = i.split(' ')[0]
    amount = int(i.split(' ')[1])
    if direction == 'forward':
        horizontal_pos += amount
        depth_pos += aim * amount
    elif direction == 'down':
        aim += amount
    elif direction == 'up':
        aim -= amount
print(horizontal_pos * depth_pos)
