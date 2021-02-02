import re


def PuzzleOne():
    with open("day 4/input.txt") as passportData:
        # number of valid passports
        answer = 0
        # dictionary to store each passport's data
        passport = {}
        # an array of the needed types of data on each passport
        requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

        for line in passportData:
            # we first want to remove the new line character at the end of each line
            line = line.strip()

            # this if statement allows for the capture of each passport's complete data. Since the most passports are on seperate lines, we can read each line and combine them until we encounter a blank line which indicates the end of a passport. Then we can check to see if all the necessary data is in each passport.
            if not line:
                valid = True

                for item in requiredFields:
                    if item not in passport:
                        valid = False

                if valid:
                    answer += 1
                passport = {}
            else:
                fields = line.split()
                for field in fields:
                    k, v = field.split(":")
                    passport[k] = v

        print(answer)


def PuzzleTwo():
    with open("day 4/input.txt") as passportData:
        # number of valid passports
        answer = 0
        # dictionary to store each passport's data
        passport = {}

        for line in passportData:
            # same new line cleaning as in problem one
            line = line.strip()

            # same if statement to collect all data for each passport
            if not line:
                valid = True

                # the first three are simple numerical range checks
                if "byr" not in passport or not (1920 <= int(passport["byr"]) <= 2002):
                    valid = False
                if "iyr" not in passport or not (2010 <= int(passport["iyr"]) <= 2020):
                    valid = False
                if "eyr" not in passport or not (2020 <= int(passport["eyr"]) <= 2030):
                    valid = False
                
                # height gets a litle more tricky. we need to deal with multiple measurement types (inches and centimeters)
                if "hgt" in passport:
                    ht = passport["hgt"]
                    # first use a regular expression to get all digits that appear at least once and combine them into one number
                    nums = re.findall(r"\d+", ht)
                    ht_n = "".join(nums)

                    # then we check if that number is valid based on if the height is measures in inches or in centimeters
                    if ht.endswith("in"):
                        if not 59 <= int(ht_n) <= 76:
                            valid = False
                    elif ht.endswith("cm"):
                        if not 150 <= int(ht_n) <= 193:
                            valid = False
                    else:
                        valid = False
                else:
                    valid = False

                # the hair color can be validated using list comprehension
                if "hcl" in passport:
                    hcl = passport["hcl"]
                    # check whether the hcl starts with a hashtag and consists of six other numberical values or not
                    if hcl[0] != "#" or any(
                        [c not in "0123456789abcdef" for c in hcl[1:]] or len(hcl) != 7
                    ):
                        valid = False
                else:
                    valid = False

                # eye color is just checking whether the given color is one of the avaiable options
                if "ecl" not in passport or passport["ecl"] not in [
                    "amb",
                    "blu",
                    "brn",
                    "gry",
                    "grn",
                    "hzl",
                    "oth",
                ]:
                    valid = False

                if "pid" in passport:
                    pid = passport["pid"]
                    # check if the pid is a nine-character numeric string
                    if len(pid) != 9 or any([c not in "0123456789" for c in pid]):
                        valid = False
                else:
                    valid = False

                if valid:
                    answer += 1
                passport = {}
            else:
                # same method for collecting each passport's complete data as in problem 1
                words = line.split()
                for word in words:
                    k, v = word.split(":")
                    passport[k] = v

        print(answer)


PuzzleOne()

PuzzleTwo()