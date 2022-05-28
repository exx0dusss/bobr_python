import random

guess_number = random.randint(1,101)
want_to_play = True

print("Number game.")
print("I guess number. Try to guess it")

while want_to_play:
    player_number = int(input("Enter your variant > "))
    if player_number == guess_number:
        print("You win!!!")
        user_input = input("Want to play again ? (yes/no)")
        if user_input == "no" or user_input == "N":
            print("Goodbye !")
            want_to_play = False
        else:
            guess_number = random.randint(1,101)
            print("I guess new number. Try to guess it")
    elif player_number < guess_number:
        print("My number is greater")
    elif player_number > guess_number:
        print("My number is less")