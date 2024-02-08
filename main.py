from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/<prof>')
@app.route('/training/<prof>')
def index1(prof):
    return render_template('training.html', prof=prof)



if __name__ == '__main__':
    app.run(port=8001, host='127.0.0.1')
