# import geometri as geo 
from Scripts.matematika.geometri import luasLingkaran, volTabung

def main():
    jari2 = float(input("masukkan jari-jari lingkaran: "))
    tinggi = float (input("masukkan tinggi tabung: "))
    # VolTab = geo.volTabung(geo.luasLingkaran (jari2), tinggi)
    VolTab = volTabung(luasLingkaran(jari2), tinggi)

    print("Volume Tabung ", VolTab)
    
if __name__ == "__name__":
    main ()