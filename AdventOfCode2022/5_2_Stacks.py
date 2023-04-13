import re

def execute_order(order):
    val = int(order["val"])
    origin = int(order["origin"])
    target = int(order["target"])
    stacks[target - 1].extend(stacks[origin - 1][-val:])
    stacks[origin - 1] = stacks[origin - 1][:-val]

def create_order(line):
    match = regex.match(line)
    return {"val":match.group(1), "origin":match.group(2), "target":match.group(3)}

#setup
with open("./Inputs/5_1_Input.txt") as f:
    lines = [line.strip() for line in f.readlines()[10:]]

stacks = [["W", "B", "D", "N", "C", "F", "J"],
          ["P", "Z", "V", "Q", "L", "S", "T"],
          ["P", "Z", "B", "G", "J", "T"],
          ["D", "T", "L", "J", "Z", "B", "H", "C"],
          ["G", "V", "B", "J", "S"],
          ["P", "S", "Q"],
          ["B", "V", "D", "F", "L", "M", "P", "N"],
          ["P", "S", "M", "F", "B", "D", "L", "R"],
          ["V", "D", "T", "R"]]

regex = re.compile(r"move (\d+) from (\d+) to (\d+)")

#iter
orders = [create_order(line) for line in lines]
for order in orders:
    execute_order(order)
for stack in stacks:
    print(stack.pop())
