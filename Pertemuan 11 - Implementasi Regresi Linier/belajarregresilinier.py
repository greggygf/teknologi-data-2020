import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm


class BelajarRegresiLinier(object):

    # '''
    def __init__(self, file_data: str):
        self.file_data = file_data
        self.data = None
        self.y_samples = None
        self.x_samples = None
        # y_hat = b0 + b1 * x1
        self.b0 = None
        self.b1 = None

    def load_data(self):
        self.data = pd.read_csv(self.file_data)
        print(self.data)
        statistik_data = self.data.describe()
        print(statistik_data)

    def set_dependent_independent(self):
        # Jangan lupa:
        # y^ = b0 + b1x1
        # Tentukan dependent variable (y^)
        self.y_samples = self.data['luas']
        # Independent variable (x1)
        self.x_samples = self.data['harga_usd']

    def visualisasikan_data(self):
        plt.scatter(self.x_samples, self.y_samples)
        plt.xlabel('Sample Harga Real Estate ( USD )', fontsize=20)
        plt.ylabel('Sample Luas Tanah', fontsize=20)
        plt.show()

    def set_b0_b1(self):
        # Setiap bilangan pada matrix x_samples ditambahkan 1 kolom berisi angka 1 disebelah kiri
        # Kalikan matrix X dengan 1
        x1 = sm.add_constant(self.x_samples)
        print(x1)
        # Menemukan b0 & b1 model dengan statmodels
        model = sm.OLS(self.y_samples, x1).fit()
        self.b0 = model.params['const']
        self.b1 = model.params['harga_usd']
        print(model.params['const'])
        summary = model.summary()
        print(summary)

    def visualisasikan_model(self):
        plt.scatter(self.x_samples, self.y_samples)
        prediksi = self.b0 + self.b1 * self.x_samples
        plt.plot(self.x_samples, prediksi, c='red', label='Regression Line')
        plt.xlabel('Sample Harga Real Estate ( USD )', fontsize=20)
        plt.ylabel('Prediksi Luas Tanah', fontsize=20)
        plt.show()

    def prediksi(self, harga_usd):
        # y_hat ~ Luas Tanah
        y_hat = self.b0 + self.b1 * harga_usd
        return y_hat  # Prediksi Luas Tanah.
    # '''
