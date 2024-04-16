

# region Example
class Motorcycle:
    marka = ''
    model = ''
    tork = 0
    beygir = 0
    agirlik = 0


m1 = Motorcycle()
m1.marka = 'KTM'
m1.model = '1390 Super Duke R'
m1.tork = 140
m1.beygir = 190
m1.agirlik = 190
print(f'Marka: {m.marka}\n'
        f'Model: {m.model}\n'
        f'Tork: {m.tork}nm\n'
        f'Beygir: {m.beygir}hp\n'
        f'Ağırlık: {m.agirlik}kg')




m2 = Motorcycle()
m2.marka = 'Yamaha'
m2.model = 'R7'
m2.tork = 68
m2.beygir = 75
m2.agirlik = 190
print(f'Marka: {m2.marka}\n'
        f'Model: {m2.model}\n'
        f'Tork: {m2.tork}nm\n'
        f'Beygir: {m2.beygir}hp\n'
        f'Ağırlık: {m2.agirlik}kg')
# endregion


# region __init()__ fonksiyonu ilgili sınıfı kullanıma hazırlar. RAM'in heap bölgesinde tutulur.
class Boxer:
    takma_ad = ''  # sınıfın attributesi (özelliği)

    def __init__(self, ad: str, soyad: str, yas: int):
        # "ad", "soyad" ve "yas" objeninin attributesidir.
        self.ad = ad
        self.soyad = soyad
        self.yas = yas


b1 = Boxer('Mike', 'Tyson', 60)  # b1 adlı objede sınıftan yani prototipten geldiği için içinde takma_ad görülebilir ancak Boxer adlı sınıfta objedeki ad, soyad ve yas görünemez.
print(dir(Boxer))  # takma_ad
print(dir(b1))  # ad, soyad, yas, takma_ad
# endregion


# region # Daire isminde bir sınıf yarat
# # pi adında class attribute olsun
# # yaricap adında bir object attribute olsun
# # alan ve çevre hesaplama fonksiyonları olsun

class Daire:
    pi = 3.14

    def __init__(self, yaricap: float):
        self.yaricap = yaricap


    def alan(self):
        return self.pi * self.yaricap ** 2


    def cevre(self):
        return 2 * self.pi * self.yaricap


yaricap = float(input("Yarı çapı giriniz:"))
d1 = Daire(yaricap)
print(f'Çevre: {d1.cevre()}')
print(f'Alan: {d1.alan()}')
# endregion


# region Departman adında bir sınıf oluştur
# departman_adi ve calisan_sayisi class attribute olsun.
# ad, yas object attribute olsun.
# bilgileri_goster() olsun.
# calisan_sayisi_goster() fonksiyonu olsun. Departman sınıfından her instance alındığında calisan_sayisi 1 arttırılsın ve bu arttırma işleminin sonucu ekrana yazılsın

class Departman:
    departman_adi = 'Yazılım Geliştiricisi'
    calisan_sayisi = 0

    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas
        self.bilgileri_goster()
        self.calisan_sayisi_goster()
        Departman.calisan_sayisi += 1  # calisan_sayisi Departman sınıfı attributesi olduğundan ve orada yer aldığından oradan güncellenebileceği için Departman sınıfından çağırıp güncelledik.


    def bilgileri_goster(self):
        print(f'Adı: {self.ad}\n'
                f'Yaşı: {self.yas}\n'
                f'Çalıştığı Departman: {self.departman_adi}')


    def calisan_sayisi_goster(self):
        print(f'Toplam çalışan sayısı: {self.calisan_sayisi}')

D1 = Departman('Bora', 22)
D2 = Departman('Mehmet', 34)
# endregion


# region # Software Developer adında bir class yarat.
# # ad, soyad, object attribute olsun
# # bilinen_diller = [] class attribute olsun.
# # bilgi_goster() fonksiyonu olsun.
# # yeni_dil_ekle() yeteneği olsun. lakin bazen bir dil bazen de birden fazla dil girebilsin
# # example input => python
# # example input => python, c#, vb
# # listenin içine her biri ayrı ayrı item olarak girsin.

class Software_Developer:
    bilinen_diller = []

    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad


    def bilgi_goster(self):
        print(f'Kişi Bilgisi: {self.ad} {self.soyad}\n'
                f'Bilinen Diller: {self.bilinen_diller}')


    def yeni_dil_ekle(self, dil_liste):
        for i in dil_liste:
            self.bilinen_diller.append(i.lstrip())


    def split_diller(self, dil_girisi: str):
        dil_liste = dil_girisi.split(" ")
        return dil_liste





s1 = Software_Developer('Bora', 'Erdem')
diller = input("Dilleri giriniz: ")
dil_listesi = s1.split_diller(diller)
s1.yeni_dil_ekle(dil_listesi)
s1.bilgi_goster()
# endregion


# region Oyun karakteri oluşturup ihtimalleri yap.
from random import choice, randint

class Character:
    def __init__(self, ad, irk, sinif, can, zirh, hasar, level):
        self.ad = ad
        self.irk = irk
        self.sinif = sinif
        self.can = can
        self.zirh = zirh
        self.hasar = hasar
        self.level = level

    def zar(self):
        return randint(1, 20)

    def saldir(self):
        return self.level * self.hasar

    def savun(self):
        return self.level * self.zirh

    def savustur(self, player_1_zar, player_2_zar):
        if player_1_zar > player_2_zar:
            print(f'{self.ad} saldırıyı savuşturdu!')
        elif player_2_zar > player_1_zar:
            print(f'{self.ad} saldırıyı savuşturamadı.')
        else:
            print(f'Her iki oyuncu da anlık olarak sersemledi. Tur sırası sona erdi.')

    def durum_bilgisi(self):
        print(f'{self.ad} adlı oyuncunun bilgileri:\n'
                f'Can: {self.can}\n'
                f'Zırh: {self.zirh}\n'
                f'Hasar: {self.hasar}\n'
                f'Level: {self.level}\n')


def main():
    p1 = Character('Boakhan', 'insan', 'monk', 79, 18, randint(1, 11), 5)
    p2 = Character('Sylvanus', 'ork', 'warlock', 68, 16, randint(4, 15), 5)

    while True:
        try:
            player_1_zar = p1.zar()
            player_2_zar = p2.zar()

            player_2_aksiyonlari = [p2.saldir(), p2.savun()]

            player_1_aksiyon_secimi = input("Aksiyon tipini giriniz (saldır/savun): ").lower()

            if player_1_aksiyon_secimi == 'saldır':
                hasar = p1.saldir()
                if choice(player_2_aksiyonlari) == p2.savun():
                    savun = p2.savun()
                    alinan_hasar = hasar - savun
                    p2.can -= alinan_hasar
                    guncel_p2_can = p2.can - alinan_hasar
                    print(f'{p1.ad} adlı oyuncu {p2.ad} adlı oyuncuya {alinan_hasar} hasar verdi. {p2.ad} adşı oyuncunun kalan canı: {guncel_p2_can}')
                    p1.durum_bilgisi()
                    p2.durum_bilgisi()
                else:
                    print(f'{p2.ad} adlı oyuncu saldırıyı savuşturdu!')

            elif player_1_aksiyon_secimi == 'savun':
                hasar = p2.saldir()
                savun = p1.savun()
                alinan_hasar = hasar - savun
                alinan_hasar -= p1.can
                guncel_p1_can = alinan_hasar - p1.can
                print(f'{p2.ad} adlı oyuncu {p1.ad} adlı oyuncuya {alinan_hasar} hasar verdi. {p1.ad} oyuncunun kalan canı: {guncel_p1_can}')
                p1.durum_bilgisi()
                p2.durum_bilgisi()

            elif player_1_zar == player_2_zar:
                print(f'Karşılıklı hamleler sonucu anlık sersemlediniz. {p1.ad} ve {p2.ad} adlı oyuncular bu turu pass geçtiler.')

            else:
                print('Geçersiz komut. Sadece "saldır" veya "savun" giriniz.')

            if p1.can <= 0:
                print(f'{p2.ad} adlı oyuncu kazandı. Tebrikler..!')
                p2.durum_bilgisi()
                break

            elif p2.can <= 0:
                print(f'{p1.ad} adlı oyuncu kazandı. Tebrikler..!')
                p1.durum_bilgisi()
                break

        except ValueError as err:
            print(f'Lütfen geçerli komutları giriniz..')


main()
# endregion


# region (CRUD) Kategori adında bir classımız olsun.
# kategoriler = {}
# isim, acıklama object attriubuteleri olsun.
# Kategori_Servisi adında bir classımız olsun. Bu sınıf içerisine CRUD operasyonlarını yürütürken ihtiyaç duyulacak fonksiyonları yaz.
# Servisin fonksiyonları => create(), update(), delete(), get_all(), get_by_id()

from uuid import uuid4
from pprint import pprint


kategoriler = {}

class Kategori:

    def __init__(self, isim, aciklama):
        self.isim = isim
        self.aciklama = aciklama
        self.id = uuid4()



class Kategori_Servisi:

    def create(self, kategori_objesi: Kategori):
        kategoriler[str(kategori_objesi.id)] = {
            'isim': kategori_objesi.isim,
            'açıklama': kategori_objesi.aciklama
        }

        print(f'{kategori_objesi.isim} başarıyla oluşturuldu.')



    def get_all(self, kategori_dict):
        pprint(kategori_dict)


    def get_by_id(self, id):
        for i in kategoriler.keys():
            if i == id:
                return kategoriler.get(id)


    def update(self, id, isim, aciklama):
        mevcut_kategori = self.get_by_id(id)

        mevcut_kategori.update({
            'isim': isim,
            'açıklama': aciklama
        })

        print(f'{id} kategori başarıyla güncellenmiştir.')


    def delete(self, id):
        kategoriler.get(id)

        if kategoriler != {}:
            del kategoriler[id]
            print(f'Kategori başarıyla silinmiştir..!')
        else:
            print(f'Böyle bir kategori yok..!')


def main():
    while True:
        servis = Kategori_Servisi()

        islem = input("Yapmak istediğiniz işlemi giriniz: ").lower()

        if islem == 'create':
            kategori_ismi = input("Kategori isimini giriniz: ")
            kategori_acikalamasi = input("Açıklamayı giriniz: ")
            kategori_objesi = Kategori(kategori_ismi, kategori_acikalamasi)
            servis.create(kategori_objesi)
            servis.get_all(kategoriler)

        elif islem == 'get all':
            servis.get_all(kategoriler)

        elif islem == 'get by id':
            id = input("ID: ")
            pprint(servis.get_by_id(id))

        elif islem == 'update':
            id = input("ID: ")
            kategori_ismi = input("Kategori ismi: ")
            kategori_acikalamasi = input("Kategori açıklaması: ")
            servis.update(id, kategori_ismi, kategori_acikalamasi)
            pprint(servis.get_by_id(id))

        elif islem == 'delete':
            id = input("ID: ")
            servis.delete(id)
        else:
            print(f'Doğru işlem türünü giriniz..!')

main()
# endregion


# region Kopek classımız olsun ve köpeğin insan yaşını hesaplayalım. (insan yaşı = köpeğin yaşı * 7)
# 1.Yol
class Kopek:



    def __init__(self, yas):
        self.yas = yas


    def insanyasi(self, insan_yasi_katsayisi = 7):
        return insan_yasi_katsayisi * self.yas


yas = int(input("Yaş:"))
k1 = Kopek(yas)
print(k1.insanyasi())


# 2.Yol
class Kopek:

    insan_yasi_katsayisi = 7

    def __init__(self, yas):
        self.yas = yas


    def insan_carpani(self):
        return self.insan_yasi_katsayisi * self.yas


yas = int(input("Yaş giriniz: "))
kopke = Kopek(yas)
print(kopke.insan_carpani())
# endregion


# region Bir Liste sınıfı oluştur
# ekle(liste): Listeye bir eleman ekle
# cikar(liste): Belirtilen elemanı listeden çıkar eğer listede yoksa hata ver
# toplam_sayi_adedi_sayisi(): Listenin toplam eleman sayısını döndür
# yeni_liste(): Listenin içindeki tüm elemanları döndür

class Liste:

    def __init__(self, yeni_liste):
        self.yeni_liste = yeni_liste

    def ekle(self, sayi):
        self.yeni_liste.append(sayi)

    def cikar(self, sayi):
        if sayi in self.yeni_liste:
            self.yeni_liste.remove(sayi)
        else:
            raise ValueError("Listede böyle bir eleman yok..!")

    def toplam_sayi_adedi(self):
        return len(self.yeni_liste)

    def yeni_liste_icindeki_sayilar(self):
        for sayi in self.yeni_liste:
            print(sayi)

sayi = int(input("Sayı ekle: "))
l1 = Liste([sayi])  # Giriş bir liste olarak alınmalı
print("Toplam sayı adedi:", l1.toplam_sayi_adedi())
# endregion