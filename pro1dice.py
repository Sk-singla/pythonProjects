import random

dices = { 1: "-------\n|     |\n|  0  |\n|     |\n-------",2: "-------\n|     |\n| 0 0 |\n|     |\n-------",3: "-------\n|  0  |\n|  0  |\n|  0  |\n-------",4: "-------\n| 0 0 |\n|     |\n| 0 0 |\n-------",5: "-------\n| 0 0 |\n|  0  |\n| 0 0 |\n-------",6: "-------\n| 0 0 |\n| 0 0 |\n| 0 0 |\n-------"}

q = 'y'
while(q == 'y' or q == 'Y'):
	num = random.randint(1,6)
	print(dices[num])
	q = input('Want to roll again(y/n): ')