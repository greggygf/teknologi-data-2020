from belajardasar import BelajarDasar


def main():
    belajar = BelajarDasar()

    # Relative path, ke file yang akan dicek
    alamat_file = '../Resources/text_file.txt'

    # Cek keberadaan file
    belajar.cek_file(alamat_file)

    # Membaca isi file
    belajar.baca_file(alamat_file)

    # Menulis isi file
    file_tulis = '../Resources/tes_tulis.txt'
    belajar.tulis_file('Ayam Krispi', file_tulis)

    # # Membaca konten suatu URL
    # url = 'http://twitter.com'
    # belajar.baca_url(url)

    # Menyimpan konten suatu URL ke dalam file
    url = 'http://google.com'
    file_simpan_konten_url = '../Resources/konten_url_2.html'
    belajar.simpan_konten_url(url,file_simpan_konten_url)

main()
