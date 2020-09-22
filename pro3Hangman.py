import random
turns = 10
l = ["samarth","gupta"]
word = random.choice(l)
length = len(word)

Name = input("Enter ur name: ")
print(f"Welcome {Name}")
print(f"Try to guess the word in less than {turns} attempts")
guessmade =""

while(True):
	main = ""
	for letter in word:
		if letter in guessmade:
			main += letter
		else:
			main += "_"+""

	if main== word:
		print(main)
		print("you win!")
		break

	print("Guess the word",main)
	guess = input()
	if(guess in word):
		guessmade += guess
	else:
		turns -= 1
		if turns == 9:
			print("  ---------  ")

		elif turns == 8:
			print("  ---------  ")
			print("      O      ")

		elif turns ==7:
			print("  ---------  ")
			print("      O      ")
			print("      |      ")
		elif turns ==6:
			print("  ---------  ")
			print("      O      ")
			print("      |      ")
			print("      |      ")
		elif turns ==5:
			print("  ---------  ")
			print("      O      ")
			print("      |      ")
			print("     /       ")

		elif turns ==4:
			print("  ---------  ")
			print("      O      ")
			print("      |      ")
			print("     / \     ")
		elif turns ==3:
			print("  ---------  ")
			print("      O/     ")
			print("      |      ")
			print("     / \     ")
		elif turns ==2:
			print("  ---------  ")
			print("     \O/     ")
			print("      |      ")
			print("     / \     ")
		elif turns ==1:
			print("  ---------  ")
			print("      |      ")
			print("     \O/     ")
			print("      |      ")
			print("     / \     ")
		elif turns ==0:
			print("  ---------  ")
			print("      |      ")
			print("      O      ")
			print("     /|\      ")
			print("     / \     ")
			print("You Loss the Game. Man die!")
			break;
		