from belajarregresilinier import BelajarRegresiLinier


def main():
    print('Regresi Linier Sederhana')

    print('-- Learning --')
    brl = BelajarRegresiLinier('Resources/data_kuis_2.csv')
    brl.load_data()
    brl.set_dependent_independent()
    # brl.visualisasikan_data()
    brl.set_b0_b1()
    # brl.visualisasikan_model()

    print('-- Testing --')
    harga = 100
    prediksi_luas_tanah = brl.prediksi(harga)
    print(prediksi_luas_tanah)


main()
