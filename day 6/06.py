input = open("Days 6-10/06.txt", "r")


def puzzle(input):
    ans = 0
    letters = []
    lettersSet = set()
    people = 0
    for line in input:
        line = line.strip()

        if not line:
            letters.sort()
            for let in lettersSet:
                print(let, ": ", letters.count(let))
                print(people)
                if letters.count(let) == people:
                    ans += 1

            letters = []
            lettersSet = set()
            people = 0

        else:
            for letter in line:
                letters.append(letter)
                lettersSet.add(letter)
            people += 1

    print(ans)


puzzle(input)