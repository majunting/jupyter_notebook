# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
secret_word = 'apple'
letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# letters_guessed = ['i', 'k', 'p', 'r', 's']

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    contain_all_words = True
    for char in letters_guessed:
        if char not in secret_word:
            contain_all_words = False
            break
    return contain_all_words



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    new_str = ""
    for (index, e) in enumerate(secret_word):
        if e not in letters_guessed:
            new_str += "_ "
        else:
            new_str += e
    return new_str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    full_str = string.ascii_lowercase
    for char in letters_guessed:
        full_str = full_str.replace(char, "")
    return full_str

        

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_left = 3
    guesses_left = 6
    guessed = False
    vowels = ['a', 'e', 'i', 'o']
    
    unique_letter_count = 0
    letters_guessed = []
    result = "_ " * (len(secret_word) - 1) + "_"
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have 3 warnings left.")
    print("-----------------")
    while True:
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        user_input = input("Please guess a letter:").lower()
        if not user_input.isalpha() or len(user_input) > 1:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", result)
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left:")
                print("so you lose one guess:", result)
        elif user_input in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have", warnings_left, "warnings left:", result)
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left:")
                print("so you lose one guess:", result)          
        else:
            letters_guessed.append(user_input)
            if user_input not in secret_word:
                if user_input in vowels:
                    guesses_left -= 2
                else:
                    guesses_left -= 1
                print("Oops! That letter is not in my word:", result)
            else:
                result = get_guessed_word(secret_word, letters_guessed)
                print("Good guess:", result)
                unique_letter_count += 1
        print("---------------")
        if "_" not in result:
            guessed = True
            break
        elif guesses_left == 0:
                break
    if guessed:
        print("Congratulations, you won!")
        print("your total score for this game is:", unique_letter_count * guesses_left)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



# additional functions
def get_list_of_letters(word):
    revealed_letters = []
    for letter in word:
        if letter not in revealed_letters and letter != "_":
            revealed_letters.append(letter)
    return revealed_letters



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
        return False
    revealed_letters = get_list_of_letters(my_word)
    
    for index, letter in enumerate(other_word):
        if letter in revealed_letters and letter != my_word[index]:
            return False
        if letter not in revealed_letters and my_word[index] != "_":
            return False
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_word_list = ""
    matched = False
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_word_list += word +" "
            matched = True
    if matched:
        print(matched_word_list[:-1])
    else:
        print("No matches found")



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    warnings_left = 3
    guesses_left = 6
    guessed = False
    vowels = ['a', 'e', 'i', 'o']
    
    unique_letter_count = 0
    letters_guessed = []
    result = "_ " * (len(secret_word) - 1) + "_"
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have 3 warnings left.")
    print("-----------------")
    while True:
        print("You have " + str(guesses_left) + " guesses left.")
        print("Available letters: " + get_available_letters(letters_guessed))
        user_input = input("Please guess a letter:").lower()
        if user_input == '*':
            print(result)
            show_possible_matches(result)
        elif not user_input.isalpha() or len(user_input) > 1:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! That is not a valid letter. You have", warnings_left, "warnings left:", result)
            else:
                guesses_left -= 1
                print("Oops! That is not a valid letter. You have no warnings left:")
                print("so you lose one guess:", result)
        elif user_input in letters_guessed:
            if warnings_left > 0:
                warnings_left -= 1
                print("Oops! You've already guessed that letter. You have", warnings_left, "warnings left:", result)
            else:
                guesses_left -= 1
                print("Oops! You've already guessed that letter. You have no warnings left:")
                print("so you lose one guess:", result)          
        else:
            letters_guessed.append(user_input)
            if user_input not in secret_word:
                if user_input in vowels:
                    guesses_left -= 2
                else:
                    guesses_left -= 1
                print("Oops! That letter is not in my word:", result)
            else:
                result = get_guessed_word(secret_word, letters_guessed)
                print("Good guess:", result)
                unique_letter_count += 1
        print("---------------")
        if "_" not in result:
            guessed = True
            break
        elif guesses_left == 0:
                break
    if guessed:
        print("Congratulations, you won!")
        print("your total score for this game is:", unique_letter_count * guesses_left)
    else:
        print("Sorry, you ran out of guesses. The word was", secret_word)

    

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
