import random


correctNumber = random.randint(1,100)



inputNumber = int(input("Guess a number between 1 and 100: "))

isCorrect = False

while not isCorrect:
    if inputNumber == correctNumber:
        print("You guessed it! You are a hard worker")
        isCorrect = True
    elif inputNumber > correctNumber:
        print("Too High")
        inputNumber = int(input("Guess a number between 1 and 100: "))
    elif inputNumber < correctNumber:
        print("Too Low")
        inputNumber = int(input("Guess a number between 1 and 100: "))

