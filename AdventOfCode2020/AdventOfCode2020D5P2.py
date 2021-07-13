BinTranslate = {70:48, 76:48, 66:49, 82:49}

#Abstraction of the decoding process (binary space partitioning).
def AbstractDecoder(bin):
    acc = 0
    sol = 0
    for b in bin[::-1]:
        if int(b):
            sol += 2 ** acc
        acc += 1
    return sol

#Takes in the "binary" seat and return a tuple with the row and column as int.
def Decoder(seat):
    bseat = seat.translate(BinTranslate)
    brow = bseat[:7]
    bcol = bseat[7:]
    return (AbstractDecoder(brow), AbstractDecoder(bcol))

#Takes the decoder output and return the seat identifier.
def Hasher(seattuple):
    return seattuple[0] * 8 + seattuple[1]

#Standard input reading.
with open("AdventOfCode2020\AOC2020Input\AOC2020D5Input.txt", "r") as f:
    InputList = f.readlines()
ParsedInputList = list(map(lambda x: x.strip(), InputList))

#Driver code
DecodedInputList = list(map(Decoder, ParsedInputList))
HashedInputList = list(map(Hasher, DecodedInputList))
NiceHashedInputList = sorted(HashedInputList)
for i in enumerate(NiceHashedInputList):
    if i[1] != i[0] + 13:
        Sol = i[1] - 1
        break

print(Sol)