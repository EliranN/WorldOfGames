from decimal import Decimal

from flask import Flask, render_template

from Utils import SCORES_FILE_NAME

app = Flask(__name__)


def score_server():
    raise FileNotFoundError


@app.route('/')
def index():
    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            for tav in score_file:
                score_list = tav.split(',')
            total_score = sum(Decimal(i) for i in score_list)
            return render_template('home_page.html', score=total_score)
    except FileNotFoundError as e:
        return render_template('error_page.html', ERROR=f'{e.args[1]}')


if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True, port=8080)
