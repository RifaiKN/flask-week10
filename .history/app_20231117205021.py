from flask import Flask, render_template, request

app = Flask(__name__)

# Route untuk homepage
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


if __name__ == "__main__":
    app.run(debug=True)