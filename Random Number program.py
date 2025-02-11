import random

low = 1
high = 100
option = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

number = random.random( )
options =random.choice(option)
shuffle = random.shuffle(cards)
print(cards)
print(number)
print(options)