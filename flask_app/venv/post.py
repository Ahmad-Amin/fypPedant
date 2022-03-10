from flask import Flask, render_template, request
from itertools import combinations

app = Flask(__name__)

names = ["saif","aiman", "zargham", "hasan"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        value = request.form.getlist('value', type=str)
        rslt = ' '.join(value)
    
    x = 4
    pairs = combinations(range(1,x), 2)
    return render_template('index.html', **locals())


if __name__ == "__main__":
  app.run(debug=True)