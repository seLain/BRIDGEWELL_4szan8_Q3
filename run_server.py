from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/<int:multiplier>/<int:multiplicand>')
def multiply(multiplier, multiplicand):
    # check if multiplier and multiplicand both int
    if isinstance(multiplier, int) and isinstance(multiplicand, int):
        return str(multiplier*multiplicand)
    else:
        return 'Only int is accepted'

if __name__ == '__main__':
    app.run(debug=True)