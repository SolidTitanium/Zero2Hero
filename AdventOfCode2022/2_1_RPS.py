rules = {"A":[3,6,0], "B":[0,3,6], "C":[6,0,3]}
translate = {"X":1, "Y":2, "Z":3}

with open(r".\Inputs\2_1_Input.txt") as f:
    games = [game.strip() for game in f.readlines()]

points = [rules[game[0]][translate[game[-1]]-1]+translate[game[-1]] for game in games if game != ""]
result = sum(points)
print(result)
