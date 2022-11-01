from fungsiDanish import *
from F15_load import load

def UbahGame(gamecsv):
    
    print(">>> Menu ubah game")
    id_game = input("Masukkan ID Game: ")

    found = False
    index_found = 0

    for i in range(length(gamecsv)):
        if gamecsv[i][0] == id_game:
            index_found = i
            found = True

    if found == True:
        namaGame = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahunRilis = input("Masukkan tahun rilis(int): ")
        harga = input("Masukkan harga(int): ")

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

        if next == "Y" or next =="y":
            gamecsv = UbahGame(gamecsv)

        
    return gamecsv