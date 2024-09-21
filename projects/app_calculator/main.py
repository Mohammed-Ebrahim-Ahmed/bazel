from flask import Flask
from random import randint

from projects.calculator.calculator import calculator

app = Flask(__name__)
my_calculator = calculator()


@app.route('/')
def hello():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    message = "{} + {} = {}".format(num1, num2, my_calculator.add(num1, num2))
    return message

if __name__ == "__main__":
    app.run()