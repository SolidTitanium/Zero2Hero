import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
counter = 0

def Validator(mystr):
    checklist = []
    for field in fields:
        strexpr = field + r"(?=:)"
        expr = re.compile(strexpr)
        if expr.search(mystr) != None:
            checklist.append(True)
        else:
            checklist.append(False)
    return checklist

with open("AdventOfCode2020\AOC2020Input\AOC2020In1-5\AOC2020D4Input.txt", "r") as f:
    InputList = f.readlines()

passport = ""
for line in InputList:
    if line == "\n":
        checklist = Validator(passport)
        checklist.pop()
        if all(checklist):
            counter += 1
        passport = ""
    else:
        passport += line

print(counter)