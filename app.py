from flask import Flask

import random

app = Flask(__name__)


@app.route("/")
def homepage():
    """shows a greeting to the user"""
    return "Are you there, world? It's me, Ducky!"


@app.route("/animal/<users_animal>")
def favourite_animal(users_animal):
    """Display a message to the user that changes based on their favourite animal."""
    return f"Wow, {users_animal} is my favourite animal, too!"


@app.route("/dessert/<users_dessert>")
def favourite_dessert(users_dessert):
    """Display a message to the user that changes based on their favourite dessert"""
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<noun>")
def madlibs(adjective, noun):
    """Display a story using the user choices"""
    return f"Poor thing, are you feeling {adjective}? Why don't you go lay on the {noun} and get some rest."


@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """Multiply user's numbers and display the result"""
    if number1.isdigit() and number2.isdigit():
        return f"{number1} times {number2} is {int(number1) * int(number2)}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"


@app.route("/sayntimes/<word>/<n>")
def say_n_times(word, n):
    """Repeat the word by the times the user chooses"""
    if word.isalpha() and n.isdigit():
        return f"{word} " * int(n)
    else:
        return "Invalid input. Please try again by entering a word and a number!"


@app.route("/dicegame")
def dicegame():
    """Chooses a random number from 1 to 6. If the user rolls a 6, they win the game; otherwise, they lose."""
    dice_face = random.randint(1, 6)
    if dice_face == 6:
        return f"You rolled a {dice_face}. You won!"
    else:
        return f"You rolled a {dice_face}. You lost!"


if __name__ == "__main__":
    app.run(debug=True, port=3000)
