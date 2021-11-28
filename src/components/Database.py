import pandas as pd

PATH = "database/"

class Database:

    def __init__(self):
        self.tabel_barang = pd.read_csv(PATH + "T_BRG.csv")
        self.tabel_barang['ID_barang'] = self.tabel_barang['ID_barang'].astype(str)
        self.tabel_struk = pd.read_csv(PATH + "T_STRUK.csv")
        self.tabel_struk['total_pembayaran'] = self.tabel_struk['total_pembayaran'].astype(int)
        self.tabel_transaksi = pd.read_csv(PATH + "T_TRANSAKSI.csv")

    def insert_struk(self, data):
        self.tabel_struk = self.tabel_struk.append(data, ignore_index=True)

    def insert_transaksi(self, data):
        self.tabel_transaksi = self.tabel_transaksi.append(data, ignore_index=True)

    def select_barang(self, barang):
        return self.tabel_barang[self.tabel_barang['nama_barang'] == barang].iloc[0]

    def select_struk(self, start_date="", end_date=""):
        result = self.tabel_struk
        if (start_date):
          result = result[result['tanggal_pembuatan_struk'] >= start_date]
        if (end_date):
          result = result[result['tanggal_pembuatan_struk'] <= end_date]
        return result

    def select_peak(self, start_date="", end_date=""):
        result = self.select_struk(start_date=start_date, end_date=end_date)
        joined_result = result.merge(self.tabel_transaksi[['ID_struk', 'ID_barang']], on='ID_struk', how='left')
        joined_result['count'] = joined_result.groupby('tanggal_pembuatan_struk')['tanggal_pembuatan_struk'].transform('count')
        joined_result = joined_result.groupby('tanggal_pembuatan_struk').aggregate({'total_pembayaran':'sum', 'count': 'max'}).sort_values('count', ascending=False)
        return joined_result[:10]

    def select_best_product(self, start_date="", end_date=""):
        result = self.select_struk(start_date=start_date, end_date=end_date)
        joined_result = result.merge(self.tabel_transaksi[['ID_struk', 'ID_barang', 'jumlah_barang']], on='ID_struk', how='left').groupby('ID_barang').aggregate({'total_pembelian': 'sum', 'jumlah_barang': 'sum'}).merge(self.tabel_barang, on='ID_barang', how='left').sort_values(by='total_pembelian', ascending=False)
        return joined_result[:5] 

    def save(self):
        self.tabel_transaksi.to_csv(PATH + "T_TRANSAKSI.csv", index=False)
        self.tabel_struk.to_csv(PATH + 'T_STRUK.csv', index=False)

DB = Database()