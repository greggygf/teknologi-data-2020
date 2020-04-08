# Komentar
# Satu Baris, pakai kres

"""
Ini adalah komentar
1. Baris satu
2. Baris dua
"""

# Variabel
# adalah named storage, yang artinya penyimpanan yang diberi nama
# Variabel di Python bersifat dynamic typing, yang artinya tidak perlu menyebutkan tipe data
# Contoh yang lain adalah bahasa PHP, typescript, dll

# Lawan dari dynamic typing adalah static typing
a = 'Hello' # Tipe datanya String
b = 1       # Tipe datanya Integer
c = 1.0     # Tipe datanya float, dst.

# Setiap perintah diakhiri dengan "enter" bukan titik koma ";"

# Operasi Variabel
# Menggabungkan 2 String itu cukup dengan tanda +

halo = 'Hello '
dunia = 'World'

# gabung = halo + dunia
# print(gabung) # Cara run project ini adalah dengan klik kanan lalu Run project atau bisa dengan shortcut CTRL+SHIFT+F10

# Gabungan 2 variabel dengan beda tipe data
tahun = 'Sekarang tahun: '
dua_ribu = 2000

# gabung = tahun + dua_ribu
# print(gabung)

# Untuk mengoperasikan 2 buah variabel atau lebih, maka tipe datanya harus sesuai
# Gunakan fungsi str() untuk mengubah suatu tipe data menjadi String

dua_ribu = 2000
gabung = tahun + str(dua_ribu)
print(gabung)

# ada 2 literal untuk string:
# 1. Karakter petik satu (')
# 2. Karakter petik dua (")
# Apa bedanya? Kenapa ada 2?
# Gunanya untuk mempermudah apabila ada tanda petik di dalam string

contoh = 'Dia berkata, "Python itu mudah!"'
print(contoh)

# Memformat string
nama= 'Test'
nim = 123
sql = "SELECT * FROM mahasiswa WHERE nama = '' AND NIM = 123;"
print(sql)

# Kalau tidak pakai format
sql = "SELECT * FROM mahasiswa WHERE nama = '" + nama + "' AND NIM = " + str(nim) + ";"
print(sql)

# Kalau pakai format
nama = "Tes Format"
nim = 999000
sql = "SELECT * FROM mahasiswa WHERE nama = '{}' AND NIM = {}".format(nama,nim)
print(sql)

# Mengambil input dari user
# Dilakukan dengan menggunakan fungsi input()
# nama_user = input('Masukkan nama anda: ')
# print("nama anda adalah : {}".format(nama_user))

# Mengetahui panjang karakter suatu string
# Dapat menggunakan fungsi len()
panjang_nama = len('Greggy Gianini Firmansyah')
print('Panjang nama anda adalah {} karakter'.format(panjang_nama ))