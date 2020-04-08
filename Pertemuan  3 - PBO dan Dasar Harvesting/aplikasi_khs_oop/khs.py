from matkul import Matkul

# Class yang melakukan perhitungan terhadap class Matkul
class Khs(object):
    def __init__(self):
        # Data yang diolah di class ini (atribut)
        # Atribut yang aman diakses dari luar kelas:
        self.daftar_matkul = []
        self.totalSks = 0
        self.ipk = 0

        # Atribut yang sebaiknya tidak diakses di luar kelas ini ('private')
        # Dianjurkan untuk menambahkan underscore di depan nama var/method
        # Karena di Python semuanya public

        self._totalNilai = 0

    # Method untuk menambahkan matakuliah yang akan diproses
    def tambah_matkul(self, matkul_baru: Matkul):
        self.daftar_matkul.append(matkul_baru)

    # Untuk menghitung sks dan ipk
    def proses(self):
        # Berulang sebanyak matkul yang ada di dalam daftar_matkul
        for matkul in self.daftar_matkul:
            self.totalSks += matkul.sks  # Total SKS
            self._totalNilai += (matkul.get_nilai_skala_4() * matkul.sks)

        # Mencari nilai IPK
        self.ipk = self._totalNilai / self.totalSks

    # Untuk mencetak IPK, total SKS dan semua data mata kuliah
    def cetak(self):
        for matkul in self.daftar_matkul:
            print("Mata Kuliah : {}".format(matkul.nama))
            print("Nilai Angka : {}".format(matkul.get_nilai_skala_4()))
            print("Nilai Huruf : {}".format(matkul.get_nilai_huruf()))
            print("--------------------------------------------")

        print("Total SKS : {}".format(self.totalSks))
        print("IPK : {}".format(self.ipk))
