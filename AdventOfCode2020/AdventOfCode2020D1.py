import itertools as it

with open("AdventOfCode2020\AOC2020Input\AOC2020D1Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: int(x.strip()), InputList))
CartesianMess = it.product(ParsedInputList, ParsedInputList)
Solutions = [i*j for i, j in CartesianMess if i + j == 2020]
print(Solutions)