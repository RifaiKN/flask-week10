from flask import Flask, render_template, request, redirect
import random
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
from fibonacci import get_fibonacci_sequence
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
from csv2json import tampilkan_data
@app.route('/getjson')
def csvtojson():
    return tampilkan_data()

# Route untuk Form - Nomor 4
import csv
@app.route('/form/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        try:
            nama = request.form['nama']
            email = request.form['email']
            pesan = request.form['pesan']

            # Simpan data ke file forms.csv
            with open('static/forms.csv', 'a', newline='') as csvfile:
                fieldnames = ['Nama', 'Email', 'Pesan']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                # Tulis data ke file CSV
                writer.writerow({'Nama': nama, 'Email': email, 'Pesan': pesan})

            return redirect('/hasilform/')  # Redirect ke halaman /hasilform/

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template('form.html')


@app.route('/hasilform/')
def hasil_form():
    # Baca data dari file forms.csv
    with open('static/forms.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    return render_template('hasilform.html', data=data)

# Laman Kerang Ajaib

kalimat = [
    "Iya, jalani langkah-langkahmu dengan keyakinan.",
    "Tidak, cuaca mungkin akan mengejutkanmu.",
    "Bergantung pada intuisimu, mungkin baik untuk mendengarkan teman.",
    "Cinta sejati seperti gelombang laut yang datang dan pergi.",
    "Rencanamu mungkin sukses, tetapi semuanya tergantung pada usahamu.",
    "Keberuntungan seringkali hadir kepada yang bersiap.",
    "Cobalah hal baru, dan lihatlah apa yang terjadi.",
    "Mungkin, tetapi pertemuan istimewa memerlukan waktu.",
    "Ya, saatnya mengambil risiko dan melangkah maju.",
    "Ada kemungkinan petualangan menarik menanti di depanmu."
]

@app.route('/formkerangajaib')
def form_kerang():
    return render_template('formskerang.html')

@app.route('/kerangajaib/', methods=['GET', 'POST'])
def kerangajaib():
    if request.method == 'POST':
        name = request.form.get('nama')
        sentence = f"Selamat datang, {name}, anda berhasil masuk ke Puja Kerang Ajaib"
        return render_template('kerangajaib.html', sentence=sentence)
    elif request.method == 'GET':
        name = request.args.get('nama')
        if not name:
            sentence = random.choice(kalimat)
        else:
            sentence = f"{name.capitalize()}, {random.choice(kalimat).lower()}"
        return render_template('kerangajaib.html', sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)
    