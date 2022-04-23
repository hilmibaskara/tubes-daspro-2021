def UbahStok():
    global gamecsv, index_id_game, index_nama_game, index_kategori_game, index_tahun_game, index_harga_game, index_stock_game

    print(">>> Menu ubah stok")
    id_game = input("Masukkan ID Game: ")

    found = False
    index_found = 0
    while found == False:
        if gamecsv[index_found][index_id_game] == id_game:
            found = True
        else:
            index_found += 1
    
    if found == True:
        stok = int(input("Masukkan jumlah: "))

        if (gamecsv[index_found][5] + stok) >= 0:
            gamecsv[index_found][5] = (gamecsv[index_found][5] + stok)
            print(f"Stok game {gamecsv[index_found][1]} berhasil dirubah. Stok sekarang: {gamecsv[index_found][5]}")
        else:
            print(f"Stok game {gamecsv[index_found][1]} gagal dirubah karena stok kurang. Stok sekarang: {gamecsv[index_found][5]}")
    else:
        print("Tidak ada game dengan ID tersebut")