import hangman
from hangman import *


# Test if word was in fact chosen from list
def test_choose_word():
    word = choose_word()
    assert word.lower() in list


# Function to mock input
def mocker(input_arr):
    guess_input = input_arr.copy()

    def mock_input(s):
        return guess_input.pop(0)

    hangman.input = mock_input


# Test when user wins
def test_win(capsys):
    input_letters = ["b", "e", "n"]
    mocker(input_letters)
    ty =hangman.play("BEE", 0, 1)
    out, err = capsys.readouterr()

    assert " is in the word! (:" in out
    assert "B__" in out
    assert "YOU WIN" in out
    assert "Thanks for playing! Bye (:" in out

# Test if given input was more than a single letter
def test_multiple_letter_guess(capsys):
    multi_guess = ["ae", "b", "e", "n"]
    mocker(multi_guess)
    hangman.play("BEE", 0, 1)
    out, err = capsys.readouterr()

    assert "Please enter one letter at a time" in out
    assert " is in the word! (:" in out
    assert "Thanks for playing! Bye (:" in out


# Test if given input is not a letter
def test_non_alpha_guess(capsys):
    non_alpha_guess = ["4", "@", "b", "e", "n"]

    mocker(non_alpha_guess)
    hangman.play("BEE", 0, 1)
    out, err = capsys.readouterr()
    assert "Please enter a letter" in out
    assert " is in the word! (:" in out
    assert "Thanks for playing! Bye (:" in out


# Test when user loses
def test_lose(capsys):
    wrong_guesses = ["c", "c", "x", "s", "y", "z", "p", "n"]
    mocker(wrong_guesses)
    hangman.play("BEE", 0, 1)
    out, err = capsys.readouterr()
    assert " is not in the word" in out
    assert "You already guessed this letter" in out
    assert "YOU LOSE, the word was BEE" in out
    assert "Thanks for playing! Bye (:" in out


# Test play again option
def test_play_again(capsys):
    two_rounds = ["b", "e", "y", "x", "z", "w", "q", "k", "ñ", "h", "k", "o", "n", "g", "r", "v"]
    mocker(two_rounds)
    hangman.play("BEE", 0, 1)
    out, err = capsys.readouterr()

    assert " is in the word! (:" in out
    assert "YOU WIN" in out
    assert "Round: 2" in out
    assert "YOU LOSE" in out


# Test add_point function
def test_add_points():
    assert add_point(9) == 10
    assert add_point(2) == 3


# Test update_spaces function
def test_update_spaces():
    word = "TEST"
    spaces = "____"
    guess = "E"
    spaces = update_spaces(word, guess, spaces)
    assert spaces == "_E__"

    guess = "T"
    spaces = update_spaces(word, guess, spaces)
    assert spaces == "TE_T"


# Test display() function
def test_display():
    lives = 0
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |     / \\
                   |
                 -----
                """

    lives = 1
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |     / 
                   |
                 -----
                """
    lives = 2
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |     \\O/
                   |      |
                   |  
                   |    
                 -----
                """

    lives = 3
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |     \\O
                   |      |
                   | 
                   |    
                 -----
                """

    lives = 4
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |      O
                   |      |
                   |
                   |     
                 -----
                """
    lives = 5
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |      O
                   |    
                   |      
                   |     
                 -----
                """
    lives = 6
    out = display(lives)
    assert out == """
                   ________
                   |      |
                   |      
                   |    
                   |      
                   |     
                 -----
                """
