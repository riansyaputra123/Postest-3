print("==============================================")
print("         >> GUITAR ACCOUSTIC STORE <<         ")
print("==============================================")
print("Kode:      Nama Gitar:             Harga:     \n")
print("YMH   :    Yamaha F400          :  Rp. 1250000")
print("CRT   :    Cort AD810E          :  Rp. 1750000")
print("CDZ   :    Cadenza CE203        :  Rp. 1500000")
print("SGV   :    Segovia D-W07        :  Rp. 1850000")
print("PRD   :    Prodinne tapa40CN    :  Rp. 1450000")
print("==============================================")
print("=           --> DISKON SPESIAL! <--          =")
print("=                                            =")
print("= -Diskon 10% jika belanja lebih dari 5 juta =")
print("= -Diskon 25% jika belanja lebih dari 7 juta =")
print("==============================================")

jumlah_tipe = int(input("Banyak tipe   : "))
x = 0
harga = [1250000, 1750000, 1500000, 1850000, 1450000] 
total = []
while x < jumlah_tipe:
    print("\nTipe ke -", 1 + x)
    kode_produk = str(input("Kode produk   : "))
    jumlah_produk = int(input("Jumlah produk : "))
    x += 1
    
    y = kode_produk
    if y == "CDZ" or y == "cdz":
        total.append(jumlah_produk*harga[2])
        total1 = jumlah_produk*harga[2]
        print("Total harga   : Rp.", total1)
    elif y == "CRT" or y == "crt":
        total.append(jumlah_produk*harga[1])
        total2 = jumlah_produk*harga[1]
        print("Total harga   : Rp.", total2)
    elif y == "YMH" or y =="ymh":
        total.append(jumlah_produk*harga[0])
        total3 = jumlah_produk*harga[0]
        print("Total harga   : Rp.", total3)
    elif y == "SGV" or y == "sgv":
        total.append(jumlah_produk*harga[3])
        total4 = jumlah_produk*harga[3]
        print("Total harga   : Rp.", total4)
    elif y == "PRD" or y == "prd":
        total.append(jumlah_produk*harga[4])
        total5 = jumlah_produk*harga[4]
        print("Total harga   : Rp.", total5)

print("==============================================")
sub_total =sum(total)
print("sub total                    : Rp.", sub_total)
diskon1 = sub_total * 0.10
diskon2 = sub_total * 0.25
if sub_total <= 5000000:
    print("Diskon - %                   : Rp. -")
    print("\nTotal                        : Rp.", sub_total)
    print("==============================================")
    uang_tunai1 = int(input("Uang tunai                   : Rp. "))
    kembalian1 = uang_tunai1 - sub_total
    print("Kembalian                    : Rp.", kembalian1)
    print("\n----------------------------------------------")
elif sub_total <= 7000000:
    print("Diskon 10%, potongan sebesar : Rp.", diskon1)
    total_bayar2 = sub_total - diskon1
    print("\nTotal                        : Rp.", total_bayar2)
    print("==============================================")
    uang_tunai2 = int(input("Uang tunai                   : Rp. "))
    kembalian2 = uang_tunai2 - total_bayar2
    print("Kembalian                    : Rp.", kembalian2)
    print("\n----------------------------------------------")
elif sub_total > 7000000:
    print("Diskon 25%, potongan sebesar : Rp.", diskon2)
    total_bayar3 = sub_total - diskon2
    print("\nTotal                        : Rp.", total_bayar3)
    print("==============================================")
    uang_tunai3 = int(input("Uang tunai                   : Rp. "))
    kembalian3 = uang_tunai3 - total_bayar3
    print("Kembalian                    : Rp.", kembalian3)
    print("\n----------------------------------------------")
    