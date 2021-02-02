input = open("Days 1-5/05.txt", "r")


def puzzle1(input):
    ids = []

    for line in input:
        line = line.strip()

        frontback = line[:7]
        rightleft = line[7:]

        row = getRow(frontback)
        column = getColumn(rightleft)

        id = (row * 8) + column

        ids.append(id)

    ids.sort()
    print(ids)


def puzzle2(input):
    ids = []

    for line in input:
        line = line.strip()

        frontback = line[:7]
        rightleft = line[7:]

        row = getRow(frontback)
        column = getColumn(rightleft)

        id = (row * 8) + column

        ids.append(id)

    ids.sort()
    print(ids)

    for i in range(1, len(ids) - 1):
        if ids[i+1] != ids[i] + 1:
            print(ids[i])


def getRow(frontback):
    total = [0, 127]

    for char in frontback:
        if char == "F":
            total = removeHalf(total, "lower")
        else:
            total = removeHalf(total, "upper")

    return round((total[0] + total[1]) / 2)


def getColumn(rightleft):
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
    else:
        nums[0] = nums[0] + (total / 2)

    return nums


puzzle2(input)