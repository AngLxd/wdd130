secret_word = "orange"
guess_count = 0

while True:
    guess = input("Type to guess: ").lower()
    guess_count += 1
    #hi
    if guess == secret_word:
        print("You Guessed The Secret Word, Congratulations!")
        break
    else:
        print("Your guess was not correct.")
        print(f"It took you {guess_count} guesses.")
