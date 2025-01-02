# main.py
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