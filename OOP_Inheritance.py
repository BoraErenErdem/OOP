

# from socket import gethostname, gethostbyname  #  socket modülü ağ programlaması için kullanılır. Soketler ağdaki iki cihaz arasında veri alışverişi yapmak için kullanılan iletişim araçlarıdır.


# gethostname() yerel makinenin adını (hostname) döndürür. Yerel bilgisayarın adı genellikle kullanıcı tarafından belirlenir veya işletim sistemi tarafından atanır. Bu işlev bilgisayarın adını belirlemek için kullanışlıdır ve genellikle ağda benzersiz bir tanımlayıcı olarak kullanılır.


# gethostbyname() bir alan adı veya bir IP adresi ile ilişkilendirilmiş olan IP adresini döndürür. Örneğin bir alan adı verildiğinde bu işlev o alan adının IP adresini döndürür. Eğer verilen bir IP adresi ise, aynı IP adresini döndürür.




# NOT: Bazen alt sınıfta (child class) yapılan değişikler üst sınıfta (Ata class) yapılan değişikliklerin üstüne yazılır. Buna "Overriding" denir. Yani bir sınıfa ait methodun o sınıftan türetilmiş bir alt sınıf içerisine aynı isimli method tanımlanarak, temel sınıftaki methodun yerine geçmesine denir. Bu işlemin en büyük avantajı ise bir metodun aynı sınıftan türetilmiş farklı sınıflarda farklı işlere yaramasını sağlar. (Alt sınıftaki method temel sınıftaki methodu ezer)




# region Ata Sınıf ve çocuk sınıflar
class Insan:  # Ata class

    def __init__(self, boy, kilo, lakap):
        self.boy = boy
        self.kilo = kilo
        self.lakap = lakap


    def bilgileri_goster(self):
        return self.__dict__




class Archer(Insan):  # Child class

    def __init__(self, boy, kilo, lakap, isabet):
        super().__init__(boy, kilo, lakap)  # super() fonksiyonu üst sınıftaki yani ata sınıfaki fonksiyonları çağırmaya yarar. Eğer bu alt sınıfa yeni bir parametre vermek istersen alt                                            sınıftaki def __init()__ içine yazıp self ile tanımlamalısın!! (isabet gibi) ya da (bilgi gibi)
        self.isabet = isabet


class Mage(Insan):  # Child class

    def __init__(self, boy, kilo, lakap, bilgi):
        super().__init__(boy, kilo, lakap)
        self.bilgi = bilgi



a1 = Archer(1.85, 81, 'sniper', '%90')
print(a1.bilgileri_goster())

m1 = Mage(1.72, 63, 'ölüm büyücüsü', '+4')
print(m1.bilgileri_goster())
# endregion


# region Çalışan objesi için CRUD işlemleri yap
# BaseEntity ata sınıf

from enum import Enum  # belirli değerleri sınırlandırır ve sabitler, kullanışlıdır
from datetime import datetime  # tarih ve saat işlemleri için kullanılan modüldür
from uuid import uuid4
from socket import gethostname, gethostbyname  # socket modülü ağ programlaması için kullanılır. Soketler ağdaki iki cihaz arasında veri alışverişi yapmak için kullanılan iletişim araçlarıdır.

class Durum(Enum):
    Aktif = 1
    Degistirilmis = 2
    Pasif = 3


class BaseEntity:
    def __init__(self, isim, soyisim, departman):
        self.isim = isim
        self.soyisim = soyisim
        self.departman = departman
        self.id = str(uuid4())
        self.durum = Durum.Aktif.name
        self.ip_adresi_yarat = gethostbyname(gethostname())
        self.bilgisayar_ismi_yarat = gethostname()


class Calisan(BaseEntity):
    pass


class Calisan_Servis:

    calisanlar = []

    def create(self, calisan: Calisan):
        self.calisanlar.append(calisan)
        print(f'{calisan.isim} {calisan.soyisim} başarıyla oluşturuldu.')


    def get_all(self):
        for i in self.calisanlar:
            print(i.__dict__)  # sözlük olarak getirmesini istediğmiz için böyle yaptık __dict__()


    def get_by_full_name(self, tamisim):
        for i in self.calisanlar:
            if f"{i.isim} ve {i.soyisim}".lower() == tamisim:
                print(i.__dict__)


    def pasif_olma_durumu(self):
        pasif_calisanlar = []
        for i in self.calisanlar:
            if i.durum == 'Aktif' or i.durum == 'Değiştirilmiş':
                print(i.__dict__)
            else:
                pasif_calisanlar.append(i.__dict__)
        return pasif_calisanlar



def main():
    servis = Calisan_Servis()

    while True:

        islem = input("Yapmak istediğiniz işlemi seçiniz: ").lower()

        if islem == 'create':
            isim = input("isim:")
            soyisim = input("soyisim:")
            departman = input("departman:")
            calisan = Calisan(isim, soyisim, departman)
            servis.create(calisan)


        elif islem == 'get all':
            servis.get_all()


        elif islem == 'get by name':
            tamisim = input("Tam isim: ")
            servis.get_by_full_name(tamisim)


        elif islem == 'aktivite durumu':
            print(servis.pasif_olma_durumu())


        elif islem == 'çıkış':
            print(f'Sistemden çıkılıyor..')
            break


        else:
            print(f'Lütfen doğru parametreyi giriniz..!')

main()
# endregion


# region Belirli bir ürün olsun. BaseEntitiy den kalıtım alsın, Product adında class olsun, fiyat ve stok bilgileri object attribute olsun.
from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum


class Status(Enum):
    Aktif = 1
    Modifiye = 2
    Pasif = 3


class BaseEntity:
    def __init__(self, isim, aciklama):
        self.isim = isim
        self.aciklama = aciklama
        self.id = str(uuid4())
        self.ip_adres_yarat = gethostbyname(gethostname())
        self.makine_adi_yarat = gethostname()
        self.status = Status.Aktif.name


    def bilgileri_goster(self):
        print(f'ID: {self.id}\n'
                f'İsim: {self.isim}\n'
                f'Açıklama: {self.aciklama}')



class Kategori(BaseEntity):
    pass


class Product(BaseEntity):
    def __init__(self, isim, aciklama, stok, fiyat):
        super().__init__(isim, aciklama)
        self.stok = stok
        self.fiyat = fiyat
    
    
    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f'Stok Durumu: {self.stok}\n'
                f'Fiyat: {self.fiyat}')


k1 = Kategori('Motor Gidonu', 'En sağlam ve ucuz motor gidonu')
k1.bilgileri_goster()

p1 = Product('Motor Lastiği', 'Orta yumuşaklıkta V kenarlı 3 katmanlı kauçuk motor lastiği', 20, 15000)
p1.bilgileri_goster()
# endregion


# region BasePhone adında bir ata sınıf oluşturalım. phone_id, marka, model, fiyat attribute'leri olsun.
# # bilgileri_goster() fonksiyonu olsun. telefon_zil_sesi() fonksiyonu 'genel telefon sesi' string ifadesini return etsin.
# # Samsung adında bir sınıf oluşturalım. BasePhone kalıtım alıcak. operating_system attribute olsun. phone_ring_sound() 'samsung telefon sesi' return etsin.
# # İphone adında bir sınıf oluşturalım. BasePhone kalıtım alıcak. camera attribute olsun. phone_ring_sound() 'iphone telefon sesi' return etsin.
# # Huaweie adında bir sınıf oluşturalım. BasePhone kalıtım alıcak. anten attribute olsun. phone_ring_sound() 'huaweie telefon sesi' return etsin.


class BasePhone:

    def __init__(self, phone_id, marka, model, fiyat):
        self.phone_id = phone_id
        self.marka = marka
        self.model = model
        self.fiyat = fiyat


    def bilgileri_goster(self):
        print(f'Telefon Seri No: {self.phone_id}\n'
                f'Marka: {self.marka}\n'
                f'Model: {self.model}\n'
                f'Fiyat: {self.fiyat}')


    def telefon_zil_sesi(self):
        return f"genel telefon sesi"



class Samsung(BasePhone):

    def __init__(self, phone_id, marka, model, fiyat, isletim_sistemi):
        super().__init__(phone_id, marka, model, fiyat)
        self.isletim_sistemi = isletim_sistemi


    def telefon_zil_sesi(self):
        return f"samsung telefon sesi"


    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f'İşletim Sistemi: {self.isletim_sistemi}')



class Iphone(BasePhone):

    def __init__(self, phone_id, marka, model, fiyat, kamera):
        super().__init__(phone_id, marka, model, fiyat)
        self.kamera = kamera


    def telefon_zil_sesi(self):
        return f"iphone telefon sesi"


    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f'Kamera: {self.kamera}')



class Huaweie(BasePhone):

    def __init__(self, phone_id, marka, model, fiyat, kg):
        super().__init__(phone_id, marka, model, fiyat)
        self.kg = kg


    def telefon_zil_sesi(self):
        return f"huaweie telefon sesi"


    def bilgileri_goster(self):
        super().bilgileri_goster()
        print(f'Kg: {self.kg}')



s1 = Samsung(1, 'Samsung', 'Galaxy S24', 80000, 'Android')
print(s1.telefon_zil_sesi())
s1.bilgileri_goster()

i1 = Iphone(2, 'İphone', '15 Pro Max', 92000, '5x')
print(i1.telefon_zil_sesi())
i1.bilgileri_goster()

h1 = Huaweie(3, 'Huaweie', 'MatePhone 12', 65000, '1 kg')
print(h1.telefon_zil_sesi())
h1.bilgileri_goster()
# endregion


# region BaseFatura sınıfımız olsun. fatura_adi, vergi, miktar attribute sahip olsun. fatura_hesapla ve create_log fonksiyonları olsun.
# log'lar bill_info.txt dosyasına yazılsın. fatura_adi ve toplam_miktar yazmanız ve tarih yeterli
# Su_Faturasi, Elektrik_Faturasi, Dogal_Gaz_Faturasi child classlarımız
# fatura_hesapla() miktar * vergi
# su faturasının mill adında özelliği olsun
# elektrik kw adında bir özelliği olsun
# doğalgaz m3 adında bir özelliği olsun

from datetime import datetime

class BaseFatura:

    def __init__(self, fatura_adi, vergi, miktar):
        self.fatura_adi = fatura_adi
        self.vergi = vergi
        self.miktar = miktar


    def fatura_hesapla(self):
        return self.miktar * self.vergi


    def create_log(self):
        with open(file="bill_info.txt", mode="a", encoding="utf-8") as file:
            file.write(f"{self.fatura_adi} ***** Toplam Miktar: {self.fatura_hesapla()} ******** Tarih: {datetime.now()}\n")


class Su_Faturasi(BaseFatura):

    def __init__(self, fatura_adi, vergi, miktar, mill):
        super().__init__(fatura_adi, vergi, miktar)
        self.mill = mill

    def fatura_hesapla(self):
        return  super().fatura_hesapla() + self.mill
    
    
    def create_log(self):
        super().create_log()
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f"{self.fatura_adi} ******** Toplam Miktar: {self.fatura_hesapla()} ********** Mill: {self.mill} *********** Tarih: {datetime.now()}\n")





class Elektrik_Faturasi(BaseFatura):

    def __init__(self, fatura_adi, vergi, miktar, kw):
        super().__init__(fatura_adi, vergi, miktar)
        self.kw = kw

    def fatura_hesapla(self):
        return super().fatura_hesapla() + self.kw

    def create_log(self):
        super().create_log()
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f"{self.fatura_adi} ******** Toplam Miktar: {self.fatura_hesapla()} ********** Kw: {self.kw} ******** Tarih: {datetime.now()}\n")





class Dogal_Gaz_Faturasi(BaseFatura):

    def __init__(self, fatura_adi, vergi, miktar, m3):
        super().__init__(fatura_adi, vergi, miktar)
        self.m3 = m3

    def fatura_hesapla(self):
        return super().fatura_hesapla() + self.m3

    def create_log(self):
        super().create_log()
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f"f{self.fatura_adi} ********** Toplam Miktar: {self.fatura_hesapla()} ********* m3: {self.m3} ********** tarih: {datetime.now()}\n")





s1 = Su_Faturasi('ISKI', 0.21, 100, 51)
print(s1.fatura_hesapla())
s1.create_log()

e1 = Elektrik_Faturasi('AkdenizElektrik', 0.8, 200, 18)
print(e1.fatura_hesapla())
e1.create_log()

d1 = Dogal_Gaz_Faturasi('IGDAS', 0.28, 250, 180)
print(d1.fatura_hesapla())
d1.create_log()
# endregion