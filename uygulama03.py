__author__ = "Nurettin Şen"
#Adam Asmaca
print("Oyunumuza Hoşgeldiniz")

import random

sectigimizKelime = random.choice(["monitör", "mouse", "klavye", "yazıcı", "kasa", "fan", "harddisk", "anakart", "flashbellek", "işlemci"])
can_sayisi = 5
pano = []
cizgi = "_"

print("Adam Asmaca oyununa hoşgeldiniz..\n")

for kelime in sectigimizKelime:

    pano.append(cizgi)

print(pano)

while can_sayisi > 0:

    i = 0

    girdi = input("\nBir harf giriniz: ").lower()

    if girdi in sectigimizKelime:
        for kontrol in sectigimizKelime:
            if sectigimizKelime[i] == girdi:
                pano[i] = girdi
            i += 1

        print("")
        print(pano)
        print("\n \"%s\" harfi doğru tahmin!" %girdi)

    else:
        can_sayisi -= 1
        print("")
        print(pano)
        print("\n\"%s\" harfi yanlış tahmin. oynamaya devam et bulabilirsin :)" % girdi)
        print("\nKalan can sayısı = " + "[" + can_sayisi * " ♥ " + "] = " + str(can_sayisi))

    if can_sayisi == 0:
        print("Başaramadın! Doğru cevap: %s" %sectigimizKelime)
        break

    if cizgi not in pano:
        print("\nTebrikler! Kelimeyi buldun!")
        break

