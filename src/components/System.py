from .Struk import Struk
from .Database import *
import re

# System Class
class System:
    def __init__(self):
        self.active_struk = None
    
    def run(self, command: str):
        try:
            command_list = command.split(" ", 1)
            main_command = command_list[0]
            rest_command = command_list[1] if (len(command_list) == 2) else None
            if (main_command == 'CREATE_STRUK'):
                self.create_struk()
            elif (main_command == 'INSERT'):
                self.insert_struk(rest_command)
            elif (main_command == 'CALCULATE_STRUK'):
                self.calculate_struk()
            elif (main_command == 'PAYMENT'):
                self.payment(rest_command)
            elif (main_command == 'CANCEL_STRUK'):
                self.cancel_struk()
            elif (main_command == 'DISPLAY_STRUK'):
                self.display_struk(rest_command)
            elif (main_command == 'DISPLAY_PEAK'):
                self.display_peak(rest_command)
            elif (main_command == 'BEST_PRODUCT'):
                self.best_product(rest_command)
            elif (main_command == 'EXIT'):
                quit()
            else:
                raise Exception("Command tidak valid")

        except Exception as e:
            print(e)

    def create_struk(self):
        self.active_struk = Struk()
        print("CREATE_STRUK sukses. ID Struk: %s. Struk aktif: %s" % (self.active_struk.id, self.active_struk.id))

    def insert_struk(self, rest_command):
        self.check_active_struk(error_message="INSERT gagal. ")
        is_valid = re.match("\"[\w\s]+\" [0-9]+", rest_command)
        if (is_valid):
            rest_command_arr = rest_command.rsplit(" ", 1)
            nama_barang, jumlah_barang = rest_command_arr[0].replace('"', ''), int(rest_command_arr[1])
            self.active_struk.insert(nama_barang, jumlah_barang)
            print("INSERT pada struk %s sukses. Barang %s. Jumlah barang %d." % (self.active_struk.id, nama_barang, jumlah_barang))
        else:
            raise Exception("INSERT pada struk %s gagal. Sintaks salah." % (self.active_struk.id))

    def calculate_struk(self):
        self.check_active_struk(error_message="CALCULATE_STRUK gagal. ")
        self.active_struk.calculate()
        print("CALCULATE_STRUK pada struk %s berhasil. Total pembelian adalah %d." % (self.active_struk.id, self.active_struk.total))

    def payment(self, rest_command):
        self.check_active_struk(error_message="PAYMENT gagal. ")
        nominal = int(rest_command)
        self.active_struk.set_payment(nominal)
        print('PAYMENT pada struk ' + self.active_struk.id + ' berhasil. '\
            'Pembayaran ' + str(self.active_struk.payment) + '. Total Pembelian ' + str(self.active_struk.total) + '. '\
            'Kembalian ' + str(self.active_struk.exchange) + '. Struk berhasil disimpan dan dihapus dari struk aktif.')
        self.active_struk = None

    def cancel_struk(self):
        self.check_active_struk(error_message="CANCEL_STRUK gagal. ")
        print("STRUK %s berhasil dihapus dari memori." % self.active_struk.id)
        self.active_struk = None

    def display_struk(self, start_date, end_date):
        # TO DO LIST
        # HINT: Backend codenya ada di Database
        pass

    def display_peak(self, start_date="", end_date=""):
        # TO DO LIST
        # HINT: Backend codenya ada di Database
        pass

    def best_product(self, start_date="", end_date=""):
        # TO DO LIST
        # HINT: Backend codenya ada di Database
        pass

    def check_active_struk(self, error_message):
        if (self.active_struk == None):
            raise Exception(error_message + "Tidak ada struk aktif. Silakan membuat struk.")
