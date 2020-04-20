"""
Aplikasi KHS dengan paradigma prosedural
"""

# Matakuliah 1
mk1_nama = 'Teknologi Data'
mk1_sks = 3
mk1_nilai = 90

# Matakuliah 2
mk2_nama = 'Komputasi Kognitif'
mk2_sks = 2
mk2_nilai = 81

# Matakuliah 3
mk3_nama = 'Algoritma dan Struktur Data'
mk3_sks = 2
mk3_nilai = 65

# Matakuliah 4
mk4_nama = 'Statistika Terapan'
mk4_sks = 3
mk4_nilai = 90

# ---- PROSES ----
# Mengubah ke skala-4

mk1_skala_4 = mk1_nilai / 100 * 4
mk2_skala_4 = mk2_nilai / 100 * 4
mk3_skala_4 = mk3_nilai / 100 * 4
mk4_skala_4 = mk4_nilai / 100 * 4


def get_nilai_huruf(nilai: float):
    if nilai >= 3.70:
        return 'A'
    elif 3.70 > nilai >= 3.0:
        return 'B'
    elif 3.0 > nilai >= 2.0:
        return 'C'
    elif 2.0 > nilai >= 1.0:
        return 'D'
    else:
        return 'E'

# Menentukan nilai huruf
mk1_nilai_huruf = get_nilai_huruf(mk1_skala_4)
mk2_nilai_huruf = get_nilai_huruf(mk2_skala_4)
mk3_nilai_huruf = get_nilai_huruf(mk3_skala_4)
mk4_nilai_huruf = get_nilai_huruf(mk4_skala_4)

# Menghitung total SKS
total_sks = mk1_sks + mk2_sks + mk3_sks + mk4_sks

# Menghitung IPK
ipk = ((mk1_skala_4 * mk1_sks) + (mk2_skala_4 * mk2_sks) + (mk3_skala_4 * mk3_sks) + (mk4_skala_4 * mk4_sks)) / total_sks

print("KARTU HASIL STUDI")
print("--------------------------")
print("Mata Kuliah : {}".format(mk1_nama))
print("Nilai Angka : {}".format(mk1_skala_4))
print("Nilai Huruf : {}".format(mk1_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk2_nama))
print("Nilai Angka : {}".format(mk2_skala_4))
print("Nilai Huruf : {}".format(mk2_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk3_nama))
print("Nilai Angka : {}".format(mk3_skala_4))
print("Nilai Huruf : {}".format(mk3_nilai_huruf))
print("--------------------------")
print("Mata Kuliah : {}".format(mk4_nama))
print("Nilai Angka : {}".format(mk4_skala_4))
print("Nilai Huruf : {}".format(mk4_nilai_huruf))
print("--------------------------")
print("Total SKS \t: {}".format(total_sks))
print("IPK \t\t: {}".format(ipk))