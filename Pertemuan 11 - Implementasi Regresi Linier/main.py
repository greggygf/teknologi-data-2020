from belajarregresilinier import BelajarRegresiLinier


def main():
    print('Regresi Linier Sederhana')

    print('-- Learning --')
    brl = BelajarRegresiLinier('Resources/harga_real_estate.csv')
    brl.load_data()
    brl.set_dependent_independent()
    # brl.visualisasikan_data()
    brl.set_b0_b1()
    # brl.visualisasikan_model()

    print('-- Testing --')
    harga_usd = 300000
    prediksi_luas_tanah = brl.prediksi(harga_usd)
    print(prediksi_luas_tanah)


main()
