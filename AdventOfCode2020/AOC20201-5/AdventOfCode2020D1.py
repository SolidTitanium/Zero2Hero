import itertools as it

#AdventOfCode2020\AOC2020Input\AOC2020D1P1Input.txt
with open("AdventOfCode2020\AOC2020Input\AOC2020In1-5\AOC2020D1P1Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: int(x.strip()), InputList))
#CartesianMess = it.combinations(ParsedInputList, 2)
CartesianMess = it.combinations(ParsedInputList, 3)
#Solutions = [i*j for i, j in CartesianMess if i + j == 2020]
Solutions = [i*j*k for i, j, k in CartesianMess if i + j + k == 2020]
print(Solutions)