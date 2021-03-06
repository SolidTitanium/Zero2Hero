#Takes in a single string that contains the group answers and outputs the number of unique answers
def QuestionCounter(group):
    questions = set(())
    for q in group:
        questions.add(q)
    return len(questions)

#Standard input reading.
with open("AdventOfCode2020\AOC2020Input\AOC2020In6-10\AOC2020D6Input.txt", "r") as f:
    InputList = f.readlines()
ParsedInputList = list(map(lambda x: x.strip(), InputList))

Sol = 0
Curr = 0
Group = ""
ItemCount = len(ParsedInputList)

#Driver code
for person in ParsedInputList:
    Curr += 1
    if person == "" or Curr == ItemCount:
        Sol += QuestionCounter(Group)
        Group = ""
    elif person != "":
        Group += person
    
print(Sol)