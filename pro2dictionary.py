import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
	word = word.lower()

	if word in data:
		return data[word]

	elif word.title() in data:
		return data[word.title()]

	elif word.upper() in data:
		return data[word.upper()]

	elif len(get_close_matches(word,data.keys())) >0:
		qr =input("Do u mean %s  ('y' or 'n')"%get_close_matches(word,data.keys())[0])
		if(qr == 'y' or qr == 'Y'):
			return data[get_close_matches(word,data.keys())[0]]

	else:
		print("Incorrect word!")

#=====================================================
wd = input("Enter the word: ")
output = translate(wd)
if type(output) == list:
	for i in range(len(output)):
		print(i+1,". ",output[i],sep = "")
else:
	print(output)