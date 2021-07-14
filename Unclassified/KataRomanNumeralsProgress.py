import math as m

class RNC:
    
    Numerals = ("I", "V", "X", "L", "C", "D", "M")
    
    #Index provider function
    @staticmethod
    def symbolfinder(order, ind):
        index = (order - 1) * 2 + ind - 1
        return RNC.Numerals[index]
    
    @staticmethod
    def to_roman(decin):
        
        #Initialization (potential for list comprehension?)
        #YES dig = [int(m.floor(decin/(10**n)) % 10) for n in range(3,-1,-1)]
        #left it this way for...comprehension purposes... (plus the none at the start is important, thought not crucial)
        romout = ""
        dig4 = int(m.floor(decin/1000))
        dig3 = int(m.floor(decin/100) % 10)
        dig2 = int(m.floor(decin/10) % 10)
        dig1 = int(decin % 10)
        dig = [None, dig1, dig2, dig3, dig4]
        
        #The iterator mess is about counting how many digits the input has
        #but due to how the code works it only needs to know the amount
        #if there are less than 4
        for n in range(min(4,m.floor(m.log10(decin)+1)),0,-1):
            if n == 4:
                for i in range(dig[n]):
                    romout += RNC.symbolfinder(n, 1)
            else:
                if dig[n] >= 5:
                    if dig[n] % 5 == 4:
                        romout += RNC.symbolfinder(n,1) + RNC.symbolfinder(n+1,1)
                    else:
                        romout += RNC.symbolfinder(n,2)
                        try:
                            for i in range(dig[n] % 5):
                                romout += RNC.symbolfinder(n,1)
                        except Exception:
                            pass
                else:
                    if dig[n] == 4:
                        romout += RNC.symbolfinder(n,1) + RNC.symbolfinder(n,2)
                    else:
                        try:
                            for i in range(dig[n]):
                                romout += RNC.symbolfinder(n,1)
                        except Exception:
                            pass
                        
        return romout
    
    @staticmethod
    def from_roman(romin):
        
        #Initialization
        key = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        rominl = list(romin)
        rominc = rominl.copy()
        rominc.pop(0)
        rominc.append("I")
        myiter = zip(rominl, rominc)
        decout = 0
        
        #sight and foresight aproach
        #if sight < foresight add foresight - sight and skip a step
        #else add sight
        for i, j in myiter:
            if key[i] < key[j]:
                decout += key[j] - key[i]
                next(myiter)
            else:
                decout += key[i]
                
        return decout
    
RomanNumerals = RNC()