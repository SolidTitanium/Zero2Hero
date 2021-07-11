with open("AdventOfCode2020\AOC2020Input\AOC2020D3Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: x.strip(), InputList))
linecounter = 0
treecounter = 0
for line in ParsedInputList:
    if line[(linecounter * 3) % 31] == "#":
        treecounter += 1
    linecounter +=1
print(treecounter)