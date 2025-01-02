# class_view/class_view.py
class ProdukView:
    def tampilkan_produk(self, produk_list):
        print(f"{'Nama Produk':<20} {'Harga':<10} {'Stok':<10}")
        print("-" * 40)
        for produk in produk_list:
            print(f"{produk.nama:<20} {produk.harga:<10.2f} {produk.stok:<10}")