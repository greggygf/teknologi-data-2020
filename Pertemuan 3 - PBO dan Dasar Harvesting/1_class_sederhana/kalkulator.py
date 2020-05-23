class Kalkulator:

    # Membuat konstruktor
    # Konstruktornya berparameter, bilangan 1, 2 dan operatornya
    def __init__(self, b1: float, b2: float, op: str):
        # Mengisikan nilai ke atribut class
        self.bilangan1 = b1
        self.bilangan2 = b2
        self.operator = op

    # Membuat method instance
    # Method tidak berparameter, cukup dengan self saja.
    def hitung(self):
        # Percabangan. Menghitung berdasarkan operator yang diinputkan oleh pengguna

        if (self.operator == '+'):
            return self.bilangan1 + self.bilangan2
        elif (self.operator == '-'):
            return self.bilangan1 - self.bilangan2
        elif (self.operator == '*'):
            return self.bilangan1 * self.bilangan2
        elif (self.operator == '/'):
            return self.bilangan1 / self.bilangan2
        else:
            return 'Operator invalid!'
