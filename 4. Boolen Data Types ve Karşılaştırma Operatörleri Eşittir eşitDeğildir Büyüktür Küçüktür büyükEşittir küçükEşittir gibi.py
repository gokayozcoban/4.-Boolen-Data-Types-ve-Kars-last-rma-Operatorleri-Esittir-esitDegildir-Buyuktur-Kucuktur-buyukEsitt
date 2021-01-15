
# Boolean Data Types (Boolean Veri Tipleri)
# Karşılaştırma Operatörleri > < == != >= <= 

# True ve False sonucunu döndüren veri tipleridir.
# True, Python'da 1 değerli olarak kabul edilir:
print(True + True)
2

# False ise Python'da 0 olarak kabul edilir:
print(8 * False)
0

# Karşılaştırma Operatörleri üzerinde anlatırsak:
print(5 > 4, 5 < 4)
True False
print(5 == 5, 5 == 4) # == işareti değişken tanımlarken kullanılan = ifadesi ile
True False            #karıştırılmasın diye kullanılmış.
print(6 != 5, 4 != 4) # != işareti, "eşit değildir" anlamına gelir.
True False
print(6 >= 5, 6 >= 7) # >= işareti, "büyük veya eşittir" anlamına gelir.
True False
print(7 <= 7, 7 <= 6) # <= işareti, "küçük veya eşittir" anlamına gelir.

# Yukarıdaki kodların hepsi de True False olarak çıktı.

# True ve False Boolean Data Type'ları matematiksel işlemleri kullanarak da
# deneyebiliriz:
print(True * 5 + 5)
10
# True'yu 1 kabul etti, 5 ile çarptı, 5 sonucunu verdi ve 5 ile topladı.

print(False * 5 + 5)
5
# False'ı 0 kabul etti, 5 ile çarptı, 0 sonucunu verdi, 0 ile 5'i topladı.
