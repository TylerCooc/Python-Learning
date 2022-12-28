#uses a secret word that continuously takes user input until they get the correct word

secret_word = "meatball" #defined our secret word user is aiming to guess

guesses = "" #empty string to hold all guesses
guess_counter = 0
guess_limit = 3
out_of_guesses = False
lives = 3

while guesses != secret_word and not(out_of_guesses):
    if guess_counter < guess_limit:  
        print("Hint: the secret word is a meat usually used in italian cuisine")
        guesses = input("enter guess: ")
        guess_counter = guess_counter + 1
        if guesses != secret_word:
            lives = lives - 1
            print("You have " + str(lives) + " remaining lives")
            if lives == 0:
                exit
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses and lose")
else:
    print("You guessed the secret word, congratulations")
