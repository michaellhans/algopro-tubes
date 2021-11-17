import pandas as pd

PATH = "database/"

class Database:
    
    def __init__(self):
        self.tabel_barang = pd.read_csv(PATH + "T_BRG.csv")
        self.tabel_struk = pd.read_csv(PATH + "T_STRUK.csv")
        self.tabel_transaksi = pd.read_csv(PATH + "T_TRANSAKSI.csv")

    def insert_struk(self, data):
        self.tabel_struk.append(data)

    def insert_transaksi(self, data):
        self.tabel_transaksi.append(data)

    def select_barang(self, barang):
        return self.tabel_barang[self.tabel_barang['nama_barang'] == barang].iloc[0]

    def select_struk(self, start_date, end_date=""):
        if (end_date == ""):
            return self.tabel_struk[(self.tabel_struk['date'] >= start_date)]
        else:
            return self.tabel_struk[(self.tabel_struk['date'] >= start_date) & (self.tabel_struk['end_date'] <= end_date)]

    def save(self):
        self.tabel_barang.to_csv(PATH + "T_BRG.csv")
        self.tabel_struk.to_csv(PATH + 'T_STRUK.csv')

DB = Database()
print(DB.select_barang("Indomie Goreng")['ID_barang'])