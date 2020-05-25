import io
from flask import Flask, Response
from belajarkmeans import BelajarKMeans
from matplotlib.backends.backend_agg import FigureCanvasAgg # Untuk mengkonversi gambar grafik ke dalam png

app = Flask(__name__)


@app.route('/')
# Tampilan Utama di Web
def index():
    return f"""
    <h1> Ujian Akhir Semester - Teknologi Data </h1>
    <h3> Greggy Gianini Firmansyah</h3>

    <img src="/img.png" alt="grafik" height="700">
    """


@app.route("/img.png")
def img_png():
    bkm = BelajarKMeans('resource/data_nasabah_asuransi_crawling.csv')
    bkm.load_data()
    # bkm.scatter_plot()
    bkm.buat_cluster()
    figure = bkm.scatter_web()  # Objek Gambar

    output = io.BytesIO()  # Membuat objek BytesIO dan menulis beberapa data byte di dalamnya.
    FigureCanvasAgg(figure).print_png(output)  # Mengkonversi gambar grafik dalam bentuk png.
    return Response(output.getvalue(), mimetype="image/png")  # Mengembalikan gambar png.


if __name__ == '__main__':
    import webbrowser

    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
