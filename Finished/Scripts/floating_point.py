number = float(input("Number to convert to floating point notation (eg. -124.0): "))
precision = int(input("Precion to use (32 or 64): "))
mantisa = 23 if precision == 32 else 52

signbit = "0" if number > 0 else "1"
afterpointlength = len(str(number).split(".")[1])
afterpoint = round(abs(number) % 1, afterpointlength)
beforepoint = abs(number) - afterpoint

def numberToBinary(num):
    binaryString = []
    currentnum = num
    while currentnum != 0:
        if currentnum % 2 == 0:
            currentnum = currentnum / 2
            binaryString.insert(0, "0")
        else:
            currentnum = (currentnum - 1) / 2
            binaryString.insert(0, "1")
    return "".join(binaryString)

def decimalToBinary(num):
    binaryString = []
    currentnum = num
    while currentnum != 0 and (len(beforepointbinary)) + len(binaryString) < mantisa:
        currentnum = currentnum * 2
        if currentnum >= 1:
            currentnum = round(currentnum - 1, afterpointlength)
            binaryString.append("1")
        else:
            binaryString.append("0")
    return "".join(binaryString)

beforepointbinary = numberToBinary(beforepoint)[1:]
exponent = numberToBinary(len(beforepointbinary) + 127 if precision == 32 else 1023)
afterpointbinary = decimalToBinary(afterpoint)

result = signbit + exponent + beforepointbinary + afterpointbinary

result = result + "".join(["0" for i in range(precision - len(result))])

print(result)