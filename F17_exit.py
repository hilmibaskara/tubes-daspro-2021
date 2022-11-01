from F16_save import save

def fungsi_exit(data_user, data_kepemilikan, data_riwayat, data_game) :
    print("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    masukkan=input()
    cek = True
    while cek: 
        if masukkan == "Y" or masukkan == "y" :
            save(data_user, data_kepemilikan, data_riwayat, data_game)
            cek=False
            exit()
        elif masukkan == "n" or masukkan == "N" :
            print("Permainan selesai")
            exit()
        else : 
            print("Pilihan tidak valid. Masukkan (y/n)")
