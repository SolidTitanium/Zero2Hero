#Takes in a list of strings that contains the group answers by person and outputs the number of unique answers
def QuestionCounter(group):
    setquestions = set(())
    listquestions = []
    sol = 0
    for q in group:
        for a in q:
            setquestions.add(a)
            listquestions.append(a)
    for ans in setquestions:
        if listquestions.count(ans) == len(group):
            sol += 1
    return sol

#Standard input reading.
with open("AdventOfCode2020\AOC2020Input\AOC2020In6-10\AOC2020D6Input.txt", "r") as f:
    InputList = f.readlines()
ParsedInputList = list(map(lambda x: x.strip(), InputList))

Sol = 0
Curr = 0
Group = []
ItemCount = len(ParsedInputList)

#Driver code
for person in ParsedInputList:
    Curr += 1
    if person == "" or Curr == ItemCount:
        Sol += QuestionCounter(Group)
        Group = []
    elif person != "":
        Group.append(person)
    
print(Sol)