"""
Write a txt file which has a word in each line like:
Hands
Legs
India
Crow
Rain
...

Write a python code to read the file and store the words in the list

Write a function to guess a word randomly from the list.

Now, write a function which asks user to guess the chosen word letter by letter.
Show "incorrect" message to the wrong guessed letter. 
Display  letters in the clue word that were guessed correctly. 

Let say word is EVAPORATE

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
You left with 5 chances to guess.

>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on.


1)Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
3)When the player wins or loses, let them start a new game.
"""

import random

def read_words_from_file(filename):
    with open(filename, 'r') as file:
        words = [line.strip().upper() for line in file.readlines()]
    return words

def choose_random_word(word_list):
    return random.choice(word_list)

def play_hangman():
    words = read_words_from_file("words.txt")
    while True:
        word_to_guess = choose_random_word(words)
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = 6
        display_word = ['_'] * len(word_to_guess)
        
        print("\n>>> Welcome to Hangman!")
        print(" ".join(display_word))
        
        while incorrect_guesses < max_attempts:
            guess = input("\n>>> Guess your letter: ").upper()
            
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid input! Please enter a single letter.")
                continue
            
            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            
            guessed_letters.add(guess)
            
            if guess in word_to_guess:
                for i, letter in enumerate(word_to_guess):
                    if letter == guess:
                        display_word[i] = guess
                print(" ".join(display_word))
                
                if "_" not in display_word:
                    print("Congratulations! You guessed the word!")
                    break
            else:
                incorrect_guesses += 1
                print("Incorrect!")
                print(f"You have {max_attempts - incorrect_guesses} chances left.")
                print(" ".join(display_word))
                
        if "_" in display_word:
            print(f"You lost! The word was: {word_to_guess}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_hangman()
