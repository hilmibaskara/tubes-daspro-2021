# F11
from fungsiDanish import *

def cariGameF11(gamecsv):
    
    # Ngelist game yg dimiliki dari kepemilikan.csv
    
    cariID = input("Masukkan ID Game: ")
    cariNama = input("Masukkan Nama Game: ")
    cariKategori = input("Masukkan Kategori Game: ")
    cariHarga = input("Masukkan Harga Game: ")
    cariTahun = input("Masukkan Tahun Rilis Game: ")
    try:
        cariHarga = int(cariHarga)
    except:
        cariHarga = cariHarga

    try:
        cariTahun = int(cariTahun)
    except:
        cariTahun = cariTahun

    listGameOutput = []
    listGameOutput = cariDlmList(gamecsv, cariID, 0)
    listGameOutput = cariDlmList(listGameOutput, cariNama, 1)
    listGameOutput = cariDlmList(listGameOutput, cariKategori, 2)
    listGameOutput = cariDlmList(listGameOutput, cariHarga, 4)
    listGameOutput = cariDlmList(listGameOutput, cariTahun, 3)

    dataIndex = []
    for i in range(length(listGameOutput)):
        dataIndex = myappend(dataIndex, (int(listGameOutput[i][0][4:]))-1)
    

    OSoutput(dataIndex, gamecsv)   
    return gamecsv
