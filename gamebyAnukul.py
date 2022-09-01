# specific number guessing : 
guess_number = 10
guess=int(input("Please guess the number between 1 to 10 : "))
if guess > guess_number:
    print("Sorry your guess was too high")
elif guess < guess_number:
    print("Sorry your guess was too low")    
elif guess == guess_number:
    print("Well done you guessed the number right!") 
