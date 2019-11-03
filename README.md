# Pengertian Kondisi If Else If Bahasa Python
  Pada dasarnya, kondisi If Else If adalah sebuah struktur logika program yang di dapat dengan cara menyambung beberapa kondisi If Else menjadi sebuah kesatuan.
  Jika kondisi pertama tidak terpenuhi atau bernilai False, maka kode program akan lanjut ke kondisi If di bawahnya. Jika ternyata tidak juga terpenuhi, akan lanjut lagi ke kondisi If di bawahnya, dst hingga blok Else terakhir atau terdapat kondisi If yang bernilai True.


## yang pertama kita akan membuat contoh bilangan yang memasukin bilangan satu sampai tiga

  Bilangan1 = int(input("Masukkan Bilangan 1:"))
  Bilangan2 = int(input("Masukkan Bilangan 2:"))
  Bilangan3 = int(input("Masukkan Bilangan 3:"))


# Berikutnya kita juga bisa membuat kondisi if int(Bilangan1) and (Bilangan1 > Bilangan3): seperti dibawah ini :
 print("Nilai terbesarnya adalah :", Bilangan1)
    Terbesar = Bilangan1
    NomBil = "Bilangan 1"


# Selanjutnya kita juga bisa membuat kondisi elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1): Seperti dibawah ini:
   print("Nilai terbesarnya adalah :", Bilangan2)
    Terbesar = Bilangan2
    NomBil = "Bilangan 2"

  else:
    Terbesar = Bilangan3
    NomBil = "Bilangan 3"
    
# Selanjutnya menggunakan bilangan besar adalah
print("Bilangan yang terbesar adalah", NomBil, "dengan nilai", Terbesar)
![ss nombil](https://user-images.githubusercontent.com/56245966/68082495-24380280-fe50-11e9-8ec6-d2c9b351abc6.png)

 
# Selanjutnya kita mengetahui setelah RUN yang benar:
![ss pycharm](https://user-images.githubusercontent.com/56245966/68082693-42066700-fe52-11e9-82d3-d6b0438817ef.png)





 Pada if segment diatas memiliki ketentuan nilai if pertama harus bernilai true barulah nilai if yang berikutnya yang akan di proses atau dieksekusi, namun jika nilai if pertama bernilai false maka nilai if yang berikutnya tidak akan di proses, namun jika nilai if yang pertama bernilai true sedangkan nilai if yang kedua bernilai false maka yang akan di proses hanyalah if yang pertama. Berikut hasilnya jika if segment yang kita masukan bernilai true :


selanjutnya kita juga bisa menambahkan is dan is not pada if segment seperti dibawah ini :

Pada Bahasa pemrograman python untuk membuat sebuah kondisi sama halnya dengan Bahasa pemgraman yang lain yaitu sama-sama menggunakan if, pada setiap pemrograman if berisi sebuah ekspresi logika menggunakan sebuah data yang telah dibandingkan seperti alur flowchart dibawah ini.

![ss pemrograman](https://user-images.githubusercontent.com/56245966/67922398-3bbb8500-fbdd-11e9-9ab6-31f46cebce86.png)

