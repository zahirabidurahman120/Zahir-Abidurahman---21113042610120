# Modul Parkir
# Berisi fungsi-fungsi untuk menghitung tarif parkir
#
# Ketentuan tarif:
# Becak : flat Rp 1000
# Motor : masuk Rp 2000 (s.d. 2 jam), progresif Rp 1000/jam, maksimal Rp 10000, inap Rp 15000
# Mobil : masuk Rp 4000 (s.d. 2 jam), progresif Rp 2000/jam, maksimal Rp 15000, inap Rp 20000
#
# Aturan lain:
# - Lama parkir dihitung dari selisih tanggal dan jam masuk dengan keluar
# - Kelebihan menit dibulatkan ke atas menjadi 1 jam
# - Setiap 24 jam dihitung 1x tarif INAP, sisa jamnya dihitung tarif biasa

import datetime


# Fungsi untuk mengubah kode jenis menjadi nama jenis
def cari_nama_jenis(kode):
    if kode == "1":
        return "Becak"
    elif kode == "2":
        return "Motor"
    elif kode == "3":
        return "Mobil"
    else:
        return "Tidak dikenal"


# Fungsi untuk membuat waktu dari teks tanggal dan jam
def buat_waktu(tanggal, jam):
    pecah_tanggal = tanggal.split("-")
    pecah_jam = jam.split(":")

    hari = int(pecah_tanggal[0])
    bulan = int(pecah_tanggal[1])
    tahun = int(pecah_tanggal[2])
    jam_masuk = int(pecah_jam[0])
    menit = int(pecah_jam[1])

    waktu = datetime.datetime(tahun, bulan, hari, jam_masuk, menit)
    return waktu


# Fungsi untuk menghitung lama parkir (dalam jam) dari waktu masuk dan keluar
def hitung_lama(waktu_masuk, waktu_keluar):
    selisih = waktu_keluar - waktu_masuk
    detik = selisih.total_seconds()

    lama = int(detik // 3600)       # jam penuh
    if detik % 3600 > 0:            # ada sisa menit, dibulatkan ke atas
        lama = lama + 1
    return lama


# Fungsi menghitung tarif becak (flat)
def hitung_becak():
    biaya = 1000
    return biaya


# Fungsi menghitung tarif motor
def hitung_motor(lama):
    hari = lama // 24               # jumlah 24 jam penuh (inap)
    sisa = lama % 24                # sisa jam

    biaya = hari * 15000            # tarif inap

    if sisa > 0:
        if sisa <= 2:
            biaya_sisa = 2000       # tarif masuk
        else:
            biaya_sisa = 2000 + (sisa - 2) * 1000   # tarif progresif

        if biaya_sisa > 10000:      # tarif maksimal < 24 jam
            biaya_sisa = 10000

        biaya = biaya + biaya_sisa
    return biaya


# Fungsi menghitung tarif mobil
def hitung_mobil(lama):
    hari = lama // 24               # jumlah 24 jam penuh (inap)
    sisa = lama % 24                # sisa jam

    biaya = hari * 20000            # tarif inap

    if sisa > 0:
        if sisa <= 2:
            biaya_sisa = 4000       # tarif masuk
        else:
            biaya_sisa = 4000 + (sisa - 2) * 2000   # tarif progresif

        if biaya_sisa > 15000:      # tarif maksimal < 24 jam
            biaya_sisa = 15000

        biaya = biaya + biaya_sisa
    return biaya


# Fungsi utama untuk menghitung biaya sesuai jenis kendaraan
def hitung_biaya(jenis, lama):
    if jenis == "1":
        biaya = hitung_becak()
    elif jenis == "2":
        biaya = hitung_motor(lama)
    else:
        biaya = hitung_mobil(lama)
    return biaya


# Prosedur untuk menampilkan struk (tidak ada return)
def tampil_struk(plat, nama_jenis, masuk, keluar, lama, biaya):
    print("")
    print("-------- STRUK PARKIR --------")
    print("Plat nomor  : " + plat)
    print("Jenis       : " + nama_jenis)
    print("Masuk       : " + masuk)
    print("Keluar      : " + keluar)
    print("Lama parkir : " + str(lama) + " jam")
    print("Biaya       : Rp " + str(biaya))
    print("------------------------------")


# Prosedur untuk menampilkan rekap seluruh kendaraan (tidak ada return)
def tampil_rekap(data_parkir, total_pendapatan):
    print("")
    print("================ REKAP PARKIR ================")
    print("Plat\t Jenis\t Masuk\t\t\t Keluar\t\t\t Lama\t Biaya")
    for data in data_parkir:
        print(data[0], "\t", data[1], "\t", data[2], "\t", data[3], "\t", data[4], "\t", data[5])
    print("==============================================")
    print("Jumlah kendaraan :", len(data_parkir))
    print("Total pendapatan : Rp", total_pendapatan)