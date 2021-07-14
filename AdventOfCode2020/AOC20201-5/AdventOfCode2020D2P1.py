def DataPerLine(mystr):
    anchor = (mystr.find(" "), mystr.find("-"))
    rangedata = (int(mystr[0:anchor[1]]), int(mystr[anchor[1] + 1:anchor[0]]))
    keydata = mystr[anchor[0] + 1]
    return (rangedata, keydata, mystr[anchor[0] + 4:])

def Validator(args):
    counter = args[2].count(args[1])
    if counter <= args[0][1] and counter >= args[0][0]:
        return True
    else:
        return False

with open("AdventOfCode2020\AOC2020Input\AOC2020In1-5\AOC2020D2Input.txt", "r") as f:
    InputList = f.readlines()

ParsedInputList = list(map(lambda x: x.strip(), InputList))
DataList = list(map(DataPerLine, ParsedInputList))
ProcessedDataList = list(map(Validator, DataList))
print(ProcessedDataList.count(True))