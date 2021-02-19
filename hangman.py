#Creating an Hangman game
import random
from words import words_list #importing words from a list of words

def get_word():
    word = random.choice(words_list) #taking a random choice word
    return word.upper()


def play(word):
    word_completeion = "-" * len(word)
    guessed = False
    guessed_letters = [] 
    guessed_words = []
    tries = 6 #defining tries at first then will be reducing count 1 by 1
    print("Let's play Hangman!!")
    print(display_hangman(tries))
    print(word_completeion)
    print("\n")
    while not guessed and tries > 0:
        guess = input ("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if  guess in guessed_letters :
                print("You already guessed that letter", guess)
            elif guess not in word:
                print(guess, "Not in the Word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good Job", guess, "is in the word!!")
                guessed_letters.append(guess)
                word_as_list = list(word_completeion)
                indices = [i for i,letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completeion = "".join(word_as_list)
                if "-" not in word_completeion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You Already guessed the Word!!")
            elif guess != word :
                print(guess, "is not the word!")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completeion = word

        else:
            print("Not A Valid Guess!!")
        print(display_hangman(tries))
        print(word_completeion)
        print("\n")
    if guessed:
        print("Congradulations, You guessed the word right")
    else:
        print("Sorry, You ran out of tries. The word was  " + word + ". Maybe Next time!!!")




def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Do u want to play again? (Y/N)" ).upper() == "Y" :
        word = get_word()
        play(word)

if __name__== "__main__":
    main()
