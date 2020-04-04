# Membuat fungsi di Python diawali dengan kata kunci def

def kali_100(angka: float):
    hasil = angka * 100
    return hasil


def eja_nama(nama: str):
    nama_kapital = nama.upper()
    hasil = ""
    for huruf in nama_kapital:
        hasil = (hasil + huruf + ", ")
    hasil = hasil[0:(len(hasil) - 2)]
    return hasil


def main():
    nama = 'Greggy'
    print(eja_nama(nama))


main()
