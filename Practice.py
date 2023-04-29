import requests
from bs4 import BeautifulSoup
import csv
from random import choice

def translate(random_word):
	url = "https://www.morfix.co.il/"+random_word
	response = requests.get(url, timeout=2)
	soup = BeautifulSoup(response.text, "html.parser")
	translation = soup.find(class_="normal_translation_div").get_text()
	return translation[::-1]

def format_to_a_list(ls):
	words = []
	for l in ls:
		words.append(l[0])
	return words

words_I_know = []
words_I_dont_know = []

with open("weekly_practice.csv") as csv_file:
	csv_reader = csv.reader(csv_file)
	words_I_dont_know = format_to_a_list(list(csv_reader))
	
while True:
	if len(words_I_dont_know) == 0:
		break
	random_word = choice(words_I_dont_know)
	print(random_word)
	
	#reavel translation
	if(input("Press AnyThing (Except Enter) to reveal translation: ")):
		print(translate(random_word))

	if(input("Did you know the answer? (Type y/n): ").lower() in ["Yes", "y"]):
		words_I_know.append(random_word)
		words_I_dont_know.remove(random_word)

	print(" "*1)
	print(f"words I know: {words_I_know}")
	print(" "*1)

	my_input = input("Do you want to quit?")
	if (my_input.lower() in ["y", "yes"]):
		break

print(" "*1)
print("Thanks For The Daily Practice! See You Tommorow!") 
