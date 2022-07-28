import os
from random import choice
from string import ascii_lowercase


FILENAME = 'sowpods.txt'


def get_guess_word(filename) -> str:
    """Get word from data/sowpods.txt"""
    with open(filename, 'r') as f:
        return choice([x.strip() for x in f]).lower()


def print_game(wrong, word, letters) -> None:
    """Draw template in terminal for game"""
    print('\nWrong guess:', ', '.join(wrong))
    for i in letters:
        if i is None:
            print(' ', end=' ')
        else:
            print(i, end=' ')
    print()
    for i in word:
        if i != ' ':
            print('-', end=' ')
        else:
            print(' ', end=' ')
    print()


def get_letter(attempt, guess) -> str:
    """Get user input as letter"""
    user_input = input(f'> Guess a letter ({attempt} attempts left): ').lower()
    if len(user_input) != 1 or user_input not in ascii_lowercase:
        print("> Please input a letter!")
    elif user_input in guess:
        print(f"> You have guessed '{user_input}' before")
    else:
        return user_input


def play(word) -> None:
    """Game logic"""
    attempt = 6
    guess, guess_wrong = [], []
    letters = []
    for i in word:
        i = None if i != ' ' else i
        letters.append(i)
    while attempt > 0:
        print_game(guess_wrong, word, letters)
        if None not in letters:
            print('> You win!')
            break
        user_letter = get_letter(attempt, guess)
        if user_letter is not None:
            for i in range(len(word)):
                if user_letter == word[i]:
                    letters[i] = user_letter
            guess.append(user_letter)
            if user_letter not in letters:
                guess_wrong.append(user_letter)
                attempt -= 1
    else:
        print_game(guess_wrong, word, letters)
        print('> You lose...')
        print(f'> Answer: {word.capitalize()}')


if __name__ == "__main__":
    word = get_guess_word(os.path.join('data', FILENAME))
    play(word)
