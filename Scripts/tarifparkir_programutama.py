# Program Utama Parkir
# Memakai fungsi-fungsi dari modul parkir.py (simpan di folder yang sama)

import parkir


# Fungsi untuk meminta input waktu (tanggal + jam) sampai formatnya benar
def input_waktu(label):
    while True:
        tanggal = input("Tanggal " + label + " (dd-mm-yyyy): ")
        jam = input("Jam " + label + " (hh:mm)         : ")
        try:
            waktu = parkir.buat_waktu(tanggal, jam)
            return waktu, tanggal + " " + jam
        except (ValueError, IndexError):
            print("Format tanggal/jam salah, silakan ulangi.")


# Fungsi untuk meminta pilihan jenis kendaraan sampai valid
def input_jenis():
    print("Jenis kendaraan: 1. Becak  2. Motor  3. Mobil")
    while True:
        kode = input("Pilih jenis (1/2/3): ")
        if kode in ("1", "2", "3"):
            return kode
        print("Pilihan tidak valid.")


def main():
    data_parkir = []
    total_pendapatan = 0

    print("=== PROGRAM PARKIR ===")

    lagi = "y"
    while lagi.lower() == "y":
        print("")
        plat = input("Plat nomor: ").upper()
        kode = input_jenis()
        nama_jenis = parkir.cari_nama_jenis(kode)

        # Waktu keluar harus setelah waktu masuk
        while True:
            waktu_masuk, teks_masuk = input_waktu("masuk")
            waktu_keluar, teks_keluar = input_waktu("keluar")
            if waktu_keluar >= waktu_masuk:
                break
            print("Waktu keluar tidak boleh sebelum waktu masuk, ulangi.")

        lama = parkir.hitung_lama(waktu_masuk, waktu_keluar)
        biaya = parkir.hitung_biaya(kode, lama)

        parkir.tampil_struk(plat, nama_jenis, teks_masuk, teks_keluar, lama, biaya)

        data_parkir.append([plat, nama_jenis, teks_masuk, teks_keluar, lama, biaya])
        total_pendapatan = total_pendapatan + biaya

        lagi = input("\nInput kendaraan lagi? (y/n): ")

    if len(data_parkir) > 0:
        parkir.tampil_rekap(data_parkir, total_pendapatan)
    else:
        print("Tidak ada data parkir.")


main()
