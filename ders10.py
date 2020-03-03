"""YÜK.BİLGİSAYAR MÜHENDİSİ ENES KARALİ BYS GİRİŞ SAYFASI"""
defkullanıcı="karali001"
defparalo="trabzonrize6153"

kullanıcı = input("Enes bey kullanıcı adınızı giriniz:")
paralo =input("Enes bey paralonızı giriniz:")

if ((defparalo==paralo) and (defkullanıcı==kullanıcı)):
    print("YÜK.BİLGİSAYAR MÜHENDİSİ Enes bey sisteme hoşgeldiniz.")
elif((defparalo==paralo) and (defkullanıcı!=kullanıcı)):
     print("Enes bey kullanıcı adınızı yanlış girdiniz!")
elif((defparalo !=paralo) and (defkullanıcı==kullanıcı)):
     print("Enes bey paralonuzu yanlıs gırdınız!")
else:
     print("Hatalı giriş,Enes beye bildirileceksiniz.")
print("KARADENİZ TEKNİK ÜNİVERSİTESİ\n YÜK. BİLGİSAYAR MÜHENDİSİ ENES KARALİ")
