from .Struk import Struk
from .Database import *
import re
from datetime import datetime

# System Class
class System:
    '''
    Class System acts as Swalayan System Representation
    '''

    def __init__(self):
        '''
        System Constructor
        '''
        self.active_struk = None

    def run(self, command: str):
        '''
        Run the user command and evaluate it
        If the command is invalid or there is an error on system, print the error message
        '''
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
            elif (main_command == 'HELP'):
                self.help()
            else:
                raise Exception("Command tidak valid. Gunakan HELP untuk melihat cara penggunaannya.")

        except Exception as e:
            print(e)

    def create_struk(self):
        '''
        Create Struk functionality for create new struk
        '''
        self.active_struk = Struk()
        print("CREATE_STRUK sukses. ID Struk: %s. Struk aktif: %s" % (self.active_struk.id, self.active_struk.id))

    def insert_struk(self, rest_command):
        '''
        Insert new transaction into the active struk
        '''
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
        '''
        Calculate Struk functionality
        '''
        self.check_active_struk(error_message="CALCULATE_STRUK gagal. ")
        self.active_struk.calculate()
        print("CALCULATE_STRUK pada struk %s berhasil. Total pembelian adalah %d." % (self.active_struk.id, self.active_struk.total))

    def payment(self, rest_command):
        '''
        Doing the payment for the active struk
        '''
        self.check_active_struk(error_message="PAYMENT gagal. ")
        nominal = int(rest_command)
        self.active_struk.set_payment(nominal)
        print('PAYMENT pada struk ' + self.active_struk.id + ' berhasil. '\
            'Pembayaran ' + str(self.active_struk.payment) + '. Total Pembelian ' + str(self.active_struk.total) + '. '\
            'Kembalian ' + str(self.active_struk.exchange) + '. Struk berhasil disimpan dan dihapus dari struk aktif.')
        self.active_struk = None

    def cancel_struk(self):
        '''
        Delete the active struk
        '''
        self.check_active_struk(error_message="CANCEL_STRUK gagal. ")
        print("STRUK %s berhasil dihapus dari memori." % self.active_struk.id)
        self.active_struk = None

    def _validate_range_date(self, start_date, end_date):
        if (len(start_date) == 0 or len(end_date) == 0):
            return True
        start = datetime.strptime(start_date, '%d-%m-%Y')
        end = datetime.strptime(end_date, '%d-%m-%Y')
        return start <= end

    def _validate_date(self, date):
        if (len(date) == 0):
            return True
        datetime.strptime(date, '%d-%m-%Y')
        return True

    def _extract_range_time(self, rest_command=''):
        '''
        Extract range time from rest_command and return start_date and end_date
        '''
        if (rest_command == None):
          rest_command = ''
        start_date = ''
        end_date = ''
        rest_command_arr = rest_command.split(" ")
        try:
          start_date = rest_command_arr[0]
          end_date = rest_command_arr[1]
        except:
          pass
        try:
          self._validate_date(start_date)
          self._validate_date(end_date)
          if (not self._validate_range_date(start_date, end_date)):
              raise Exception()
        except:
          raise Exception("Date tidak valid. Gunakan format DD-MM-YYYY dan pastikan end_date >= start_date.")
        return start_date, end_date

    def display_struk(self, rest_command):
        '''
        Display Struk Functionality to return all struk based on user command
        '''
        start_date, end_date = self._extract_range_time(rest_command)
        result = DB.select_struk(start_date=start_date, end_date=end_date)
        if (len(result) > 0):
            print(result)
        else:
            print("Tidak ada data yang sesuai pada rentang waktu tersebut.")

    def display_peak(self, rest_command):
        '''
        Display Peak Functionality to return all peak date for the sales based on user command
        '''
        start_date, end_date = self._extract_range_time(rest_command)
        result = DB.select_peak(start_date=start_date, end_date=end_date)
        if (len(result) > 0):
            print(result)
        else:
            print("Tidak ada data yang sesuai pada rentang waktu tersebut.")

    def best_product(self, rest_command):
        '''
        Best Product Functionality to return all best product based on user command
        '''
        start_date, end_date = self._extract_range_time(rest_command)
        result = DB.select_best_product(start_date=start_date, end_date=end_date)
        if (len(result) > 0):
            print(result)
        else:
            print("Tidak ada data yang sesuai pada rentang waktu tersebut.")

    def check_active_struk(self, error_message):
        '''
        Check if there is an active struk or not
        If there is no active struk, raise an error
        '''
        if (self.active_struk == None):
            raise Exception(error_message + "Tidak ada struk aktif. Silakan membuat struk.")

    def help(self):
        '''
        Show the help information about how to use the system and accepted command
        '''
        help_info = "ACCEPTED COMMAND: \n\
            1. CREATE_STRUK \n\
            2. INSERT <nama_barang> <jumlah_barang> \n\
            3. CALCULATE_STRUK \n\
            4. PAYMENT <nominal> \n\
            5. CANCEL_STRUK \n\
            6. DISPLAY_STRUK <tanggal_awal> <tanggal_akhir> \n\
            7. DISPLAY_PEAK <tanggal_awal> <tanggal_akhir> \n\
            8. BEST_PRODUCT <tanggal_awal> <tanggal_akhir> \n\
            9. HELP \n\
            10. EXIT \n"

        print(help_info)