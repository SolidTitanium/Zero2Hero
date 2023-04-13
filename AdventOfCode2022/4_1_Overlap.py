def check(pair):
    conditionA = pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]
    conditionB = pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]
    return conditionA or conditionB

with open("./Inputs/4_1_Input.txt") as f:
    pairs = [line.strip().split(",") for line in f.readlines() if not line.isspace()]

pairs = [[work.split("-") for work in pair] for pair in pairs]
pairs = [[[int(num) for num in work] for work in pair] for pair in pairs]
print(sum(1 for pair in pairs if check(pair)))
