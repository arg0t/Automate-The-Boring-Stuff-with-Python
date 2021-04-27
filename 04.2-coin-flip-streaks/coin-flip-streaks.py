import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    coinFlipResult = []
    for i in range(100):
        if random.randint(0, 1) == 0:
            coinFlipResult.append('T')
        else:
            coinFlipResult.append('H')

    # Code that checks if there is a streak of 6 heads or tails in a row.
    streak = 6
    numberOfSameSide = 1 # Intialize as 1 not to forget to add the value of 'coinFlipResult[count-1]'
    count = 1
    while count < len(coinFlipResult):
        if coinFlipResult[count] == coinFlipResult[count-1]:
            numberOfSameSide += 1
            if numberOfSameSide == streak:
                numberOfStreaks += 1
                numberOfSameSide = 1 # Reset the value when the new streak found.
                count += 2
            else:
                count += 1 # Reset the value when the new streak lost.

        else:
            numberOfSameSide = 1
            count += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfStreaks)
input()
