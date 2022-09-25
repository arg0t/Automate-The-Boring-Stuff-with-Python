import pyinputplus as pyip 

sandwichMenu = {
	'breadType': {'Wheat': 1.00, 'White': 1.00, 'Sourdough': 1.25},
	'proteinType': {'chicken': 1.5, 'Turkey': 2.5, 'ham': 1.5, 'tofu': 1}, 
	'cheeseType': {'Cheddar': 1.00, 'Swiss': 2.00, 'Mozzarella': 2.5},
	'others': {'Mayo': 0.5 , 'Mustard': 0.5 , 'Lettuce': 0.25 , 'Tomato': 0.25}
	}


usrInput = pyip.inputYesNo(prompt="Do you want to order the sandwich? (y/n)")

while usrInput == 'yes':
	sandwichCost = 0

	breadType = pyip.inputMenu(list(sandwichMenu['breadType'].keys()), 
								prompt='Choose the bread type:\n', numbered=True)

	proteinType = pyip.inputMenu(list(sandwichMenu['proteinType'].keys()), 
								prompt='Choose the protein type:\n', numbered=True)

	isCheeseAdded = pyip.inputYesNo(prompt="Do you want cheese? (y/n)\n")
	
	if isCheeseAdded == 'yes':
		cheeseType = pyip.inputMenu(list(sandwichMenu['cheeseType'].keys()), 
									prompt='Select a cheese type.\n', numbered=True)

	isMayoAdded = pyip.inputYesNo(prompt="Do you want mayo? (y/n)\n")
	isMustardAdded = pyip.inputYesNo(prompt="Do you want mustard? (y/n)\n")
	isLettuceAdded = pyip.inputYesNo(prompt="Do you want lettuce? (y/n)\n")
	isTomatoAdded = pyip.inputYesNo(prompt="Do you want tomato? (y/n)\n")
	totalSandwich = pyip.inputInt(prompt="How many sandwiches do you want?\n", min=1)

	print('Your order will be ready soon. Thank')
	sandwichCost += sandwichMenu['breadType'][breadType]
	print(breadType + ': ' + str(sandwichMenu['breadType'][breadType]) + '$')

	sandwichCost += sandwichMenu['proteinType'][proteinType]
	print(proteinType + ': ' + str(sandwichMenu['proteinType'][proteinType]) + '$')

	if isCheeseAdded == 'yes':
		sandwichCost += sandwichMenu['cheeseType'][cheeseType]
		print(cheeseType + ': ' + str(sandwichMenu['cheeseType'][cheeseType]) + '$')

	if isMayoAdded == 'yes':
		sandwichCost += sandwichMenu['others']['Mayo']
		print('Mayo' + ': ' + str(sandwichMenu['others']['Mayo']) + '$')

	if isMustardAdded == 'yes':
		sandwichCost += sandwichMenu['others']['Mustard']
		print('Mustard' + ': ' + str(sandwichMenu['others']['Mustard']) + '$')

	if isLettuceAdded == 'yes':
		sandwichCost += sandwichMenu['others']['Lettuce']
		print('Lettuce' + ': ' + str(sandwichMenu['others']['Lettuce']) + '$')
		
	if isTomatoAdded == 'yes':
		sandwichCost += sandwichMenu['others']['Tomato']
		print('Tomato' + ': ' + str(sandwichMenu['others']['Tomato']) + '$')

	print('Item price: ' + str(sandwichCost))
	print('Qty: ' + str(totalSandwich))
	print('Total cost: ' + str(sandwichCost * totalSandwich) + '$')

	
	usrInput = pyip.inputYesNo(prompt="Do you want to order another sandwich? (y/n)")
	if usrInput == 'yes':
		continue

	break 
		


	