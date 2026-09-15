nama = input("Nama barang: ")
harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah barang: "))

total = harga * jumlah

print("Total bayar =", total)

bayar = int(input("Uang bayar: "))

kembalian = bayar - total

print("Kembalian =", kembalian)