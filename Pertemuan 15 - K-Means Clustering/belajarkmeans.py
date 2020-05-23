import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans


class BelajarKMeans(object):

    def __init__(self, file_dataset: str):
        sns.set()
        self.file_dataset = file_dataset
        self.data_points = None
        self.hasil_cluster = None

    def load_data(self):
        print('<<[Memuat data]>>')
        data = pd.read_csv(self.file_dataset)
        self.data_points = data.iloc[:, 1:3]
        print(self.data_points)

    def scatter_plot(self):
        print('<<[Memvisualisasikan data dengan Scatter Plot]>>')
        plt.scatter(
            self.data_points['Longitude'],  # Sumbu X
            self.data_points['Latitude']  # Sumbu Y
        )
        # Mengatur agar titik-titiknya nampak seperti di peta
        plt.xlim(-180, 180)
        plt.ylim(-90, 90)
        plt.show()

    def buat_cluster(self):
        print('<<[Membuat cluster dari data yang telah di-load sebelumnya]>>')
        kmeans = KMeans(3)  # Jumlah cluster yang diinginkan
        self.hasil_cluster = kmeans.fit_predict(self.data_points)
        print(self.hasil_cluster)

    def visualisasikan_cluster(self):
        print('<<[Memvisualisasikan cluster yang telah dibuat]>>')
        data_dgn_cluster = self.data_points.copy()
        data_dgn_cluster["Cluster"] = self.hasil_cluster
        print(data_dgn_cluster)
        plt.scatter(
            data_dgn_cluster['Longitude'],
            data_dgn_cluster['Latitude'],
            c=data_dgn_cluster['Cluster'], # Memberi warna pada titik
            cmap='inferno'
        )
        plt.xlim(-180, 180)
        plt.ylim(-90, 90)
        plt.show()
