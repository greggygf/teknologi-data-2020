# # List sebenarnya adalah Array
#
# # Array pada python bisa campur isinya
#
# nama_hari = ['Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Ahad']
#
# print(nama_hari[0])
#
# # Operasi array :
# # 1. Penambahan elemen
# # 2. Pengambilan elemen (slicing)

# Menambahkan 1 elemen di akhir array
nama_bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei']
# # Jika ingin menambahkan data pada array, gunakan fungsi append(). Fungsi append() untuk menambahkan 1 data
# nama_bulan.append('April')
# print(nama_bulan)

# # Jika menambahkan beberapa elemen di akhir array, maka gunakan fungsi extend() untuk menambahkan beberapa data
# bulan_baru = ['Mei', 'Juni', 'Juli']
# nama_bulan.extend(bulan_baru)
#
# print(nama_bulan)
#
# # Mengambil elemen dari array
#
# # Mengambil salah satu nilai pada index tertentu
# print(nama_bulan[1])
#
# Mengambil nilai pada beberapa index
# print(nama_bulan[-2])
#
# # 2 elemen pertama array
# dua_bulan_pertama = nama_bulan[0:2]
# print(dua_bulan_pertama)
#
# # 2 elemen terakhir array
# dua_bulan_terakhir = nama_bulan[-2:]
# print(dua_bulan_terakhir)
#
# # Panjang array kita gunakan fungsi len()
# panjang_array = len(nama_bulan)
# print(panjang_array)
#
# # Mencari index dari suatu nilai. Digunakan fungsi index()
# index_mei = nama_bulan.index("Mei")
# print(index_mei)
#
# # Perulangan
# # 1. Perulangan yang tidak pedui indexnya
# # 2. Perulangan yang peduli indexnya (pakai for)
# # 3. Perulangan yang peduli indexnya (pakai while)
#
# # Perulangan tidak peduli index
# # Menampilkan setiap nama bulan di console
#
for bulan in nama_bulan:
    print('Sekarang bulan: {}'.format(bulan))

# Perulangan memperdulikan index dengan for + enumerate() = mengembalikan 2 nilai, yaitu nilai index dan nilai isi dari index

for index, value in enumerate(nama_bulan):
    nomor_bulan = index + 1
    print('Bulan {} namanya: {}'.format(nomor_bulan,value))

# # Perulangan memperdulikan index dengan WHILE
i = 0
while i < len(nama_bulan):
    nomor_bulan = i + 1
    print('Bulan {} namanya: {}'.format(nomor_bulan, nama_bulan[i]))
    i += 1

