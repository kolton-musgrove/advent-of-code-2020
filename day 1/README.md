# Day 1: Report Repair

- [Problem](https://adventofcode.com/2020/day/1)
- [Code](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%201/main.py)
- [Input](https://github.com/kolton-musgrove/AdventOfCode/blob/main/day%201/input.txt)
- [Walkthrough](https://dev.to/koltonmusgrove/advent-of-code-2020-day-1-problem-1-9n9)

## Walkthrough for Problem 1

For this problem, we are given a list of numbers—one per line—and asked to find two entries that sum to the number 2020. Once we have the two numbers, we multiply them together to get our answer.

### Naive Approach

The naive approach to solving the classic sum-two problem is using a nested search to test every combination of numbers that add to the desired amount (2020).

```python
# load data
with open("day 1/input.txt", "r") as input:
    # create an empty set to hold the data
    inSet = set()

    # add each item from the input list to the inSet
    for num in input:
        inSet.add(int(num))

    # for every num in inSet, check if any value in inSet sums with that number to equal 2020. If a pair of numbers is found, print them and the answer
    for num1 in inSet:
        for num2 in inSet:
            if (2020 - num1 - num2) in inSet:
                print("Values: ", num1, num2)
                print("Answer: ", num1 * num2)
```

This approach is very time inefficient. For every additional, unique number in the input array, this solution adds an additional computation step for every item in the inSet. This solution has a time complexity O(n<sup>2</sup>).

### Opimal Approach

A more efficient solution is to use a binary search for every item in the inSet to look for another number that sums with the item to equal 2020.

First, we need a binary search algorithm to use.

```python
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
            return mid
        elif list[mid] > target:
            high = mid -1
        else:
            low = mid + 1
    return None
```

Now that we have our binary search implementation, we can use it to search for an addend for each item in the list which sums with it to 2020.

```python
with open("day 1/input.txt") as input:
    inSet = set()

    # I start with a set, append all of the values, and then convert to a list because of the time complexity for each additional item that will be saved if there are no duplicates in the list. This is not a space-optimal operation.
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
```

This function will give us an answer to the first problem in a reasonable amount of time regardless of the size of the input to the problem.

## Problem 2

The second problem of day one is very similar to the first. The only difference is that we now need to find a solution that returns three addends that sum to 2020. Like the last problem, our answer is the product of the three numbers.

### Naive Approach

This naive solution for problem two is almost the same as the naive solution to problem 1. The only difference is that we now add an additional loop to the search portion of the solution.

```python
# load data
with open("day 1/input.txt", "r") as input:
    # create an empty set to hold the data
    inSet = set()

    # add each item from the input list to the inSet
    for num in input:
        inSet.add(int(num))

    # for every num in inSet, check if any other two values in inSet sum with it to 2020. If a solution is found, print the addends and the answer.
    for num1 in inSet:
        for num2 in inSet:
            for num3 in inSet:
                if (2020 - num1 - num2 -num3) in inSet:
                    print("Values: ", num1, num2, num3)
                    print("Answer: ", num1 * num2 * num3)
```

This is an even slower algorithm than the naive solution in problem 1. Because of the extra loop, this solution now has the time complexity O(n<sup>3</sup>)

### Optimal Approach

The optimal solution to this problem is also similar to its problem-one counterpart. For this solution though, we add a loop that iterates over every item in the list and then runs the problem one solution to find the other two numbers. This significantly increases the time complexity of the algorithm, but there are no other solutions that have a relatively similar level of coding complexity.

```python
# load data
with open("day 1/input.txt") as input:
    inSet = set()

    # again we use a set to list converstion to get rid of duplicates
    for num in input:
        inSet.add(int(num))

    inList = list(inSet)

    # this is not an elegant solution to the problem, but it works, and with decent time complexity
    for i in inList:
        for j in inList:
            target = 2020 - i - j

            # k will be the index of the third number that—along with i and j—sums to 2020
            k = BinarySearch(inList, target)

            if k is not None:
                print("Values: ", i, j, k)
                print("answer: ", i * j * k)
                exit()
```
