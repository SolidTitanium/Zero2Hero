from os import access


class Bag:
    relmatrix = []
    translatedict = {}

    def __init__(self, color, id):
        self.color = color
        self.id = id
        Bag.translatedict.update({self.color: self.id})
    
    #Bags come in (number, color) pairs, add bags to the relation matrix.
    @staticmethod
    def AddBags(*bags):
        rel = [0 for i in range(len(Bag.translatedict))]
        for bag in bags:
            currindex = Bag.translatedict[bag[1]]
            rel.insert(currindex, bag[0])
            rel.pop(currindex + 1)
        Bag.relmatrix.append(rel)

    #Gets a string with averything after the word "contain", returns a list with (number, color) pairs.
    @staticmethod
    def BagShipping(bagstr):

        #To Big for a lambda, to small for anything else.
        def SmallBagShipping(bbag):
            #Removing bag/bags.
            rblank = bbag.rfind(" ")
            bag = bbag[:rblank]

            #Pair builder.
            blank = bag.find(" ")
            number = int(bag[:blank])
            color = bag[blank + 1:]
            return (number, color)

        if bagstr == " no other bags":
            return []
        baglist = bagstr.split(",")
        bags = list(map(lambda x: x.strip(), baglist))
        return list(map(SmallBagShipping, bags))
    
    #Calling this takes the line and uploads it to the relation matrix.
    @staticmethod
    def Linehandler(line):
        contains = line.find("contain")
        bagstr = line[contains + 7:]
        bags = Bag.BagShipping(bagstr)
        Bag.AddBags(*bags)

    #Searches for bags that directly contain this one, returns container bags ID and number of copies,
    #aditionally if the flag is set return the ID of the searched bag.
    @staticmethod
    def Search(ID, flag = 0):
        counter = 0
        containers = []
        for bag in TransposedRelationMatrix[ID]:
            if bag > 0:
                if flag == 0:
                    containers.append((counter, bag))
                else:
                    containers.append((counter, bag, ID))
            counter += 1
        return containers

#Standard input reading.
with open("AdventOfCode2020\AOC2020Input\AOC2020In6-10\AOC2020D7Input.txt", "r") as f:
    InputList = f.readlines()
ParsedInputList = list(map(lambda x: x.strip().rstrip("."), InputList))

#ObjectInstantiation.
IdCounter = 0
for line in ParsedInputList:
    contain = line.find("contain")
    Bag(line[:contain - 6], IdCounter)
    IdCounter += 1

#Relationship matrix filling.
for line in ParsedInputList:
    Bag.Linehandler(line)

#Reverse seek for containment
Trans = []
for Entry in range(len(Bag.relmatrix)):
    current = []
    for bag in Bag.relmatrix[Entry]:
        current.append(bag)
    Trans.append(current)


#This list comprehension is product of 1 hour of headbanging myself against the code
#I understand the inner list easily but the outer one troubles me
#i think the catch is on using range(len(Bag.translatedict)) but I'm not sure.
TransposedRelationMatrix = [[i[k] for i in Bag.relmatrix] for k in range(len(Bag.translatedict))]
RTranslateDict = {v: k for k, v in Bag.translatedict.items()}
Flist = [299]
short = []
while True:
    acc = []
    for bag in Flist:
        if bag in short:
            pass
        else:
            acc.extend(Bag.Search(bag))
    print(acc)
    short = []
    short.extend(Flist)
    if acc == []:
        break
    for bag in acc:
        Flist.append(bag[0])

NoDups = set(Flist)

print(len(NoDups) - 1)

"""
#Return all bags that contain bag with ID 299 (shiny gold)
FCount = 0
for bag in TransposedRelationMatrix[519]:
    if bag > 0:
        print("ID =", FCount, "Position =", FCount + 1, "Color =", RTranslateDict[FCount])
    FCount += 1
"""

"""
SEND HELP BRAIN HURTS
FCount = 0
for bag in Bag.relmatrix[0]:
    if bag > 0:
        print(bag, RTranslateDict[FCount])
    FCount += 1


DCount = 0
dark_orage_row = [i[492] for i in Bag.relmatrix]
for bag in dark_orage_row:
    if bag > 0:
        print(DCount, RTranslateDict[DCount])
    DCount += 1

print("----")

Trans = [[i[k] for i in Bag.relmatrix] for k in range(len(Bag.translatedict))]

LCount = 0
for bag in Trans[492]:
    if bag > 0:
        print(LCount, RTranslateDict[LCount])
    LCount += 1 

print(Bag.translatedict["dark orange"])
print(Bag.relmatrix[0][492])
"""