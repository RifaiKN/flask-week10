from flask import Flask, render_template, request
from fibonacci import get_fibonacci_sequence
app = Flask(__name__)

# Route untuk homepage - Nomor 1
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/hobi')
def hobi():
    return render_template('hobi.html')

@app.route('/pendidikan')
def pendidikan():
    return render_template('pendidikan.html')

@app.route('/pengalaman')
def pengalaman():
    return render_template('pengalaman.html')

# Route untuk Fibonacci - Nomor 2
@app.route('/fibonacci')
def fibonacci():
    return render_template('fibonacci.html')

# Route untuk CSV2JSON - Nomor 3
app.route('/getjson')
def pengalaman():
    return render_template('getjson.html')

# Route untuk Form - Nomor 4
app.route('/forms')
def pengalaman():
    return render_template('forms.html')

if __name__ == "__main__":
    app.run(debug=True)