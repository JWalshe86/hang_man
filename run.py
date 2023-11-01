
from ast import main
import os
import random

from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

current_guesses = []
current_message = ''

end_of_game = False


def main():
    """to control flow of the game
    """
    choice = game_entry()
    guess, lives = display_stage(choice)
    what_to_do_with_incorrect_guess_input(guess)
    game_description(choice)
    chosen_word, word_length = get_chosen_word()
    display = guess_management(guess, word_length, chosen_word, lives)
    display = check_guessed_letter(word_length, chosen_word, guess, display)
    play_again = get_play_again_input()
        
def game_entry():
    """function to display game options and returns user input
    """
    print(logo)
    print("Welcome to Hangman Game!")
    # while True:
    print("\nMain Menu:")
    print("1. Start a New Game")
    print("2. Game Description")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")
    return choice

def game_description(choice):
    if choice == '2':   
        print("\nHangman is a word-guessing game where you have to guess a hidden word letter by letter.")
        print("You can make a limited number of incorrect guesses before the hangman is complete.")
        print("Your goal is to guess the word before the hangman is fully drawn.")
        print("Good luck!")

def clear():
    """
    This clears the terminal to prevent clutter on it.
    """
    os.system('cls' if os.name=='nt' else 'clear')

lives = 6

def display_stage(choice):
    clear()
    if choice == '1':
        print(stages[lives])
        # print(f"{' '.join(guesses)}")
        
        guess = input("Guess a letter: ").lower()
        return guess, lives
    
    
def what_to_do_with_incorrect_guess_input(guess):
    if len(guess) == 0:
        print("Guess cannot be empty")
    elif len(guess) > 1:
        print("Guess should not be more than one character!")
    elif not guess.isalpha():
        print("Guess should be a letter")
                
def get_chosen_word():

    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    return chosen_word, word_length


def guess_management(guess, word_length, chosen_word, lives):
            #Create blanks
    display = []
    for _ in range(word_length):
                    display += "_"     
                        
    if guess in current_guesses:
        message = f"You've already guessed {guess}"
        print(message)
    elif guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    if lives == 0:
        end_of_game = True
        current_message = "You lose!"
        print(current_message)
        print("You lose.")
    
    return display

def check_guessed_letter(word_length, chosen_word, guess, display):
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            print("GUESS CORRECT!")
            current_message = "Correct guess!"
            display[position] = letter
            display = letter

    current_guesses.append(guess)
        #Check if user is wrong.
        
            #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

            #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        current_message = "You win!"
        print(current_message)
      
    return display 

# while True:
def get_play_again_input():
    play_again = input("Do you want to play again? Y or N: ").lower()
    return play_again
    

def play_again_managment(play_again):
    if play_again not in ["y", "n"]:
        print("Invalid input!")
    elif play_again == 'y':
        main()
    else:
        print("Thank you for playing Hangman. Goodbye!")

    
    print(stages[lives])

main()

