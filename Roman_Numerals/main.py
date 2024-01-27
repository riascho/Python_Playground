#TODO: define unit testing!

numerals = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}

def roman_to_num(string):
    pass

def num_to_roman(number):
    output = ""
    while number > 0:
        for letter,increment in numerals.items():
            amount = number//increment
            output +=(amount)*letter
            number -=(amount*increment) 
    if "DCCCC" in output: #900
        output = output.replace("DCCCC","CM")
    if "LXXXX" in output: #90
        output = output.replace("LXXXX","XC")
    if "VIIII" in output: #9
        output = output.replace("VIIII","IX")
    if "CCCC" in output: #400
        output = output.replace("CCCC","CD")
    if "XXXX" in output: #40
        output = output.replace("XXXX","XL")
    if "IIII" in output: #4
        output = output.replace("IIII","IV")
    return output

print(num_to_roman(2444))
#1990 is MCMXC