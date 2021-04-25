def collatz(num):
    if num % 2 == 0:
        return num // 2
    else:
        return 3 * num + 1

print('Enter a number:')
number = int(input())

while number > 1:
    number = collatz(number)
    print(number)
