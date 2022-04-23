def UbahGame():
    global gamecsv, index_id_game, index_nama_game, index_kategori_game, index_tahun_game, index_harga_game, index_stock_game
    
    print(">>> Menu ubah game")
    id_game = input("Masukkan ID Game: ")

    found = False
    index_found = 0
    while found == False:
        if gamecsv[index_found][index_id_game] == id_game:
            found = True
        else:
            index_found += 1
    
    print(gamecsv[0][0])

    if found == True:
        namaGame = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahunRilis = int(input("Masukkan tahun rilis(int): "))
        harga = int(input("Masukkan harga(int): "))

        if namaGame != "":
            gamecsv[index_found][1] = namaGame
        if kategori != "":
            gamecsv[index_found][2] = kategori
        if tahunRilis != "":
            gamecsv[index_found][3] = tahunRilis
        if harga != "":
            gamecsv[index_found][4] = harga

        print(f"Data game dengan ID {gamecsv[index_found][0]} berhasil diubah")
    
    else:
        print("ID game tidak ditemukan")
        print("Apakah mau memasukkan ID ulang? Y/N")
        next = input()

        if next == ("Y" or "y"):
            UbahGame()
        else:
            exit()