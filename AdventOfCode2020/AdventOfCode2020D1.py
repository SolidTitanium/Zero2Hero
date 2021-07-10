import itertools as it

with open("AdventOfCode2020\AOC2020Input\AOC2020D1P2Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: int(x.strip()), InputList))
CartesianMess = it.combinations(ParsedInputList, 3)
Solutions = [i*j*k for i, j, k in CartesianMess if i + j + k == 2020]
print(Solutions)