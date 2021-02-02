# Day 2: Password Philosophy

- [Problem](https://adventofcode.com/2020/day/2)
- [Code](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%202/main.py)
- [Input](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%202/input.txt)
- [Walkthrough](https://dev.to/koltonmusgrove/advent-of-code-2020-day-2-3o7m)

## Walkthrough for Problem 1

The first problem of day two focuses heavily on data parsing. The input for our puzzle consists of strings that look like the following:

- "1-3 a: abcde"
- "1-3 b: cdefg"
- "2-9 c: ccccccccc"

The integers at the beginning of each string represent the minimum and the maximum number of times the character that follows them must or can appear in the password. The password is the string of characters that follows the colon.

Our answer is the number of passwords that have a number of specific character occurrences between the minimum and maximum numbers in the policy.

Luckily, this puzzle focuses more on string parsing than it does on algorithmic efficiency. This is because puzzles in the beginning few days of the Advent of Code prepare the user with the skills to solve the more complex puzzles later on.

### Solution

```python
with open("day 2/input.txt") as input:
    answer = 0

    for line in input:
        # we are going to break the string apart in multiple "steps". Python's built-in split function will help out greatly here

        # the first one will be separating the policy—number of minimum and maximum appearances—from the password itself
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

    print(answer)
```

## Problem 2

The second puzzle is very much like the first one, but the if statement will be different. Rather than having the numbers in the policy represent the minimum and maximum occurrences of the letter in the password, they represent positions.

Our answer will be the number of passwords that have a matching character at either one of the locations in the policy but not in both locations.

### Solution

```python
with open("day 2/input.txt") as input:
    answer = 0

    for line in input:
        # again, we will be using multiple "steps" to separate the different parts of the input strings

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
```
