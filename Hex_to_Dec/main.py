hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
# TODO: use recursion to accept more than 3 digit input

def hexToDec(hexNum):
    for i in hexNum:
        if i not in hexNumbers:
            return None
    if len(hexNum) == 3:
        return hexNumbers[str(hexNum[0])]*(16*16) + hexNumbers[str(hexNum[1])]*16 + hexNumbers[str(hexNum[2])]
    if len(hexNum) == 2:
        return hexNumbers[str(hexNum[0])]*16 + hexNumbers[str(hexNum[1])]
    if len(hexNum) == 1:
        return hexNumbers[str(hexNum[0])]

print(hexToDec("ABCDE"))

