from datetime import date
import random

from Transaksi import Transaksi
from Database import *

class Struk:
    def __init__(self):
        self.id = str(random.randint(10000, 99999))
        self.date = date.today()
        self.total = 0
        self.payment = 0
        self.exchange = 0
        self.transactions = []

    def insert(self, barang, jumlah):
        self.transactions.append(Transaksi(barang, jumlah, self.id))

    def calculate(self):
        self.total = 0
        for transaction in self.transactions:
            self.total += transaction.subtotal
        return self.total

    def to_csv(self):
        return {
            "ID_struk": self.id,
            "tanggal_pembuatan_struk": self.date,
            "total_pembelian": self.total,
            "total_pembayaran": self.payment,
            "kembalian": self.exchange,
        }
    
    def set_payment(self, payment):
        message = ''
        if (self.total == 0):
            message = 'Anda belum melakukan kalkulasi atau menentukan barang yang dibeli.'

        elif (payment < self.total):
            message = 'PAYMENT pada struk ' + self.id + ' gagal. Pembayaran tidak cukup.'

        else:
            self.payment = payment
            self.exchange = payment - self.total
            for transaction in self.transactions:
                DB.insert_transaksi(transaction.to_csv())
            DB.insert_struk(self.to_csv())
            message = 'PAYMENT pada struk ' + self.id + ' berhasil. '\
                'Pembayaran ' + self.payment + '. Total Pembelian ' + self.total + '. '\
                'Kembalian ' + self.exchange + '. Struk berhasil disimpan dan dihapus dari struk aktif.'
    
        print(message)

        

    