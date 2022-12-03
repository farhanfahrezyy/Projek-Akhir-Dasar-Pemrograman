import re
judul = """\033[1m\33[94m 
███▄ ▄███▓ ▄▄▄       ██▀███   ██▓ ███▄    █ ▓█████      ██████ ▄▄▄█████▓ ▒█████   ▄████▄   ██ ▄█▀
▓██▒▀█▀ ██▒▒████▄    ▓██ ▒ ██▒▓██▒ ██ ▀█   █ ▓█   ▀    ▒██    ▒ ▓  ██▒ ▓▒▒██▒  ██▒▒██▀ ▀█   ██▄█▒ 
▓██    ▓██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██▒▓██  ▀█ ██▒▒███      ░ ▓██▄   ▒ ▓██░ ▒░▒██░  ██▒▒▓█    ▄ ▓███▄░ 
▒██    ▒██ ░██▄▄▄▄██ ▒██▀▀█▄  ░██░▓██▒  ▐▌██▒▒▓█  ▄      ▒   ██▒░ ▓██▓ ░ ▒██   ██░▒▓▓▄ ▄██▒▓██ █▄ 
▒██▒   ░██▒ ▓█   ▓██▒░██▓ ▒██▒░██░▒██░   ▓██░░▒████▒   ▒██████▒▒  ▒██▒ ░ ░ ████▓▒░▒ ▓███▀ ░▒██▒ █▄
░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒▓ ░▒▓░░▓  ░ ▒░   ▒ ▒ ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒░▒░▒░ ░ ░▒ ▒  ░▒ ▒▒ ▓▒
░  ░      ░  ▒   ▒▒ ░  ░▒ ░ ▒░ ▒ ░░ ░░   ░ ▒░ ░ ░  ░   ░ ░▒  ░ ░    ░      ░ ▒ ▒░   ░  ▒   ░ ░▒ ▒░
░      ░     ░   ▒     ░░   ░  ▒ ░   ░   ░ ░    ░      ░  ░  ░    ░      ░ ░ ░ ▒  ░        ░ ░░ ░ 
       ░         ░  ░   ░      ░           ░    ░  ░         ░               ░ ░  ░ ░      ░  ░   
                                                                                  ░               
\033[0m"""
print("\033[1m\033[32m---------------------------------------------------------------------------------------------------\033[0m")
print(judul)
print("\033[1m\033[32m---------------------------------------------------------------------------------------------------\033[0m\n")
print("\033[1m\33[91mPILIHAN MENU\n\033[0m")
print("\033[36m1. Melihat data\n\033[0m\033[93m2. Menambah data\n\033[0m\033[32m3. Menghapus data\n\033[0m\033[36m4. Keluar program\n\033[0m")
pm = input("Masukan pilihan menu:")
namafile = "datasam.txt"

while pm != '4':
    if pm=="1":
        print("------------------------------")
        print("\033[1m\33[91mDATA KOLAM\n\033[0m")
        z =open(namafile)
        text=z.readlines()                                                                         
        text.sort()                                                                            
        print("-"*30)                                                                             
        print("Isi File:")
        noBaris = 1

        for baris in text:

            modal = re.findall("modal=(.*?);", baris)[0]
            harga = re.findall("harga=(.*?);", baris)[0]
            jumlah = re.findall("jumlah=(.*?);", baris)[0]
            terjual = re.findall("terjual=(.*?);", baris)[0]
            mati = re.findall("mati=(.*?);", baris)[0]
            persen_untung = re.findall("persen_untung=(.*?);", baris)[0]
            keuntungan = re.findall("keuntungan=(.*?);", baris)[0]
            rugi = re.findall("rugi=(.*?);", baris)[0]

            print("=" * 7 + str(noBaris) + "=" * 7)

            show = f"""|-Modal: {modal}
|-Harga: {harga}
|-Jumlah: {jumlah}
|-Terjual: {terjual}
|-Mati: {mati}
|-Persen untung: {persen_untung}
|-Untung: {keuntungan}
|-Rugi: {rugi}"""

            print(show)
            # print(f"{m
            print("=" * 7 + str(noBaris) + "=" * 7)
            noBaris+=1
        z.close()
    elif pm=="2":
        print("----------------------------------------------------------------")
        print("Menambah data ke file kolam")
        z  =open(namafile,"a")

        modal = int(input("Modal: " ))
        hargaikan = int(input("Harga per ikan: " ))
        jumlahikan = modal//hargaikan
        print("Jumlah ikan : ", jumlahikan)
        ikanterjual = int(input("Jumlah ikan terjual: "))
        ikanmati = int(input("Jumlah ikan mati: "))
        if ikanterjual > ikanmati :
            print("UNTUNG")
        elif ikanterjual < ikanmati :
            print("RUGI")
        persenuntung = int(input("Masukan persentase keuntungan :"))

        if ikanterjual > ikanmati:
            keuntungan = ikanterjual*hargaikan*((persenuntung+100)/100)-(hargaikan*ikanterjual)
            rugi = ikanmati*hargaikan
            print("keuntungannya adalah",keuntungan)
        elif ikanterjual < ikanmati:
            rugi = ikanmati*hargaikan
            keuntungan = ikanterjual*hargaikan*((persenuntung+100)/100)-(hargaikan*ikanterjual)
            print("kerugiannya adalah",rugi)
        elif ikanterjual == ikanmati:
            print("imapas")
        a=str(modal)
        b=str(hargaikan)
        c=str(jumlahikan)
        d=str(ikanterjual)
        e=str(ikanmati)
        f=str(persenuntung)
        g=str(keuntungan)
        h=str(rugi)

        z.writelines("modal="+a+";"+"harga="+b+";"+"jumlah="+c+";"+"terjual="+d+";"+"mati="+e+";"+"persen_untung="+f+";"+"keuntungan="+g+";"+"rugi="+h+";"+"\n")
        z.close()
        print("Data telah disimpan.")
    elif pm=="3":
        print("----------------------------------------------------------------")
        print("Menghapus data kolam dengan pilihan nomer")
        # target =  input("Masukan nama mahasiswa yang datanya ingin dihapus:")
        f = open("datasam.txt", "r")
        baris = input("baris yg dihapus: ")

        listnya = []
        i = 0
        for x in f.readlines():
            if (int(baris) - 1) != i:
                listnya.append(x)
            i+=1

        string = ""
        for x in listnya:
            string += x

        f = open('datasam.txt', "w")
        f.write(string)
        f.close()
    else:
        print("Pilihan menu anda tidak valid!")

    pm = input("\nMasukan pilihan menu berikutnya:")
print("Anda keluar dari program, program selesai")