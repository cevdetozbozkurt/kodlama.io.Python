### Soru 1 : pythonda veri tipleri ###

x = 1 # int, integer yani tam sayilari ifade eder, 32 bitlik sayilari tutabilir yani alabeilcegi max deger 2147483647
x = 2147483641234 # long turunde bir sayidir, uzun tam sayilari ifade eder.
x = 3.14 # float ondalik sayilari ifade eder. 64 bit uzunluga ve hassasiyete sahiptir.
x = "Hello World!" # str , string ; karakterlerden olusan dizileri temsil eder. Kisaca metinsel veriler.
x = True # bool True veya False degerini alir dogru veya yanlis olan veri kontrol eder. Karar yapilarinda kullanilir.
x = complex(1j) # karmasik sayilar icin kullanilir. tam sayilari karmasik sayiya donusturur.
x = ["Hello","World"] # Array; liste, dizi  yapisi icerisinde birden fazla eleman tutabilir 
x = list(("Merhaba")) # liste bu sekilde de kullanilabilir.
x = (1,2,3,4) # tuple (demet) demetlerde ekleme cikarma mevcut degildir.
x = {1,2,3,4} # set veri tipi ayni tipteki verileri bir den fazla depolamak icindir.
x = {"brand" : "Ford", "model" : "Mustang", "year":1964} # dictionaries (kutuphaneler), anahtar kilit mantigi ile calisir. Anahtara karsilik gelen bir veri vardir. 

### Soru 2 ###

x = "Odev 1" #baslik olarak verilmistir str tipinde bir degiskendir.
x = 100 #tamamlanma yuzdesi int bir degerdir.

### Soru 3 ### 
# bir kursa kayit olmak icin tiklandiginda true veya false dondurur ve kayit islemi yapilir.
derseKayitliMi = False
if(derseKayitliMi):
    print("Derse zaten kayitlisiniz.")
else:
    print("Derse kayitli degilsiniz.")


