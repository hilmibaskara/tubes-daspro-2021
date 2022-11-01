from fungsiDanish import *

def UbahStok(gamecsv, ):

    print(">>> Menu ubah stok")
    id_game = input("Masukkan ID Game: ")

    found = False
    index_found = 0
    for i in range(length(gamecsv)):
        if gamecsv[i][0] == id_game:
            index_found = i
            found = True
    
    if found == True:
        stok = int(input("Masukkan jumlah: "))

        if (gamecsv[index_found][5] + stok) >= 0:
            gamecsv[index_found][5] = (gamecsv[index_found][5] + stok)
            print(f"Stok game {gamecsv[index_found][1]} berhasil dirubah. Stok sekarang: {gamecsv[index_found][5]}")
        else:
            print(f"Stok game {gamecsv[index_found][1]} gagal dirubah karena stok kurang. Stok sekarang: {gamecsv[index_found][5]}")
    else:
        print("Tidak ada game dengan ID tersebut")