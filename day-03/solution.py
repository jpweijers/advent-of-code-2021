def get_input():
    return open('input.txt', 'r')


def part_1():
    puzzle_input = get_input()
    gamma_rate = [''] * 12
    epsilon_rate = [''] * 12
    zero_count = [0] * 12
    one_count = [0] * 12
    for line in puzzle_input:
        bits = [bit for bit in line if bit != '\n']
        for index, bit in enumerate(bits):
            if bit == '0':
                zero_count[index] += 1
            elif bit == '1':
                one_count[index] += 1

    for i in range(12):
        if zero_count[i] > one_count[i]:
            gamma_rate[i] = '0'
            epsilon_rate[i] = '1'
        elif zero_count[i] < one_count[i]:
            gamma_rate[i] = '1'
            epsilon_rate[i] = '0'

    gamma_rate = ''.join(gamma_rate)
    epsilon_rate = ''.join(epsilon_rate)
    power_rate = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(power_rate)


def part_2():
    puzzle_input = get_input()
    input_array = [line for line in puzzle_input]

    for i in range(12):
        if len(input_array) == 1:
            break
        one_count = 0
        zero_count = 0

        for j in input_array:
            bits = [bit for bit in j if bit != '\n']
            if bits[i] == '1':
                one_count += 1
            else:
                zero_count += 1

            # print(one_count, zero_count)
        if one_count >= zero_count:
            input_array = [line for line in input_array if line[i] == '1']
        elif one_count < zero_count:
            input_array = [line for line in input_array if line[i] == '0']

        print(i, input_array)

    oxygen_rating = int(input_array[0], 2)
    print(oxygen_rating)

    puzzle_input = get_input()
    input_array = [line for line in puzzle_input]

    for i in range(12):
        if len(input_array) == 1:
            break
        one_count = 0
        zero_count = 0

        for j in input_array:
            bits = [bit for bit in j if bit != '\n']

            if bits[i] == '1':
                one_count += 1
            else:
                zero_count += 1

        if one_count >= zero_count:
            input_array = [line for line in input_array if line[i] == '0']
        elif one_count < zero_count:
            input_array = [line for line in input_array if line[i] == '1']
        print(i, input_array)

    scrubber_rating = int(input_array[0], 2)
    print(f'{oxygen_rating} * {scrubber_rating} = {scrubber_rating * oxygen_rating}')


part_1()
part_2()
