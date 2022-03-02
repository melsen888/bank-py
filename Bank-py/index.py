def bank():
    def header():
        print ("")
        print ("---MELSEN BANK---")
        print ("")
        print ("@welcome")
        print ("")

    header()


# isi

    print("Name :")
    name = input()
    print ("")
    saldo=int(input("tabungan anda: Rp "))





# simpan

    def simpan():
        print ("")
        if saldo == 0 :
                print ("angka yang anda inputkan tidak boleh 0")
                print("")
                print(":(")
        elif saldo > 0 :
                print("hi",name)
                print("=========================")
                print("total tabungan yang anda masukan Rp",saldo)
                print("")
    simpan()

bank()


# logika


