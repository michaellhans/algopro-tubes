from System import *

System = System()
print("Selamat datang di Toko Swalayan Algoritma dan Pemrograman B!")
command = input(">>> ")
while (command != "EXIT"):
    System.run(command)
    command = input(">>> ")
print("Terima kasih telah menggunakan kasir Algopro!")