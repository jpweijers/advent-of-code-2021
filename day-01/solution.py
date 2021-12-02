inputs = open('input.txt', 'r')
increased_count = 0
last = None
current = None
for i in inputs:
    current = int(i)
    if last and current > last:
        increased_count += 1
    last = current
print(increased_count)
