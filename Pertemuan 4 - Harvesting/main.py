from belajardasar import BelajarDasar


def main():
    belajar = BelajarDasar()

    # # Menyimpan konten suatu URL ke dalam file
    # url = 'http://google.com'
    # file_simpan_konten_url = '../Resources/konten_url_2.html'
    # belajar.simpan_konten_url(url, file_simpan_konten_url)

    # # Mengedit data di table

    # belajar.edit_mahasiswa(db, nim=2, nama='Ayam Asam Manis',telepon='0000')

    # Menghapus data di table
    db = belajar.konek_mysql(nama_db='belajar_data_science')
    belajar.delete_mahasiswa(db, nim=2)

    # Menambahkan 1 baris baru ke table

    # # belajar.tambah_mahasiswa(koneksi=db, nama='Ayam Goreng', telepon='0817373')
    #
    # # Menampilkan data mahasiswa dari table
    # semua_mahasiswa = belajar.pilih_mahasiswa(koneksi=db, where='nim=1')
    # print('-------------------------')
    # for mahasiswa in semua_mahasiswa:
    #     nim = mahasiswa[0]
    #     nama = mahasiswa[1]
    #     telepon = mahasiswa[2]
    #     print('NIM : {}'.format(nim))
    #     print('Nama : {}'.format(nama))
    #     print('Telepon : {}'.format(telepon))
    #     print('-------------------------')


    # # Membaca konten suatu URL
    # url = 'http://twitter.com'
    # belajar.baca_url(url)


    # # Menulis isi file
    # file_tulis = '../Resources/tes_tulis.txt'
    # belajar.tulis_file('Ayam Krispi', file_tulis)

    # # Relative path, ke file yang akan dicek
    # alamat_file = '../Resources/text_file.txt'

    # # Membaca isi file
    # belajar.baca_file(alamat_file)

    # # Cek keberadaan file
    # belajar.cek_file(alamat_file)
    #



    #
    # # Coba menghubungkan ke database
    # # Kedua baris pemanggilan fungsi dibawah akan menghasilkan output yang sama
    # # hanya penulisannya saja yang berbeda.
    # db = belajar.konek_mysql('belajar_data_science')
    # db = belajar.konek_mysql(nama_db='belajar_data_science')
    #
    #

    #
    # # Menghapus data di table
    # # belajar.delete_mahasiswa(db, nim=2)
    #

main()
