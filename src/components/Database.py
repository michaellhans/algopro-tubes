import pandas as pd

PATH = "database/"

class Database:
    
    def __init__(self):
        self.tabel_barang = pd.read_csv(PATH + "T_BRG.csv")
        self.tabel_struk = pd.read_csv(PATH + "T_STRUK.csv")
        self.tabel_transaksi = pd.read_csv(PATH + "T_TRANSAKSI.csv")

    def insert_struk(self, data):
        self.tabel_struk = self.tabel_struk.append(data, ignore_index=True)

    def insert_transaksi(self, data):
        self.tabel_transaksi = self.tabel_transaksi.append(data, ignore_index=True)

    def select_barang(self, barang):
        return self.tabel_barang[self.tabel_barang['nama_barang'] == barang].iloc[0]

    def select_struk(self, start_date="", end_date=""):
        # TO DO LIST
        pass

    def select_best_product(self, start_date="", end_date=""):
        # TO DO LIST
        pass

    def save(self):
        self.tabel_transaksi.to_csv(PATH + "T_TRANSAKSI.csv", index=False)
        self.tabel_struk.to_csv(PATH + 'T_STRUK.csv', index=False)

DB = Database()