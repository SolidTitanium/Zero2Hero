with open("./Inputs/1_2_Input.txt") as f:
    text = f.read()

elves = [elf.split("\n") for elf in text.split("\n\n")]
elves = [[int(food.strip()) for food in elf if food != ""] for elf in elves]
sum_elves = [sum(elf) for elf in elves]
sum_elves.sort(reverse = True)
result = sum_elves[:3]
print(sum(result))
