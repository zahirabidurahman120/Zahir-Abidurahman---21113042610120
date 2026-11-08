def luasPersegi(panjang, lebar) :
    luas = panjang * lebar
    return luas

def luasLingkaran(jari_jari) :
    pi = 3.14
    luas = pi * (jari_jari ** 2)
    return luas 

def volTabung(luas,tinggi) :
    # volume = luasLingkaran(jari_jari) * tinggi
    volume = luas * tinggi
    return volume

volTab = volTabung(luasLingkaran (7), 10)
print(volTab)