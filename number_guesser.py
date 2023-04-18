import random

def check_digit(num):
    if num.isdigit():
        return int(num)
    else:
        return False

top_of_range = input("Type a number to be Maximum:  ")
guess_count = 0
user_guess = -1

top_of_range = check_digit (top_of_range)
if top_of_range is not False:
    if top_of_range <= 0:
        print("Please type number larger than 0 next time.\n")
        quit()
else:
    print("Please type a number next time.\n")
    quit()


random_number = random.randint(0,top_of_range)


while user_guess != random_number:
    guess_count +=1
    user_guess = input("Make a Guess:  ")
    user_guess=check_digit(user_guess)

    if user_guess is False:
        print("Please type a number next time.\n")
        continue
    elif user_guess > random_number:
        print("You were above the number!\n")

    elif user_guess < random_number:
        print("You were below the number!\n")

print("You got it in", guess_count, "guesses.\n")
