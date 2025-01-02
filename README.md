# Tugas-UAS-Project-Pemrogaman
# DATA DIRI
## Nama : Sheila Antica Oktaviani
## Kelas : TI.24.A1
## NIM : 312410002
## Program akan meminta masukan data yang terdiri dari nama produk, harga produk, dan jumlah stok produk.
![output UAS project](https://github.com/user-attachments/assets/3a81cfd1-d824-49ad-95c1-c78e24f1b830)
## Class Data
## _init.py
```Python
# class_data/__init__.py
from .class_data import Produk
```
## class_data.py
```Python
# class_data/class_data.py
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok
```
## Class Process
## _init.py
```Python
# class_process/__init__.py
from .class_process import ProdukProcess
```
## class_process.py
```Python
# class_process/class_process.py
from class_data import Produk

class ProdukProcess:
    def __init__(self):
        self.produk_list = []

    def tambah_produk(self, nama, harga, stok):
        if not nama:
            raise ValueError("Nama produk tidak boleh kosong.")
        if harga <= 0:
            raise ValueError("Harga produk harus lebih besar dari 0.")
        if stok < 0:
            raise ValueError("Stok produk tidak boleh negatif.")
        
        produk = Produk(nama, harga, stok)
        self.produk_list.append(produk)

    def get_produk(self):
        return self.produk_list
```
## Class View
##  _init.py
```Python
# class_view/__init__.py
from .class_view import ProdukView
```
## class_view.py
```Python
# class_view/class_view.py
class ProdukView:
    def tampilkan_produk(self, produk_list):
        print(f"{'Nama Produk':<20} {'Harga':<10} {'Stok':<10}")
        print("-" * 40)
        for produk in produk_list:
            print(f"{produk.nama:<20} {produk.harga:<10.2f} {produk.stok:<10}")
```
## main.py
```Python
from class_data import Produk
from class_process import ProdukProcess
from class_view import ProdukView

def main():
    process = ProdukProcess()  # Membuat instance dari ProdukProcess
    view = ProdukView()        # Membuat instance dari ProdukView

    while True:
        try:
            # Meminta input nama produk
            nama = input("Masukkan nama produk (atau ketik 'exit' untuk keluar): ")
            if nama.lower() == 'exit':
                break
            
            # Meminta input harga produk
            harga = float(input("Masukkan harga produk: "))
            
            # Meminta input stok produk
            stok = int(input("Masukkan stok produk: "))
            
            # Menambahkan produk ke dalam daftar
            process.tambah_produk(nama, harga, stok)
        except ValueError as e:
            print(f"Error: {e}")

    # Tampilkan data produk
    print("\nDaftar Produk:")
    view.tampilkan_produk(process.get_produk())

if __name__ == "__main__":
    main()
```
# Penjelasan Code
Saat menjalankan program, pengguna akan diminta untuk memberikan informasi mengenai nama produk, harga, dan stok yang tersedia. class Produk: Kelas ini merepresentasikan sebuah produk. __init__(self, nama, harga, stok): Konstruktor kelas. Dipanggil saat objek Produk dibuat. Ia menginisialisasi atribut nama, harga, dan stok.
from .class_data import Produk: Di __init__.py, ini mengimpor kelas Produk dari file class_data.py dalam direktori yang sama. Tanda titik (.) di depan class_data menandakan relative import.  class_process/class_process.py dan class_process/__init__.py. class ProdukProcess: Kelas ini menangani logika pemrosesan data produk.
__init__(self): Konstruktor kelas. Menginisialisasi produk_list sebagai list kosong untuk menyimpan objek-objek Produk.
tambah_produk(self, nama, harga, stok): Menambahkan produk baru ke dalam produk_list. Melakukan validasi input untuk memastikan nama tidak kosong, harga positif, dan stok non-negatif. Jika validasi gagal, akan memunculkan ValueError. get_produk(self): Mengembalikan list produk. from class_data import Produk: Mengimpor kelas Produk agar dapat digunakan dalam tambah_produk. class_view/class_view.py dan class_view/__init__.py. class ProdukView: Kelas ini bertanggung jawab untuk menampilkan data produk.
tampilkan_produk(self, produk_list): Menerima list produk dan menampilkannya dalam format tabel yang rapi. :<20, :<10.2f, dan :<10 digunakan untuk memformat output (alignment dan presisi desimal).
main.py. main(): Fungsi utama program.
Membuat instance ProdukProcess dan ProdukView.
Perulangan while True: Meminta input data produk dari pengguna sampai pengguna mengetik "exit".
try...except ValueError: Menangani kesalahan input yang mungkin terjadi (misalnya, input non-angka untuk harga atau stok).
Memanggil process.tambah_produk() untuk menambahkan produk ke dalam list.
Memanggil view.tampilkan_produk() untuk menampilkan daftar produk.
if __name__ == "__main__":: Memastikan fungsi main() hanya dipanggil saat file main.py dieksekusi langsung (bukan diimpor sebagai modul).
## Kesimpulan Penjelasan Code 
ode ini menerapkan prinsip OOP dengan memisahkan data produk (Produk), logika pemrosesan (ProdukProcess), dan tampilan (ProdukView) ke dalam kelas-kelas terpisah. Ini membuat kode lebih modular, terorganisir, dan mudah dipelihara. Penggunaan package dan relative import juga merupakan praktik yang baik untuk proyek yang lebih besar. Validasi input dengan try...except membantu mencegah error dan membuat program lebih robust.
