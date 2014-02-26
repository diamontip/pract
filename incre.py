text = input('enter text that need to be printed in incremental order:\n')
second = ''

i = len(text) - 1
j = 0
print('--------------\ninitiated\n--------------\n')
while j != i:
	second = second + text[j]
	print (second)
	j = j + 1
	
print('\n--------------\ncompleted\n--------------')
