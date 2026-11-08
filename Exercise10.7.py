while True:
    print("\nKalkulator Penjumlahan")
    print("Ketik q untuk keluar.")

    angka1 = input("Masukkan angka pertama: ")

    if angka1.lower() == "q":
        break

    angka2 = input("Masukkan angka kedua: ")

    if angka2.lower() == "q":
        break

    try:
        hasil = int(angka1) + int(angka2)
        print("Hasil:", hasil)

    except ValueError:
        print("Input salah! Harap masukkan angka.")