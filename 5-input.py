
sayi1 = input('Bir sayi giriniz : ')  # klavyeden bir deger almak 

sayi2 = input('Bir sayi giriniz : ')  # klavyeden bir deger almak 

sayi3 = input('Bir sayi giriniz : ')  # klavyeden bir deger almak 
 
toplam = int(sayi1)+int(sayi2)+int(sayi3) # klavyeden girilen degerleri tür donusumu ile topladik

print(toplam) # Klavyeden girilen degerlerin toplamini ekrana yazdirdik.

isim = input('Isim:')  # klavyeden alinan degeri isim degiskenine atadik
soyad = input('Soyad:') # klavyeden alinan degeri soyadi degiskenine atadik.
telno = input('telno:') # klavyeden alinan degeri telno degiskenine atadik.

bilgiler = [isim,soyad,telno]  # klavyeden alinan 3 degeri listeye atadik.

print(bilgiler) # klavyeden alinan degerleri atadigimiz listeyi yazdirdik.

print('Adin: {} \nSoyadin: {}\nTelno:{} \n'.format(bilgiler[0],bilgiler[1],bilgiler[2])) # Klavyeden alinan verileri tek satirda format ozelligi ile yazdirdik.