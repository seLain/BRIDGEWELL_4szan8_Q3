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

@app.errorhandler(404)
def page_not_found(e):
    allowed_rules = [rule.rule for rule in app.url_map.iter_rules()]
    err_message = '<br/>'.join([
        'The requested URL can not be found.',
        'Only these URL rules are allowed:',
        '<plaintext>' + str(allowed_rules)
        ])
    return err_message

if __name__ == '__main__':
    app.run(debug=True)