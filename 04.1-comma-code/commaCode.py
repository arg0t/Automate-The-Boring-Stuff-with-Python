def commaCode(inputList):
    outputString = ""
    if len(inputList) == 0:
        return "List can not be empty. Try again."

    else:
        for i in range(len(inputList)-1):
            outputString = outputString + str(inputList[i]) + ", "

        outputString = outputString + "and " + str(inputList[-1])

    return outputString

spam =  ['bat', 'rat', 'cow', 4, 3.142]
egg = []

print(commaCode(spam))
print(commaCode(egg))
input()
