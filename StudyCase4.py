buku = {
    "judul" : "Bumi",
    "penulis" : "Tere Liye",
    "tahun_terbit" : "2014"
}

while True: 
    print("\n=== MENU DATA BUKU===")
    print("1. Tampilkan Data Buku")
    print("2. Tambahkan Penerbit")
    print("3. Ubah Data Penulis")
    print("4. Hapus Data Penerbit")
    print("5. Keluar")

    pilihan = input("pilihan menu:")

    if pilihan == "1":
        print("\nData Buku:")
        print("Judul:", buku["judul"])
        print("Penulis:", buku["penulis"])
        print("Tahun Terbit:", buku["tahun_terbit"])

        if "penerbit" in buku:
            print("Penerbit:", buku["penerbit"])

    elif pilihan == "2":
        penerbit = input("Masukkan nama penerbit:")
        buku["penerbit"] = penerbit
        print("Data penerbit berhasil ditambahkan.")

    elif pilihan == "3":
        penulis_baru = input("Masukkan nama penulis baru: ")
        buku["penulis"] = penulis_baru
        print("Data penulis berhasil diubah.")

    elif pilihan == "4":
        if "penerbit" in buku:
            del buku["penerbit"]
            print("Data penerbit berhasil dihapus")
        else:
            print("Data penerbit belum ada.")

    elif pilihan == "5":
        print("\nProgram selesai.")
        print("Data Buku Setelah Perubahan:")
        print(buku)
        break

    else:
        print("Pilihan menu tidak tersedia.")