nama = input("Nama Server: ")
suhu = int(input("Suhu CPU: "))

if suhu < 40:
    print("Suhu terlalu rendah")
elif suhu < 60:
    print("Suhu normal")
elif suhu < 80:
    print("Suhu cukup tinggi")
else:
    print("WARNING! Suhu terlalu tinggi")