from Struk import Struk
from Database import *

# Main program
class Swalayan:
    def __init__(self):
        self.active_struk = None
    
    def run(self, command: str):
        try:
            command_list = command.split(" ")
            main_command = command_list[0]
            rest_command = command_list[1:]
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
            else:
                raise Exception("Command tidak valid")
        
        except Exception as e:
            print(e)


    def create_struk(self):
        self.active_struk = Struk()
        print("CREATE_STRUK sukses. ID Struk: " + self.active_struk.id + ". Struk aktif: " + self.active_struk.id)

    def insert_struk(self, rest_command):
        self.check_active_struk()
        nama_barang, jumlah_barang = rest_command[0].replace('"', ''), int(rest_command[1])
        self.active_struk.insert(nama_barang, jumlah_barang)

    def calculate_struk(self):
        self.check_active_struk()
        self.active_struk.calculate()

    def payment(self, rest_command):
        self.check_active_struk()
        nominal = int(rest_command[0])
        self.active_struk.set_payment(nominal)
        self.active_struk = None

    def cancel_struk(self):
        self.check_active_struk()
        self.active_struk = None

    def display_struk(self, start_date, end_date):
        # TO DO LIST
        pass

    def display_peak(self, start_date="", end_date=""):
        # TO DO LIST
        pass

    def best_product(self, start_date="", end_date=""):
        # TO DO LIST
        pass

    def check_active_struk(self):
        if (self.active_struk == None):
            raise Exception("Struk belum dibuat. Harap gunakan CREATE_STRUK terlebih dahulu")

System = Swalayan()
print("Selamat datang di Toko Swalayan Algoritma dan Pemrograman B!")
command = input(">>> ")
while (command != "EXIT"):
    System.run(command)
    command = input(">>> ")
print("Terima kasih telah menggunakan kasir Algopro!")
