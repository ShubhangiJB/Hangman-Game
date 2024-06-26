from replit import clear
import random
import hangman_art
import hangman_words

#Choose a random word from the hangman_words list.
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

#The player gets 6 chances to guess the word correctly.
end_of_game = False
lives = 6

#Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

#Create blanks for the word
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    if guess in display:
      print("You have already guessed that letter.")
    
    #If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Import the stages from hangman_art.py
    print(hangman_art.stages[lives])
