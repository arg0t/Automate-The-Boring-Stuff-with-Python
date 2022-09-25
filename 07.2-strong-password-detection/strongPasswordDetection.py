#! /bin/python3

import re

def detectStrongPassword(passwd):

	# at least eight characters long
	least8Re = re.compile(r'.{8,}')
	# contains uppercase 
	upCaseRe = re.compile(r'[A-Z]{1,}')
	# conatins lowercase
	lowCaseRe = re.compile(r'[a-z]{1,}')
	# has at least one digit
	oneDigitRe = re.compile(r'\d{1,}')

	mo1 = least8Re.findall(passwd)
	mo2 = lowCaseRe.findall(passwd)
	mo3 = upCaseRe.findall(passwd)
	mo4 = oneDigitRe.findall(passwd)

	return len(mo1) > 0 and len(mo2) > 0 and len(mo3) > 0 and len(mo4) > 0



validPassword = 'abC123456D'
numOnlypassword = '12345678'
shortPassword = '12Dc'
upPassword = 'ABCDEFGGHJK'
lowPassword = 'qwertyasdfjk'

passwordList = [validPassword, numOnlypassword, shortPassword, upPassword, lowPassword]

# only passwordList[0] is strong password. 
for passwd in passwordList:

	if detectStrongPassword(passwd):
		print('Your password is strong!')
	else:
		print('Your password weak.')



