from khs import Khs
from matkul import Matkul


def main():
    # Panggil class-class yang sudah dibuat

    # Mata kuliah ke-1
    mk1 = Matkul()
    mk1.nama = 'Teknologi Data'
    mk1.sks = 3
    mk1.nilai_angka = 90

    # Mata kuliah ke-1
    mk2 = Matkul()
    mk2.nama = 'Komputasi Kognitif'
    mk2.sks = 2
    mk2.nilai_angka = 81

    # Mata kuliah ke-3
    mk3 = Matkul()
    mk3.nama = 'Algoritma dan Struktur Data'
    mk3.sks = 2
    mk3.nilai_angka = 65

    # Mata kuliah ke-4
    mk4 = Matkul()
    mk4.nama = 'Statistika Terapan'
    mk4.sks = 3
    mk4.nilai_angka = 90

    khs = Khs()
    khs.tambah_matkul(mk1)
    khs.tambah_matkul(mk2)
    khs.tambah_matkul(mk3)
    khs.tambah_matkul(mk4)

    khs.proses()

    khs.cetak()


main()


