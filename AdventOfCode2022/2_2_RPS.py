rules = {"A":[3,1,2], "B":[1,2,3], "C":[2,3,1]}
translate = {"X":0, "Y":3, "Z":6}

with open(r".\Inputs\2_1_Input.txt") as f:
    games = [game.strip() for game in f.readlines()]

points = [rules[game[0]][translate[game[-1]]//3]+translate[game[-1]] for game in games if game != ""]
result = sum(points)
print(result)
