def translate(char):
    val = ord(char)
    if val <= 90 and val >= 65:
        return val - 38
    return val - 96

with open("./Inputs/3_1_Input.txt") as f:
    rucksacks = [rucksack.strip() for rucksack in f.readlines() if rucksack != ""]

rucksacks = [(rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]) for rucksack in rucksacks]
char_sets = [{char for char in rucksack[0] if char in rucksack[1]} for rucksack in rucksacks]
print(sum(translate(char) for char_set in char_sets for char in char_set))
