import pyinputplus as pyip
import random, time

numOfQuiz = 10
scores = 0

for quiz in range(numOfQuiz): 
	num1 = random.randint(0,9)
	num2 = random.randint(0,9)
	try:
		# allowRegexes check right answers.
		answer = pyip.inputInt(prompt="#Quiz %s: %s * %s = " % (quiz + 1, num1, num2), 
							allowRegexes = str(num1 * num2), limit=3,timeout=8)

	except pyip.TimeoutException:
		print("Time out!")
		continue

	except pyip.RetryLimitException:
		print("Retry limit reached!")
		continue

	if int(answer) == num1 * num2:
		print('Correct!')
		scores += 1
	else:
		print('Incorrect')

	time.sleep(1)

print('Your scores: %s out of %s ' % (scores, numOfQuiz))
