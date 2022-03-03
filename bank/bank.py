def awal():
    print ("")
    print ("1) Tarik Tunai")
    print ("2) Transfer")

    menu = int(input("Pilih :"))
    return menu

menu = awal()

def tt(menu):
    if menu == 1 :
        print ("")
        print ("Max Rp 2500000")
        print ("Minimal Rp 50000")
        print ("")
        tarik = int(input("Jumlah yang akan di tarik \n Rp "))
        if tarik > 2500000 :
            print ("=========")
            print (":(")
            tt(menu)
        if tarik > 49999 :
            print ("Transaksi sedang di proses")
            awal()
        if tarik < 50000 :
            print ("==========")
            print (":(")
            tt(menu)


tt(menu)

def tf(menu):
    if menu == 2 :
        print ("======================")
        print ("")
        print ("masukan nomor rekening")
        rek = int(input(""))
        if rek > 12  :
            # jika digit lebih dari 12 
            print ("")
            print ("rek yang anda inputkan salah \n cek lagi")
            print("")
            tf (menu)
        
        if rek:
            print ("")
            print ("Atas Nama :")
            print ("Nomor Rek \n ",rek)
            print ("")
            print ("1/0")
            print ("tekan 1 jika benar \n tekan 0 jika salah")
            y= int(input())

        if y == 1 :
            print ("Transaksi Diproses")
            print ("")
            awal()
        if y == 0 : 
            print ("Transaksi Di batalkan")
            print ("")
            awal()
tf (menu)



# melsen888 :D