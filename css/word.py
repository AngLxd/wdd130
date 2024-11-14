secret_word = "orange"
guess_count = 0

while True:
    guess = input("Welcome to Wordle! Type to guess the secret six letter word: ").lower()

    if len(guess) != len(secret_word):
        print("Your guess must have the same number of letters as the secret word (6 letters).")
        continue

    guess_count += 1

    if guess == secret_word:
        print("You Guessed The Secret Word, Congrats!!")
        break
    else:
        hint = ""
        for i in range(len(secret_word)): #<--- The program will check the letter in both the guess and secret_word by separating each letter and assigning a value to each letter
            if guess[i] == secret_word[i]: #<--- If the guess is for example: "apple" and the secret word is "amber" the "if" condition would add "A " to the hint for the first position because the first letter matched
                hint += guess[i].upper() + " " #<---If the guess is correct for that position, it adds the character in uppercase
            elif guess[i] in secret_word: #<--- If the guess someone types is "apple" and the secret word is "orange", it will add "a " to the hint because p is in the word but in the wrong position
                hint += guess[i].lower() + " " #<--- If the guess is correct but the position is different it adds a lowercase
            else:
                hint += "_ " #<--- means that the letter in that space is not found in the "secret word" leaving an empty space in that spot "_"
        
        print(f"Your hint is: {hint.strip()}") #<--- : This line prints the hint for the user, showing which letters match the secret word
        print(f"It took you {guess_count} guesses.")