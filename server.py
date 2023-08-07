from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
rand_num = random.randint(0, 10)
print(rand_num)


def check_guess(guess):
    """
    Function to check if the guess is higher, lower or equal to the randomly generated number.
    Args:
        guess (int): The guessed number.

    Returns:
        str: A string indicating if the guess was too high, too low, or correct.
    """
    if guess > rand_num:
        return 'Too high, try again!'
    elif guess < rand_num:
        return 'Too low, try again!'
    else:
        return 'You found me!'


@app.route('/')
def index():
    """
    Function to serve the main page.

    Returns:
        str: HTML for the main page.
    """
    return ('<h1 style="text-align: center">Guess a number between 1 and 10 </h1> '
            '<img style="display: block; margin-left: auto; margin-right: auto;" '
            'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>')


@app.route('/<int:guess>')
def guess_number(guess):
    """
    Function to serve a page with feedback on the user's guess.

    Args:
        guess (int): The user's guess.

    Returns:
        str: HTML with feedback on the guess.
    """
    return f'<h1 style="text-align: center">{check_guess(guess)}</h1>'


if __name__ == "__main__":
    app.run(debug=True)
