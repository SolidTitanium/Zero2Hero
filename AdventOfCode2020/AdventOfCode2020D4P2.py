import re

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
counter = 0

class RangeValidators:

    @staticmethod
    def byr(value):
        if value.isdigit():
            if int(value) <= 2002 and int(value) >= 1920:
                return True
        return False
    
    @staticmethod
    def iyr(value):
        if value.isdigit():
            if int(value) <= 2020 and int(value) >= 2010:
                return True
        return False

    @staticmethod
    def eyr(value):
        if value.isdigit():
            if int(value) <= 2030 and int(value) >= 2020:
                return True
        return False

    @staticmethod
    def hgt(value):
        if value[:-2].isdigit():
            if value[-2:] == "cm":
                if int(value[:-2]) <= 193 and int(value[:-2]) >= 150:
                    return True
            if value[-2:] == "in":
                if int(value[:-2]) <= 76 and int(value[:-2]) >= 59:
                    return True
        return False

    @staticmethod
    def hcl(value):
        if re.match(r"^#[0-9a-fA-F]{6}$", value) != None:
            return True
        return False

    @staticmethod
    def ecl(value):
        acceptedvalues = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        if value in acceptedvalues:
            return True
        return False

    @staticmethod
    def pid(value):
        if re.match(r"^[0-9]{9}$", value) != None:
            return True
        return False

    @staticmethod
    def cid(value):
        return True


def Redirect(value, field):
    return getattr(RangeValidators, field)(value)


def Validator(mystr):
    checklist = []
    for field in fields:
        strexpr = field + r"(:\S+)"
        expr = re.compile(strexpr)
        lookme = expr.search(mystr)
        if lookme == None:
            checklist.append(False)
        else:
            validrange = Redirect(lookme.group(1)[1:], field)
            if validrange == True:
                checklist.append(True)
            else:
                checklist.append(False)
    return checklist

with open("AdventOfCode2020\AOC2020Input\AOC2020D4Input.txt", "r") as f:
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