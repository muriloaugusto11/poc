from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if name == '' or email == '':
            return redirect(url_for('index'))
        return render_template('success.html', name=name, email=email)

if __name__ == '__main__':
    app.run(debug=True)
