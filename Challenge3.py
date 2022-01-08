print("Welcome to our phenomenal hangman game!!")
#takes user input to define the word player 2 needs to guess
word = input("Player 1, please enter a word: ")
#takes user input to define the number of guesses player 2 gets
numOfGuesses = input("Player 1, how many guesses would you like to give player 2? ")

#sets up variables for the game
wordNotGuessed = True
lives = int(numOfGuesses)
blanks = ["_ "] * len(word)

while wordNotGuessed:
    print("")
    letterGuessed = input("Please guess a letter: ")
    while letterGuessed.isalpha() == False:
        print("Invalid guess.")
        letterGuessed = input("Please guess a valid letter: ")
    letterInWord = False
    for indexOfWord in range(len(word)):
        if letterGuessed == word[indexOfWord]:
            blanks[indexOfWord] = str(letterGuessed) + " "
            letterInWord = True
    
    if letterInWord != True:
        lives = lives - 1
        print("Incorrect guess. Letter is not in the word :(")
    else:
        print("Correct guess! :)")

    print("WORDS: ", end = '')
    for letter in blanks:
        print(letter, end = '')
    print("")
    print("GUESSES LEFT: " + str(lives))
    
    wordGuessed = True
    for indexOfGuess in range(len(blanks)):
        if "_ " == blanks[indexOfWord]:
            wordGuessed = False
            
    if wordGuessed:
        wordNotGuessed = False
        print("Hooray, you've won!")
    if lives <= 0:
        wordNotGuessed = False
        print("Aww, you lost.")