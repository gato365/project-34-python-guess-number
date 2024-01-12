
correctNumber = 73

inputNumber = int(input("Guess a number between 1 and 100: "))

isCorrect = False

while not isCorrect:
    if inputNumber == correctNumber:
        print("You guessed correctly!")
        isCorrect = True
    elif inputNumber > correctNumber:
        print("Your guess is too high!")
        inputNumber = int(input("Guess a number between 1 and 100: "))
    else:
        print("Your guess is too low!")
        inputNumber = int(input("Guess a number between 1 and 100: "))