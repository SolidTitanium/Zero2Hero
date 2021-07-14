def TreeCounter(forest, **ratio):
    linecounter = 0
    treecounter = 0
    skip = 0
    for line in forest:
        if (skip % ratio["down"] == ratio["down"] - 1) and ratio["down"] != 1:
            skip += 1
            continue
        elif line[(linecounter * ratio["side"]) % 31] == "#":
            treecounter += 1
        linecounter +=1
        if ratio["down"] != 1:
            skip += 1
    return treecounter

def ProductTreeCounter(forest, *ratios):
    carry = 1
    results = []
    for ratio in ratios:
        results.append(TreeCounter(forest, down = ratio[0], side = ratio[1]))
    for i in results:
        carry = carry * i
    return carry

with open("AdventOfCode2020\AOC2020Input\AOC2020In1-5\AOC2020D3Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: x.strip(), InputList))
ratios = ((1, 1), (1, 3), (1, 5), (1, 7), (2, 1))
x = ProductTreeCounter(ParsedInputList, *ratios)

print(x)