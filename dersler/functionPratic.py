# GONDERILEN BİR KELİMEYİ BELİRTİLEN KEZ EKRANDA GOSTEREN FONKSIYONU YAZIN

def ekranaYazdir(yazdirilacakDeger,yazdirilmaMiktari):
    while yazdirilmaMiktari>0:
        yazdirilmaMiktari=yazdirilmaMiktari-1
        print(yazdirilacakDeger)

ekranaYazdir("Umut",10)

# KENDİNE GÖNDERİLEN SINIRSIZ SAYIDAKİ PARAMETREYİ BİR LİSTEYE CEVİREN FONKSİYONU YAZALIM

def listConventer(*eklenecekSayi):
    numList=[]
    for sayi in eklenecekSayi:
       numList.append(sayi)
    return numList
x=listConventer(10,20,30,40,50)

print(x)

y=listConventer(10,20,30)
print(y)