ogrenciler = []
print("Bir Ogrenci Eklemek icin '1', \nOgrencileri Ekrana yazdirmak icin '2', \nOgrenci numarasi ile ogrencileri getirmek icin '3', \nBirden fazla ogrenci silmek icin '4', \n Birden fazla Ogrenci eklemek icin '5', cikmak icin 'q' tusuna basiniz.")
runApp = True
def mainMenu():
    girdi = input("Lutfen yapmak istediginiz islemi seciniz: ")
    if girdi == "1":
        ogrenciEkle()
    elif girdi == "2":
        ogrenciListele()
    elif girdi == "3":
        numara = input("Ogrenci numarasini giriniz: ")
        numara = int(numara)
        numaraIleGetir(numara=numara)
    elif girdi == "4":
        multipleDelete()
    elif girdi == "5":
        multipleAdd()
    elif girdi == "q":
        runApp = False
    else:
        print("Lutfen tekrar secim yapiniz")
    
def ogrenciEkle():
    ogrenci = str(input("Lutfen ogrenci ismini ve soyismini giriniz: "))    
    for i in ogrenciler:
        if i == ogrenci:
            ayniOgrenciSil(girdi=ogrenci,dizi=ogrenciler)
            break
    ogrenciler.append(ogrenci)

def ayniOgrenciSil(girdi, dizi):   
    dizi.remove(girdi)

def ogrenciListele():
    for i in ogrenciler:
        print(i)

def numaraIleGetir(numara):
    print(ogrenciler[numara])

def multipleDelete():
    print("Bir ust menuye cikmak icin 'q ya basiniz.'")
    while True:
        ogrenci = str(input("Silmek istediginiz ogrenci isim ve soyismini giriniz: "))
        if(ogrenci != "q"):
            ogrenciler.remove(ogrenci)
        else:
            break

def multipleAdd():
    print("Bir ust menuye cikmak icin 'q ya basiniz.'")
    while True:
        ogrenci = str(input("Eklemek istediginiz ogrenci isim ve soyismini giriniz: "))
        if(ogrenci != "q"):
            ogrenciler.append(ogrenci)
        else:
            break

while runApp:
    mainMenu()


