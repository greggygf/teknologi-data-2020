# Class Matkul untuk menampung data seputar mata kuliah
class Matkul(object):
    def __init__(self):
        # Properties/Atribut class (data yang diproses di class ini)
        self.nama = ''
        self.sks = 0
        self.nilai_angka = 0

    def get_nilai_skala_4(self):
        return self.nilai_angka / 100 * 4

    def get_nilai_huruf(self):
        n = self.get_nilai_skala_4()

        if n >= 3.70:
            return 'A'
        elif 3.70 > n >= 3.0:
            return 'B'
        elif 3.0 > n >= 2.0:
            return 'C'
        elif 2.0 > n >= 1.0:
            return 'D'
        else:
            return 'E'
