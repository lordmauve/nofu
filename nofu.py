import random
from flask import Flask, render_template, abort, redirect, request


app = Flask(__name__)


questions = [{
    'question': 'How many shillings were there in a pre-decimalisation pound?',
    'answer': '20',
    'red_herrings': [
        '5',
        '10',
        '20',
        '25',
        '50',
        '120',
    ]
}]


@app.route('/')
def index():
    q = random.randint(0, len(questions) - 1)
    return redirect('/q/%d/' % q)


@app.route('/a/<int:id>/')
def answer(id):
    try:
        question = questions[id]
    except IndexError:
        abort(404)

    answer = request.args['a']
    return render_template('answer.html', question=question,
                           is_correct=(answer == question['answer']))


@app.route('/q/<int:id>/')
def question(id):
    try:
        question = questions[id]
    except IndexError:
        abort(404)

    red_herrings = random.sample(question['red_herrings'], 3)
    answers = red_herrings + [question['answer']]
    random.shuffle(answers)
    return render_template(
        'question.html',
        id=id,
        question=question['question'],
        answers=answers
    )


if __name__ == '__main__':
    app.run(debug=True)
