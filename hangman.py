import random
from words import list


# Function to choose a random word and makes it upper case
def choose_word():
    word = random.choice(list).upper()
    return word


# Function to add points after a win
def add_point(points):
    points += 1
    return points


# Function that contains the hangman display according to the lives left
def display(lives):
    state = [  # Lives = 0 : head, body, both arms, and both legs
        """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |     / \\
                   |
                 -----
                """,
        # Lives = 1 : head, body, both arms, and one leg
        """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |     / 
                   |
                 -----
                """,
        # Lives = 2 : head, body, and both arms
        """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |  
                   |    
                 -----
                """,
        # Lives = 3 : head, body, and one arm
        """
                   ________
                   |      |
                   |     \\O
                   |      |
                   | 
                   |    
                 -----
                """,
        # Lives = 4 : head and body
        """
                   ________
                   |      |
                   |      O
                   |      |
                   |
                   |     
                 -----
                """,
        # Lives = 5 : head
        """
                   ________
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 -----
                """,
        # Lives = 6 : initial state
        """
                   ________
                   |      |
                   |      
                   |    
                   |      
                   |     
                 -----
                """
    ]
    return state[lives]


# Function to update spaces variables when a letter was guessed correctly
def update_spaces(word, guess, spaces):
    # Create new list to store spaces string
    new_spaces = []

    # Convert spaces to a list
    new_spaces[:] = spaces

    # Find where is the letter in the word
    for i in range(len(word)):
        if word[i] == guess:
            # Change empty space for letter guessed
            new_spaces[i] = guess

    # Updates spaces to show letter guessed
    spaces = "".join(new_spaces)

    return spaces


# Function that determines the letters input by user
def play(word, points, rounds):
    # Shows empty spaces
    spaces = "_" * len(word)

    # Keep track of status of the game
    win = False

    # Stores the letters input by user
    guessed_letters = []

    # Number of lives
    lives = 6
    if rounds == 1:
        print("Welcome to HANGMAN")
    print(display(lives))
    print(spaces)

    # While user haven't won and has lives left
    while not win and lives > 0:
        guess = input("Enter a letter: ").upper()

        # Check if input is a letter
        if guess.isalpha():

            # If input was more than one letter
            if len(guess) > 1:
                print("Please enter one letter at a time")

            # Let user know if they already guessed given letter
            elif guess in guessed_letters:
                print("You already guessed this letter")

            # If letter guessed is not in word
            elif guess not in word:
                print(guess, "is not in the word")
                guessed_letters.append(guess)
                lives -= 1

            # Letter guessed is in the word
            else:
                print(guess, " is in the word! (:")
                guessed_letters.append(guess)
                spaces = update_spaces(word, guess, spaces)

                # Check if user has won after correct guess
                if "_" not in spaces:
                    win = True

        # Given input is not a letter
        else:
            print("Please enter a letter")

        print(display(lives))
        print(spaces)

        # Let user know how many tries he/she are left
        if lives > 0 and not win:
            print("Number of tries left: " + str(lives))

    # When user wins
    if win:
        print("YOU WIN")
        points = add_point(points)
        print("Total points: " + str(points))

    # When user loses
    else:
        print("YOU LOSE, the word was " + word)
        print("Total points: " + str(points))

    again = input("Play Again? (Y/N) ").upper()
    if again == "Y":
        rounds += 1
        print("___________________________")
        print("Round: " + str(rounds))
        play(choose_word(), points, rounds)

    else:
        print("___________________________")
        print("Thanks for playing! Bye (:")


def main():
    points = 0
    rounds = 1
    word = choose_word()
    play("BEE", points, rounds)


if __name__ == "__main__":
    main()
