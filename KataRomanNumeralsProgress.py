import math as m

class RomanNumeralsClass:
    
    Numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    @staticmethod
    def to_roman(decin):
        #Initialization
        romout = ""
        dig4 = int(m.floor(decin/1000))
        dig3 = int(m.floor(decin/100) % 10)
        dig2 = int(m.floor(decin/10) % 10)
        dig1 = int(decin % 10)
        #M bit
        if dig4 >= 1:
            for i in range(dig4):
                romout += "M"
        #CD bit
        if dig3 >= 5:
            if dig3 % 5 == 4:
                romout += "CM"
            else:
                try:
                    for i in range(dig3 % 5):
                        temp3 += "C"
                    romout += "D" + temp3
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
                try:
                    for i in range(dig2 % 5):
                        temp2 += "X"
                    romout += "L" + temp2
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
                try:
                    for i in range(dig1 % 5):
                        temp1 += "I"
                    romout += "V" + temp1
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
        #Generalized secuence for writing chars in romout
        #n refers to the magnitude of the char, first and second indicates
        #if is the 1*10^n char or 5*10^n char
        #the first and second 1 chars are "I" and "V"
        #the first and second 2 chars are "X" and "L"
        #the first and second 3 chars are "C" and "D"
        # theres only one 4 char "M"
        """
        #Gen bit
        if dign >= 5:
            if dign % 5 == 4:
                romout += "firstnchar"+"firstn+1char"
            else:
                romout += "secondnchar"
                try:
                    for i in range(dign % 5):
                        romout += "firstnchar"
                except Exception:
                    pass
        else:
            if dign == 4:
                romout += "firstnchar"+"secondnchar"
                else:
                    try:
                        for i in range(dign):
                            romout += "firstnchar"
                    except Exception:
                        pass
        """

        return romout
    
    @staticmethod
    def from_roman(romin):
        pass
RomanNumerals = RomanNumeralsClass()