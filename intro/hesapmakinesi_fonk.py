while True:

    a = int(input("Birinci sayıyı giriniz "))
    b = int(input ("İkinci sayıyı giriniz "))

    def topla(a,b):
        toplama = a+b
        print(toplama)

    def carp(a,b):
        carpma = a*b
        print(carpma)

    def cikar(a,b):
        cikarma = a-b
        print(cikarma)

    def bol(a,b):
        bolme = a/b
        print(bolme)

    print("1 = toplama")
    print("2 = çıkarma")
    print("3 = çarpma")
    print("4 = bölme")

    x = int(input("Hangi işlemi yapmak istersiniz? "))

    if x==1:
       topla(a,b)
    elif x==2:
       cikar(a,b)
    elif x==3:
        carp(a,b)
    elif x==4:
      bol(a,b)
    
