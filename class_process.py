# class_process/class_process.py
from class_data import Produk
class ProdukProcess:
    def __init__(self):
        self.produk_list = []
        
    def tambah_produk(self, nama, harga, stok):
        if not nama:
            raise ValueError("Nama Produk tidak boleh kosong.")
        if harga <= 0:
            raise ValueError("Harga produk harus lebih besar dari 0.")
        if stok < 0:
            raise ValueError("Stok produk tidak boleh negatif.")
        
        produk = Produk(nama, harga, stok)
        self.produk_list.append(produk)

    def get_produk(self):
        return self.produk_list