# Like day 4, most of the logic for this problem is handled in helper functions.


def puzzle1():
    print("\n Puzzle 1: \n")

    ids = makeIds()
    print(max(ids))  # The answer for the first puzzle is the largest seat number


def puzzle2():
    print("\n Puzzle 2: \n")

    ids = makeIds()

    for i in range(min(ids), max(ids)):
        if i not in ids:
            print(i)  # Print first # not in the of numbers from min to max seat id
            break


def makeIds():
    with open("day 5/input.txt", "r") as input:
        ids = set()

        for line in input:
            line = line.strip()

            rows, cols = (
                line[:7],
                line[7:],
            )  # Separate the F's and B's from the R's and L's
            row, col = getRow(rows), getCol(cols)

            id = (row * 8) + col

            ids.add(id)

        return ids


def getRow(frontback):  # Binary algorithm to find the row number from string
    total = [0, 127]

    for char in frontback:
        if char == "F":
            total = removeHalf(total, "lower")
        else:
            total = removeHalf(total, "upper")

    return round((total[0] + total[1]) / 2)


def getCol(rightleft):  # Binary algorithm to find the col number from string
    total = [0, 7]

    for char in rightleft:
        if char == "L":
            total = removeHalf(total, "lower")
        else:
            total = removeHalf(total, "upper")

    return round((total[0] + total[1]) / 2)


def removeHalf(nums, lower):
    total = nums[1] - nums[0]
    if lower == "lower":
        nums[1] = nums[1] - (total / 2)
    elif lower == "upper":
        nums[0] = nums[0] + (total / 2)

    return nums


puzzle1()
puzzle2()