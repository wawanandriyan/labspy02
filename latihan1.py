Bilangan1 = int(input("Masukan Bilangan 1:"))
Bilangan2 = int(input("Masukan Bilangan 2:"))
Bilangan3 = int(input("Masukan Bilangan 3:"))

if int(Bilangan1) and (Bilangan1 > Bilangan3):
    print("Nilai terbesar adalah:", Bilangan1)
    Terbesar = Bilangan1
    nomBil = "Bilangan 2"
elif (Bilangan2 > Bilangan3) and (Bilangan2 > Bilangan1):
    print("Nilai terbesarnya adalah:", Bilangan2)
    Terbesar = Bilangan2
    nomBil = "Bilangan 2"
else:
    Terbesar = Bilangan3
    nomBil = "Bilangan 3"

    print("Bilangan yang terbesar adalah", NomBil, "dengan nilai", Terbesar)



