from .Database import *

class Transaksi:
    '''
    Class Transaksi to store transaction item of the struk
    '''

    def __init__(self, barang, jumlah, id_struk):
        '''
        Construct new transaksi item
        '''
        data = DB.select_barang(barang)
        self.id_barang = data['ID_barang']
        self.id_struk = id_struk
        self.barang = barang
        self.jumlah = jumlah
        self.harga_satuan = data['harga_barang']
        self.subtotal = self.jumlah * self.harga_satuan

    def to_csv(self):
        '''
        Return CSV formatted data of the transaksi
        '''
        return {
            "ID_struk": self.id_struk,
            "ID_barang": self.id_barang,
            "nama_barang": self.barang,
            "jumlah_barang": self.jumlah,
            "harga_satuan": self.harga_satuan,
            "subtotal": self.subtotal,
        }