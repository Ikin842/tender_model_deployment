from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Ganti path model pickle sesuai dengan lokasi sebenarnya
path_model = 'E:\Semester_7\proposal skripsi\deploy\deployment model tender\model_tender.pkl'
model = pickle.load(open(path_model, 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        status_spse = int(request.form['status_spse'])
        sumber_dana = int(request.form['sumber_dana'])
        k_l_pd = int(request.form['k_l_pd'])
        jenis_tender = int(request.form['jenis_tender'])
        metode_pengadaan = int(request.form['metode_pengadaan'])
        metode_pemilihan = int(request.form['metode_pemilihan'])
        metode_evaluasi = int(request.form['metode_evaluasi'])
        tahun_anggaran = int(request.form['tahun_anggaran'])
        nilai_pagu = float(request.form['nilai_pagu'])
        cara_bayar = int(request.form['cara_bayar'])
        kualifikasi = int(request.form['kualifikasi'])
        jumlah_peserta = int(request.form['jumlah_peserta'])


        # Create the input data array with transformed variables
        input_data = np.array([status_spse, sumber_dana, k_l_pd, jenis_tender, metode_pengadaan, metode_pemilihan,
                               metode_evaluasi, tahun_anggaran, nilai_pagu, cara_bayar, kualifikasi, jumlah_peserta
                               ]).reshape(1, -1)
        prediction = model.predict(input_data)

        return render_template('index.html', prediction_result=prediction)

    # Jika request adalah GET (misalnya, saat Anda pertama kali mengakses halaman)
    return render_template('index.html', prediction_result='')

if __name__ == '__main__':
    app.run(debug=True)