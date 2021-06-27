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
        
        #Obsolete code, first iteration, left for reference
        """
        #M bit
        if dig4 >= 1:
            for i in range(dig4):
                romout += "M"
                
        #CD bit
        if dig3 >= 5:
            if dig3 % 5 == 4:
                romout += "CM"
            else:
                romout += "D"
                try:
                    for i in range(dig3 % 5):
                        romout += "C"
                except Exception:
                    pass
        else: 
            if dig3 == 4:
                romout += "CD"
            else:
                try:
                    for i in range(dig3):
                        romout += "C"
                except Exception:
                    pass
        #XL bit
        if dig2 >= 5:
            if dig2 % 5 == 4:
                romout += "XC"
            else:
                romout += "L"
                try:
                    for i in range(dig2 % 5):
                        romout += "X"
                except Exception:
                    pass
        else: 
            if dig2 == 4:
                romout += "XL"
            else:
                try:
                    for i in range(dig2):
                        romout += "X"
                except Exception:
                    pass
                
        #IV bit
        if dig1 >= 5:
            if dig1 % 5 == 4:
                romout += "IX"
            else:
                romout += "V"
                try:
                    for i in range(dig1 % 5):
                        romout += "I"
                except Exception:
                    pass
        else: 
            if dig1 == 4:
                romout += "IV"
            else:
                try:
                    for i in range(dig1):
                        romout += "I"
                except Exception:
                    pass
        """
        
        #Basically a simplification of the above code.
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
                        
        #return statement
        return romout
    
    @staticmethod
    def from_roman(romin):
        
        #heh
        """
        count = 1
        while True:
            if romin == RNC.to_roman(count):
                return count
            else:
                count += 1
        """
        
        #Sight and foresight aproach
        #If sight < foresight substract foresight-sight, add to decout and skip a step
        #else add sight to decout and continue normally
    
RomanNumerals = RNC()