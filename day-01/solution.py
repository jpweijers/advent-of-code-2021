inputs = open('input.txt', 'r')
increased_count = 0
last = None
current = None

# for i in inputs:
#     current = int(i)
#     if last and current > last:
#         increased_count += 1
#     last = current
# print(increased_count)

measurements = []
for i in inputs:
    measurements.append(int(i))

for i in range(len(measurements)-2):
    current = sum(measurements[i:i+3])
    if last and current > last:
        increased_count += 1
    last = current
print(increased_count)
