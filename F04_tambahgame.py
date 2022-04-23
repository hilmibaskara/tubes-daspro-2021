from fungsi import length

def TambahGame():
    global gamecsv, index_id_game, index_nama_game, index_kategori_game, index_tahun_game, index_harga_game, index_stock_game

    # Input dan validasi data
    while True:
        namaGame = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahunRilis = int(input("Masukkan tahun rilis(int): "))
        harga = int(input("Masukkan harga(int): "))
        stokAwal = input("Masukkan stok awal: ")

        if namaGame == "" or kategori == "" or tahunRilis == "" or harga == "" or stokAwal == "":
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO')
        
        else:
            break

    # {Masukkan data game ke list data game}
    gamecsv = myappend(gamecsv, [(f"GAME{(length(gamecsv)+1)}"), namaGame, kategori, tahunRilis, harga, stokAwal])

    print(f'Selamat! berhasil menambahkan game {namaGame}')