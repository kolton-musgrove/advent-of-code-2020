import re
from collections import defaultdict

lines = [x.strip() for x in open("Days 6-10/07.txt", "r").readlines()]

bags = defaultdict(dict)

# Data cleaning and dictionary creation
for l in lines:
    bag = re.match(r"(.*) bags contain", l).groups()[0]
    for count, b in re.findall(r"(\d+) (\w+ \w+) bag", l):
        bags[bag][b] = int(count)


# Recursive solution
def part1():
    answer = set()

    def search(color):
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                search(b)

    search("shiny gold")
    return len(answer)

# Recursive solution
def part2():
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count

    return search("shiny gold") - 1  # Rm one for shiny gold itself


print(part2())