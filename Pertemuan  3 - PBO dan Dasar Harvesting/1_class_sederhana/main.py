from kalkulator import Kalkulator

def main():
    b1 = float(input('Masukkan Bilangan 1 : '))
    b2 = float(input('Masukkan Bilangan 2 : '))
    op = input('Masukkan Operator ( * / + - ) : ')

    angka = Kalkulator(b1, b2, op)


    print('Hasilnya adalah : {}'.format(angka.hitung()))


main()
