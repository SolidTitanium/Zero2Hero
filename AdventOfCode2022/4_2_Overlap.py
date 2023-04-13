def check(pair):
    pivot = pair[0]
    free = pair[1]
    condition1 = (pivot[0] <= free[0] and free[0] <= pivot[1])
    condition2 = (pivot[0] <= free[1] and free[1] <= pivot[1])
    condition3 = (free[0] <= pivot[0] and free[1] >= pivot[1])
    return condition1 or condition2 or condition3

with open("./Inputs/4_1_Input.txt") as f:
    pairs = [line.strip().split(",") for line in f.readlines() if not line.isspace()]

pairs = [[work.split("-") for work in pair] for pair in pairs]
pairs = [[[int(num) for num in work] for work in pair] for pair in pairs]
print(sum(1 for pair in pairs if check(pair)))
