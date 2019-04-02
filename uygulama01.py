__author__ = "NURETTİN ŞEN"
Duyuru = "Sınava hoşgeldiniz... Eğlenceye hazır mısınız? "
print ("Yazar adı : {} \nSınav duyurusu : {}".format(__author__, Duyuru))
adsoyad = input("Ad ve soyad : ")
print(adsoyad, "Sınava Başlayabilirsiniz.")
# Sınav Soruları
SORU1 = "### Ülkemiz Avrupa Birliğine tam üyelik müzakerelerine 2007 yılında başlamıştır. [D/Y] ###" # CEVAP 2005 OLACAK
SORU2 = "### Pusulada ( N ) harfi Doğu yönünü gösterir. [D/Y] ### " # CEVAP KUZEY OLACAK
SORU3 = "### İstiklal Marşımızın bestecisi Mehmet Akif Ersoy'dur. [D/Y] ### " # CEVAP Osman Zeki Üngör OLACAK
SORU4 = "### Şubat Ayı 2 yılda bir 29 çeker. [D/Y] ### " # CEVAP 4 OLACAK
SORU5 = "### Elektrik akımı ölçü birimi amperdir. [D/Y] ### " # DOĞRU CEVAPTIR
sonucpuan = 0

# SINAV BÖLÜMÜ
S1 = input(SORU1)
if S1 == "Y" or S1 == "y":
    print ("Cevabınız DOĞRU...!")
    print()
    sonucpuan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()
S2 = input(SORU2)
if S2 == "Y" or S2 == "y":
    print("Cevabınız DOĞRU...!")
    print()
    sonucpuan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()
S3 = input(SORU3)
if S3 == "Y" or S3 == "y":
    print("Cevabınız DOĞRU...!")
    print()
    sonucpuan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()
S4 = input(SORU4)
if S4 == "Y" or S4 == "y":
    print("Cevabınız DOĞRU...!")
    print()
    sonucpuan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()
S5 = input(SORU5)
if S5 == "D" or S5 == "d":
    print("Cevabınız DOĞRU...!")
    print()
    sonucpuan += 1
else:
    print("Cevabınız YANLIŞ...!")
    print()

print (" SINAV SONA ERDİ... SONUCUNUZ : " , str(sonucpuan*20))