import random

top_of_range = input("Type a number: ")  # user type top of the range

if top_of_range.isdigit():  # check if the user wrote number
    top_of_range = int(top_of_range)  # convert the string into a integer

    if top_of_range <= 0: # check if top number is smaller or equ. to a 0
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number.")  # exception
    quit()

random_number = random.randint(0, top_of_range)
counter = 0
while True:
    user_guess = input("Make a guess: ")
    counter += 1  # count every guess
    if user_guess.isdigit():  # check if the user wrote number
        user_guess = int(user_guess)  # convert the string into a integer
    else:
        print("Please type a number.")  # exception
        continue

    if user_guess == random_number:  # check if user guess is = to a computer's number
        print("You got it!")
        break
    else:
        if user_guess > random_number:   # check where is user number about the computer's number
            print("You were above the number!")
        else:
            print("You were below the number!")
print(f"You got it from {counter} guesses!")  # print from how many guesses you got it right


