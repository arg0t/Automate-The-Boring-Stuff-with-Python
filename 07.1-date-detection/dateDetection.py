#! /bin/python3
import re 

dateReg = re.compile(r'''([0-2]\d/|3[0-1]/) # day
	(0\d/|1[0-2]/) # month 
	([1-2]\d{3})''' # year
	, re.VERBOSE)


txt = '22/12/2022 and tomorrow was 21/02/2022'
matches = []

for groups in dateReg.findall(txt):
	matches.append(groups[0] + groups[1] + groups[2])

if len(matches) > 0:
	print('\n'.join(matches))
else:
	print('No date found.')

