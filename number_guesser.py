import random
top_of_range = input("Type a number to be Maximum:  ")
guess_count = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type number larger than 0 next time.\n")
        quit()

else:
    print("Please type a number next time.")


random_number = random.randint(0,top_of_range)

while True:
    guess_count +=1
    user_guess = input("Make a Guess:  ")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Please type a number next time.\n")
        continue

    if user_guess == random_number:
        print("You got it!")
        break

    elif user_guess > random_number:
        print("You were above the number!\n")

    else:
        print("You were below the number!\n")

print("You got it in", guess_count, "guesses.\n")
