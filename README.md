# Algoritma & Pemrograman B Tugas Besar

## Deskripsi Aplikasi
Toko Swalayan Algoritma dan Pemrograman B adalah aplikasi berbasis Command Line Interface yang dibangun sebagai sistem kasir untuk memfasilitasi kebutuhan pencatatan transaksi dan pengelolaan transaksi. Selain itu, aplikasi ini juga akan digunakan oleh pemilik toko swalayan untuk mendapatkan insight-insight tertentu terkait pendapatan yang diperoleh dalam periode waktu tertentu berdasarkan data transaksi yang dimilikinya.

## Prerequisites
* Python 3.9.9
* Pandas Library
* Regex Library

## How to Use
1. Masuk ke directory src.
2. Jalankan command prompt dan ketikkan command berikut ini.<br>
``` python app.py ```
3. Selamat menggunakan aplikasi.

## Used Syntax
1. CREATE_STRUK<br>
Membuat struk baru di memori. Struk yang baru dibuat adalah struk yang aktif.
2. INSERT<spasi><nama_barang><spasi><jumlah_barang><br>
Menambah barang pada struk yang sedang aktif. Perintah ini memeriksa apakah nama barang yang
diinput ada di dalam database. Jika barang ada di database, proses input barang dilanjutkan. Jika
barang tidak ada di dalam database, barang tidak diinput. Nama barang diinput dalam tanda petik
dua, i.e. “Coklat Silverqueen”.
3. CALCULATE_STRUK<br>
Menghitung total pembelian pada struk yang sedang aktif.
4. PAYMENT<spasi><nominal><br>
Menyimpan nilai uang pembayaran dari konsumen, menghitung jumlah kembalian, dan
menyimpan struk dalam database. Struk ini dihapus dari struk aktif.
5. CANCEL_STRUK<br>
Menghapus struk aktif dari memori.
6. DISPLAY_STRUK<spasi><tanggal_awal><spasi><tanggal_akhir><br>
Menampilkan semua struk yang dibuat pada rentang tanggal awal dan tanggal akhir. Jika hanya
ada satu tanggal saja, maka semua struk yang dibuat pada tanggal tersebut dan sesudah tanggal
tersebut ditampilkan ke layar.
7. DISPLAY_PEAK<spasi><tanggal_awal><spasi><tanggal_akhir><br>
Menampilkan top 10 hari-hari terjadinya peak transaksi dan jumlah transaksi yang terjadi pada
rentang waktu tertentu. Jika rentang tidak diberikan maka top 10 diambil dari keseluruhan transaksi.
Jika hanya satu tanggal yang diberikan maka pencarian top 10 dilakukan mulai tanggal tersebut.
8. BEST_PRODUCT<spasi><tanggal_awal><spasi><tanggal_akhir><br>
Menampilkan top 5 barang yang paling laris pada rentang waktu tertentu. Jika rentang waktu tidak
diberikan maka pencarian top 5 dilakukan pada semua transaksi. Jika hanya satu tanggal yang
diberikan maka pencarian top 5 dilakukan mulai dari transaksi yang ada sejak tanggal tersebut.
9. HELP<br>
Melihat cara penggunaan aplikasi tersebut.
10. EXIT<br>
Menutup aplikasi swalayan.

## Tabel Basis Data
Berikut ini adalah tabel basis data yang dirancang dalam aplikasi ini.

### 1. Tabel Barang
| Atribut     | Type Data   |
| ----------- | ----------- |
| ID_barang   | String      |
| nama_barang | String      |
| harga_barang| Integer     |
<br>

### 2. Tabel Struk
| Atribut                       | Type Data   |
| ----------------------------- | ----------- |
| ID_struk                      | String      |
| tanggal_pembuatan_struk       | Date        |
| total_pembelian               | Integer     |
| total_pembayaran              | Integer     |
| kembalian                     | Integer     |
<br>

### 3. Tabel Transaksi
| Atribut                       | Type Data   |
| ----------------------------- | ----------- |
| ID_struk                      | String      |
| ID_barang                     | String      |
| nama_barang                   | String      |
| harga_barang                  | Integer     |
| jumlah_barang                 | Integer     |
| harga_satuan                  | Integer     |
| subtotal                      | Integer     |

## Author
* 13518056 - Michael Hans
* 13518066 - Byan Sakura Kireyna Aji

## Acknowledgment
* Dr. Techn. Muhammad Zuhri Catur Candra, S.T, M.T.
* Dr. tech. Wikan Danar Sunindyo, S.T, M.Sc.
* Asisten Praktikum IF5021 Algoritma dan Pemrograman B
