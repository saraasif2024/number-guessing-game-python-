import random 

print(
"Welcom to the number guessing game! \n You have 5 attempts to guess the number between 50 and 100 ,  let's get started!")

number_to_guess = random.randrange(50, 100)

chances = 5

guess_counter = 0 

while guess_counter <  chances:
    guess_counter += 1
    my_guess = int(input("Enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you guessed it right!! in the {guess_counter}attempt")
        break
    elif guess_counter >= chances and  my_guess != number_to_guess:
        print(f"Sorry, you have guessed wrong number. The number was {number_to_guess} better luck next time!")

    elif my_guess < number_to_guess:
        print("Your guess is too low, try again bro!")

    elif my_guess > number_to_guess:
        print("Your guess is too high, try again bro!")    

