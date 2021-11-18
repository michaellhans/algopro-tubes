from .Database import *

class Transaksi:
    def __init__(self, barang, jumlah, id_struk):
        data = DB.select_barang(barang)
        self.id_barang = data['ID_barang']
        self.id_struk = id_struk
        self.barang = barang
        self.jumlah = jumlah
        self.harga_satuan = data['harga_barang']
        self.subtotal = self.jumlah * self.harga_satuan

    def to_csv(self):
        return {
            "ID_barang": self.id_barang,
            "ID_struk": self.id_struk,
            "nama_barang": self.barang,
            "jumlah_barang": self.jumlah,
            "harga_satuan": self.harga_satuan,
            "subtotal": self.subtotal,
        }