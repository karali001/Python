# -*- coding: cp1254 -*-

def kayit_olustur(isim1,soyisim1,isis1,sehir1):

    isim1    = "F�rat"
    soyisim1 = "�zg�l"
    isis1   = "Ubuntu"
    sehir1   = "�stanbul"

    print("isim           : ", isim1)
    print("soyisim        : ", soyisim1)
    print("i�letim sistemi: ", isis1)
    print("�ehir          : ", sehir1)

    print("-"*30)

isim2    = "Mehmet"
soyisim2 = "�ztaban"
isis2   = "Debian"
sehir2   = "Ankara"

print("isim           : ", isim2)
print("soyisim        : ", soyisim2)
print("i�letim sistemi: ", isis2)
print("�ehir          : ", sehir2)

print("-"*30)


"""-----------------------------------------------------------------"""

def sistem_bilgisi_g�ster():
    import sys
    print("\nSistemde kurulu Python'�n;")
    print("\tana s�r�m numaras�:", sys.version_info.major)
    print("\talt s�r�m numaras�:", sys.version_info.minor)
    print("\tminik s�r�m numaras�:", sys.version_info.micro)

    print("\nKullan�lan i�letim sisteminin;")
    print("\tad�:", sys.platform)
