from os import path # untuk mengecek file
from urllib.request import urlopen # Untuk terhubung ke internet
import ssl

class BelajarDasar(object):

    # ---------------------
    # Bagian-1: Operasi File
    # ----------------------

    # 1. Mengecek apakah suatu file ada atau tidak
    def cek_file(self, alamat_file:str):
        # Mengecek dilakukan dengan menggunakan fungsi path.exists()
        # Impor os.path
        print('Mengecek file: {}'.format(alamat_file))
        ada = path.exists(alamat_file)
        if(ada):
            print('File ada!')
        else:
            print('File tidak ada!')
        return ada

    # 2. Membaca file teks
    def baca_file(self, alamat_file: str):
        # Dapat menggunakan fungsi open() bawaan Python
        # r artinya read atau membaca, selain itu ada 'w' yaitu write atau menulis dan 'a' yaitu append atau menambahkan
        # ada juga 'r+' yaitu untuk membuat file jika belum ada
        f = open(alamat_file, 'r')
        teks_isi = f.read()
        print('Isi dari file adalah:')
        print(teks_isi)
        return teks_isi

    # 3. Menulis ke file
    # Menggunakan fungsi open(), tetapi dengan mode penulisan (w/w+)
    def tulis_file(self, teks:str, alamat_file:str):
        # Buat handler
        f = open(alamat_file, 'w+') # Lebih baik menggunakan w+, karena jika tidak ada file maka akan otomatis dibuatkan file tersebut.
        # Tulis teksnya ke file
        f.write(teks)
        print('Berhasil menulis ke file: {}'.format(alamat_file))

    # ---------------------
    # Bagian-2: Operasi Internet
    # ----------------------

    # 1. Membaca konten suatu URL
    def baca_url(self, alamat_url: str):
        # Antisipasi jika servernya tidak mendukung SSL yang terverifikasi
        # Untuk kasus semacam itu, kita bisa membuat urllib supaya 'mengabaikan' SSL
        setting_ssl = ssl.create_default_context() # Import library ssl
        setting_ssl.check_hostname = False
        setting_ssl.verify_mode = ssl.CERT_NONE

        # Digunakan library urllib
        response = urlopen(alamat_url, context=setting_ssl)
        konten = response.read() # Disini html-nya masih berupa bytes
        # konversi bytes ke str
        teks = konten.decode('utf-8')
        print('Konten dari URL {} adalah:'.format(alamat_url))
        print(teks)
        return teks

    # 2. Menulis/menyimpan respon yang didapat dari pembacaan konten URL ke file teks di komputer lokal.
    # Apakah bisa? bisa!
    # (Tugas-1)

    def simpan_konten_url(self, alamat_url: str, alamat_file: str):
        teks = self.baca_url(alamat_url)

        # Buat handler
        f = open(alamat_file, 'w+')
        # Tulis teksnya ke file
        f.write(teks)
        print('Berhasil menulis ke file: {}'.format(alamat_file))

    # 3. Untuk menulis ke URL (kirim data via API) caranya juga sama, dengan menggunakan urllib.open(), hanya saja pada data science, kita jarang mengirim data ke internet,
    #    Umumnya kita hanya membaca data saja.

    # ---------------------
    # Bagian-3: Operasi Database
    # ----------------------

    # 1. Menginstall library library database
    #    Untuk konek ke database diperlukan suatu driver, yaitu software pihak ketiga yang menjembatani antara Python