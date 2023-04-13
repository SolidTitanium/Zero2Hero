def translate(char):
    val = ord(char)
    if val <= 90 and val >= 65:
        return val - 38
    return val - 96

with open("./Inputs/3_1_Input.txt") as f:
    rucksacks = [rucksack.strip() for rucksack in f.readlines() if rucksack != ""]

groups = [rucksacks[i*3:i*3+3] for i in range(len(rucksacks)//3)]
char_sets = [{char for char in group[0] if (char in group[1]) and (char in group[2])} for group in groups]
print(sum(translate(char) for char_set in char_sets for char in char_set))
