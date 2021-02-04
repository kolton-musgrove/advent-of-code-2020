def puzzleOne():
    print("\n Puzzle 1: \n")

    with open("day 2/input.txt") as input:
        answer = 0

        for line in input:
            # we are going to break the string appart in multiple "steps". Python's built-in split function will help out greatly here

            # the first one will be separating the policy—number of minimum and maximum appearences—from the password itself
            step1 = line.split(":")
            password = step1[1]

            # next step is to seperate the number of occurences from the letter in the policy section
            step2 = step1[0].split(" ")
            letter = step2[1]

            # last step is to get the min and max from the step2 result
            step3 = step2[0].split("-")
            min, max = step3[0], step3[1]

            # then we check if the number of occurences of the letter is bewteen the min and max inclusive, if so, add one to answer
            if password.count(letter) >= int(min) and password.count(letter) <= int(
                max
            ):
                answer += 1

        print("puzzle one: ", answer)


def puzzleTwo():
    print("\n Puzzle 2: \n")

    with open("day 2/input.txt") as input:
        answer = 0

        for line in input:
            # again, we will be using multiple "steps" to seperate the different parts of the input strings

            # separate the policy from the password
            step1 = line.split(":")
            password = step1[1].strip()

            # separate the plocy from the character
            step2 = step1[0].split(" ")
            letter = step2[1]

            # seperate the first location from the second location
            step3 = step2[0].split("-")
            # we have to remove one from the first and second locations because array indexing starts at 0, but the counting used for the policy creation starts at 1
            first = int(step3[0]) - 1
            second = int(step3[1]) - 1

            # XOR check for the positional chracters in the password
            if password[first] == letter and password[second] != letter:
                answer += 1

            if password[first] != letter and password[second] == letter:
                answer += 1

        print("puzzle two: ", answer)


puzzleOne()

puzzleTwo()