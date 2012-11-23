#Numeral Converter project
import math
def integer_roman(n):
    """
    Returns a number in roman, converted from integer
    """
    table=[['M',1000],['CM',900],['D',500],['CD',400],['C',100],['XC',90],['L',50],['XL',40],['X',10],['IX',9],['V',5],['IV',4],['I',1]]
    romNum = ""
    
    for pair in table:
        numLtr = n/pair[1]
        if numLtr > 3:
            numLtr = 3
        n -= pair[1]*numLtr
        romNum += pair[0]*numLtr
        
    return romNum