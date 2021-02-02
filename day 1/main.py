# only time efficient solutions and their dependencies are in this file


def PuzzleOne():
    print("\n Puzzle 1: \n")

    with open("day 1/input.txt") as input:
        inSet = set()

        # I start with a set, append all of the values, and then convert to a list because of the time complexity for each additional item that will be saved if there are not duplcicates in the list. This is not a space optimal operation.
        for num in input:
            inSet.add(int(num))

        inList = list(inSet)

        for i in range(len(inList)):
            # calculate the value we would need to sum with inList[i] to get 202
            target = 2020 - inList[i]

            # check if that item is in the inList
            answer = BinarySearch(inList, target)

            if answer is not None:
                print("Values: ", inList[i], answer)
                print("Answer: ", inList[i] * answer)


def PuzzleTwo():
    print("\n Puzzle 2: \n")

    with open("day 1/input.txt") as input:
        inSet = set()

        # again we use a set to list converstion to get rid of duplicates
        for num in input:
            inSet.add(int(num))

        inList = list(inSet)

        # this is not an elegent solution to the problem, but it works, and with decent time complexity
        for i in inList:
            for j in inList:
                target = 2020 - i - j

                # k will be the index of the third number that—along with i and j—sums to 2020
                k = BinarySearch(inList, target)

                if k is not None:
                    print("Values: ", i, j, k)
                    print("answer: ", i * j * k)
                    exit()


def BinarySearch(lst, target):
    # set the low and high indecies
    low = 0
    high = len(lst) - 1

    # itterativly search the list
    while low <= high:
        # find the mid point by floor dividing the sum of the high and low
        mid = (low + high) // 2

        # return the index of the number if it is found, or set the high and low to recude the search space
        if lst[mid] == target:
            return lst[mid]
        elif lst[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


PuzzleOne()

PuzzleTwo()