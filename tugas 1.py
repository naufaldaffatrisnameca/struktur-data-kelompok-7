data = []

while True:
    print("\nMenu:")
    print("1. Tambah Pengeluaran")
    print("2. Lihat Semua Pengeluaran")
    print("3. Keluar")

    pilih = input("Pilih: ")

    if pilih == "1":
        kategori = input("Kategori (makanan/pakaian/lainnya): ")
        jumlah = int(input("Jumlah uang: "))

        item = {"kategori": kategori, "jumlah": jumlah}
        data.append(item)

        print("Data ditambahkan.")

    elif pilih == "2":
        total = 0
        print("\nDaftar Pengeluaran:")
        for d in data:
            print(d["kategori"], "-", d["jumlah"])
            total += d["jumlah"]

        print("Total:", total)

    elif pilih == "3":
        print("Selesai.")
        break

    else:
        print("Pilihan salah.")