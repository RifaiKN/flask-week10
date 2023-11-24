from flask import Flask, render_template, request
from fibonacci import get_fibonacci_sequence
from csv2json import tampilkan_data
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
@app.route('/fibonacci', methods=['GET', 'POST'])
def fibonacci():
    result = None
    error = None
    if request.method == 'POST':
        try:
            length = int(request.form['length'])
            if length < 0:
                raise ValueError("Deret Fibonacci tidak boleh kurang dari 0")
            result = get_fibonacci_sequence(length)
        except ValueError as e:
            error = str(e)

    return render_template('fibonacci.html', result=result, error=error)

# Route untuk CSV2JSON - Nomor 3
@app.route('/getjson')
def csvtojson():
    return tampilkan_data()

# Route untuk Form - Nomor 4
@app.route('/forms')
def forms():
    return render_template('forms.html')

if __name__ == "__main__":
    app.run(debug=True)