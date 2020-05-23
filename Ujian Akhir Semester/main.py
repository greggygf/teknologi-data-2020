from belajarkmeans import BelajarKMeans


def main():
    bkm = BelajarKMeans('resource/data_nasabah_asuransi.csv')
    bkm.load_data()
    # bkm.scatter_plot()
    bkm.buat_cluster()
    bkm.visualisasikan_cluster()


main()
