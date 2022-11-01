# Import modul yang dibutuhkan
from fungsi import length

def riwayat(user_id, riwayatcsv):
    # Kamus Lokal
    # count, user_id, i : integer
    # kondisi           : boolean
    # riwayatcsv        : array of list

    # Algoritma
    count = 0                               # untuk mencetak berapa banyak riwayat pembelian dalam nomor baris
    kondisi = False                         # parameter jika ditemukan riwayat atau tidak
    for i in range(length(riwayatcsv)):     # melakukan pencocokan user_id dengan matriks riwayatcsv[i][3] yang berisi user_id pembeli
        if user_id == riwayatcsv[i][3]:
            count += 1
            print(str(count) + '. ' + riwayatcsv[i][0] + ' | ' + riwayatcsv[i][1] + ' | ' + str(riwayatcsv[i][2]) + ' | ' + str(riwayatcsv[i][4]))
            kondisi = True

    if kondisi == False:                    # ketika tidak ditemukan riwayat pembelian game akan mengeluarkan output keterangan bahwa belum membeli game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")