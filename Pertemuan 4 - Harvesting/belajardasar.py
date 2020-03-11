from os import path # untuk mengecek file
from urllib.request import urlopen # Untuk terhubung ke internet
import ssl
import mysql.connector # Harus dipasang dulu drivernya di project kita
from mysql.connector.connection import MySQLConnection

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
    #    Untuk konek ke database diperlukan suatu driver, yaitu software pihak ketiga yang menjembatani antara Python dan database yang ingin diakses.
    #    Masing-masing vendor database, memiliki drivernya sendiri
    #    Misal MySQL, nama drivernya: mysql.connector
    #    SQLite beda lagi, SQL Server beda lagi, Oracle juga..
    #    Driver harus didownload dulu, dan dipasang pada project kita. Jika belum, maka library-nya tidak akan bisa di-impor
    #    Cara impor: Settings -> Preferences -> Projects -> Project Interpreter -> Tanda [+] -> Cari: mysql-connector -> Install
    #    Screenshot langkah-langkahnya!

    # 2. Persiapkan koneksi ke server MySQL. Di sana buatlah 1 tabel:
    #    mahasiswa (nim, nama, telepon)
    '''     CREATE DATABASE belajar_data_science;
            USE belajar_data_science;
            CREATE TABLE mahasiswa
            (
                nim INTEGER PRIMARY KEY AUTO_INCREMENT,
                nama VARCHAR(255),
                telepon VARCHAR(20)
            );
    '''

    # 3. Membuat koneksi ke server MySQL
    def konek_mysql(self, nama_db: str):
        # Koneksi dibuat dengan fungsi mysql.connector.connect()
        # Akan mengembalikan sebuah objek dari class:
        # mysql.connector.connection.MySQLConnection

        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database=nama_db
        )
        print(db)
        # Objek koneksi ini nantinya selalu digunakan saat melakukan operasi baca/tulis ke database
        return db

    # 4. Menambahkan data ke tabel
    #    Import dulu mysql.connector.connection.MySQLConnection terlebih dahulu
    def tambah_mahasiswa(self, koneksi: MySQLConnection, nama: str, telepon: str):
        # INSERT INTO mahasiswa (nama, telepon) VALUES ('Greggy', '0000')
        # Susun SQL (embedded query)
        sql = "INSERT INTO mahasiswa (nama, telepon) VALUES ('{}', '{}')".format(nama, telepon)
        # Untuk mengeksekusi SQL tersebut diperlukan cursor
        # cursor adalah semacam penanda, yang menunjuk ke tabel yang sedang diakses saat ini.
        # Cursor didapat dari objek koneksi.
        kursor = koneksi.cursor()
        kursor.execute(sql)
        # Tanpa 1 baris ini perubahan di db tidak akan diterapkan!
        koneksi.commit()
        print('Data berhasil ditambahkan!')

    # 5. Mengubah data ke tabel
    def edit_mahasiswa(self, koneksi: MySQLConnection, nim: int, nama: str, telepon: str):
        # UPDATE mahasiswa SET nama = 'Ayam Bakar', telepon = '09999' WHERE nim = 2
        sql = "UPDATE mahasiswa SET nama = '{}', telepon = '{}' WHERE nim = {}".format(nama, telepon, nim)

        kursor = koneksi.cursor()
        kursor.execute(sql)
        koneksi.commit()
        print('Data berhasil diedit!')

    # 6. Menghapus data dari tabel
    def delete_mahasiswa(self, koneksi: MySQLConnection, nim: int):
        # DELETE FROM mahasiswa WHERE nim = ...
        sql = "DELETE FROM mahasiswa WHERE nim = {}".format(nim)

        kursor = koneksi.cursor()
        kursor.execute(sql)
        koneksi.commit()
        print('Data berhasil dihapus!')

    # 7. Membaca data (SELECT) dari tabel
    def pilih_mahasiswa(self, koneksi: MySQLConnection, where: str = None): # default parameter value, artinya parameter 'where' tersebut boleh diisi ataupun tidak diisi.
        # Siapkan dulu SQL
        sql = "SELECT * FROM mahasiswa"
        if where is not None:
            sql += " WHERE {}".format(where)

        # Eksekusi lewat kursor
        kursor = koneksi.cursor()
        kursor.execute(sql)
        # Tidak perlu menggunakan commit, karena hanya membaca data bukan mengubah data.
        # Yang perlu adalah fetchall()
        data = kursor.fetchall()
        '''
        [
            0 => [1, 'Adi', '1010931'],
            1 => [2, 'Budi', '0283823'],
            ...
            dst
        ]
        '''
        return data