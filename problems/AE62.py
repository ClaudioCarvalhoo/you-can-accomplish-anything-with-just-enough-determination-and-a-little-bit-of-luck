# Phone Number Mnemonics

# O(4ⁿ*n)
# n = len(phoneNumber)

def phoneNumberMnemonics(phoneNumber):
    numberDict = {
		'1': ['1'],
		'2': ['a', 'b', 'c'],
		'3': ['d', 'e', 'f'],
		'4': ['g', 'h', 'i'],
		'5': ['j', 'k', 'l'],
		'6': ['m', 'n', 'o'],
		'7': ['p', 'q', 'r', 's'],
		'8': ['t', 'u', 'v'],
		'9': ['w', 'x', 'y', 'z'],
		'0': ['0']
	}
	res = [[]]
	for number in phoneNumber:
		temp = []
		for i in range(len(res)):
			for letter in numberDict[number]:
				temp.append(res[i] + [letter])
		res = temp
	return [''.join(x) for x in res]
