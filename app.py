from flask import Flask, render_template, url_for, request, flash

app = Flask('__name__')
app.config['SECRET_KEY'] = 'SKJAHcgclugscKZcnisijd'
menu = [{'name': 'Setup', 'url': 'install'},
        {'name': 'First app', 'url': 'first-app'},
        {'name': 'Feedback', 'url': 'feedback'}]


@app.route('/')
def index():
    print(url_for('index'))
    return render_template('index.html', title="Diary", menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='Personal page')


@app.route('/feedback', methods=['POST', 'GET'])
def feedback():
    if request.method == 'POST':
        print(request.form['username'])
        if len(request.form['username']) > 2:
            flash('Massage send', category='success')
        else:
            flash('error', category='error')
    return render_template('feedback.html', title='feedback', menu=menu)


# with app.test_request_context():
#    print(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
