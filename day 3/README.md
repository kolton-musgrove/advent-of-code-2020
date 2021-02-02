# Day 3: Toboggan Trajectory

- [Problem](https://adventofcode.com/2020/day/3)
- [Code](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%203/main.py)
- [Input](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%203/input.txt)
- [Walkthrough](https://dev.to/koltonmusgrove/advent-of-code-day-3-o0c)

## Walkthrough for Problem 1

Day three presents an interesting problem and a notable increase in difficulty compared to the first two days' puzzles. We are given a bunch of lines—containing hashtags and periods—that represent different positions on a mountain and a pattern—right 3, down 1—to follow. With this information, we need to determine how many hashtags we encounter if we start in the top, left corner of the text, and follow the pattern until we run out of vertical rows to use.

The first issue that we encounter is that our input has only 32 columns but it has 323 rows. If we traverse three times more rows than we do columns we will quickly run out of columns. However, the author of the puzzle specified that the rows repeat indefinitely to the right; good to know!

Also, we don't know it yet, but the answer to problem two is just a combination of the answer to problem one! To make things easier, we will write a function that can process the answer of how many hashtags we encounter based on a right-step and a down-step that we pass to the function.

### Solution for problem one and problem 2

```python
def pathSolve(right, down):
    with open("day 3/input.txt") as terrain:

        answer = 0
        # variable to hold the current position on the horizontal axis
        rightIncrement = 0
        # variable to hold the current position on the vertical axis
        downIncrment = 0

        for line in terrain:
            # we only want to check the lines that match the 'down' variable given to the function
            if downIncrement % down == 0:
                # now we have to find if the horizontal position matches the 'right' variable given to the function
                # also, since we only have 31 characters of horizontal space, we need to use the modulus operator to find our location relative to the first 31 characters
                if line[(rightIncrement * right) % 31] == "#":
                    answer += 1
                rightIncrement += 1
            downIncrement += 1
        
        return answer

# the answer to the first problem:
print("problem one: ", pathSolve(3, 1))

# the second problem asks for the product of a few different routes:
answer = (pathSolve(1, 1) * pathSolve(3, 1) * pathSolve(5, 1) * pathSolve(7, 1) * pathSolve(1, 2))

print("problem two: ", answer)

```

And just like that, we have two more stars in the bank!
