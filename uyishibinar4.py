def bank(depozit,foiz,yil):
    a=depozit+((depozit/100*foiz)*yil)
    return int(a)


    
depozit=int(input("Depozit miqdorini kiriting:"))
foiz=float(input("Foizni kiriting:"))
yil=int(input("Nechchi yilga:"))

print(bank(depozit,foiz,yil))
