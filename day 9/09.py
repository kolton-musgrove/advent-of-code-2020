input = open("09.txt", "r")


def puzzle1(input):
    previous_numbers = set()

    for line in input:
        line = line.strip()
        previous_numbers.add(int(line))

    print(previous_numbers)


puzzle1(input)