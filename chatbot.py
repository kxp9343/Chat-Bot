import random

greet = ['Hi', 'Hello', 'Hola']
greetR = ['Hey', 'Bonjour', 'Hi?']
weather = ['It is sunny', 'It is rainy', 'It is cloudy']
movie = ['My favorite movie is Advengers Endgame', 'My favorite movie is Star Wars Force Awakens', 'My favorite movie is Secret Life Of Pets']
feeling = ['Im doing good', 'Im doing okay', 'Im doing bad']

while True:
	ask = input(">>>")
	if ask in greet:
		ran = random.choice(greetR)
		print(ran)
	elif ask == "What's the weather?":
		ran = random.choice(weather)
		print(ran)
	elif ask == "What's your favorite movie?":
		ran = random.choice(movie)
		print(ran)
	elif ask == "How are you doing":
		ran = random.choice(feeling)
		print(ran)
	else:
		print("I don't understand")


