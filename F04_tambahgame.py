from fungsi import length
from fungsiDanish import *

def TambahGame(gamecsv):

    # Input dan validasi data
    while True:
        namaGame = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahunRilis = input("Masukkan tahun rilis(int): ")
        harga = input("Masukkan harga(int): ")
        stokAwal = input("Masukkan stok awal(int): ")

        if namaGame == "" or kategori == "" or tahunRilis == "" or harga == "" or stokAwal == "":
            print('Mohon masukkan semua informasi mengenai game agar dapat disimpan BNMO')
        
        else:
            break

    # {Masukkan data game ke list data game}
    gamecsv = myappend(gamecsv, [(f"GAME{(length(gamecsv)+1)}"), namaGame, kategori, tahunRilis, harga, stokAwal])

    print(f'Selamat! berhasil menambahkan game {namaGame}')

    return gamecsv