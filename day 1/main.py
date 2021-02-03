# only time efficient solutions and their dependencies are in this file

def PuzzleOne():
    print("\n Puzzle 1: \n")

    with open("day 1/input.txt") as input:
        # I start with a set, append all of the values, and then convert to a list because of the time complexity for each additional item that will be saved if there are not duplcicates in the list. This is not a space optimal operation.
        numSet = {int(num) for num in input}
        
        # Itterate over all items in numSet, subtracting one number from 2020 per loop, and check if the different is in the numSet
        for i in numSet:
            target = 2020 - i

            if target in numSet:
                print("Values: ", i, target)
                print("Answer: ", i * target)
                break
                


def PuzzleTwo():
    print("\n Puzzle 2: \n")

    with open("day 1/input.txt") as input:
        # again we use a list to set converstion to get rid of duplicates
        numSet = {int(num) for num in input}

        # I know, I know, nested for-loops are bad. You're right.
        for i in numSet:
            for j in numSet:
                target = 2020 - i - j

                if target in numSet:
                    print("Values: ", i, j, target)
                    print("answer: ", i * j * target)
                    exit()


PuzzleOne()

PuzzleTwo()