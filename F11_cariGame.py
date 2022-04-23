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
        cariTahun = int(cariTahun)
    except:
        pass

    listGameOutput = []
    listGameOutput = cariDlmList(gamecsv, cariID, 0)
    listGameOutput = cariDlmList(listGameOutput, cariNama, 1)
    listGameOutput = cariDlmList(listGameOutput, cariKategori, 2)
    listGameOutput = cariDlmList(listGameOutput, cariHarga, 3)
    listGameOutput = cariDlmList(listGameOutput, cariTahun, 4)

    dataIndex = []
    for i in range(length(listGameOutput)):
        dataIndex = myappend(dataIndex, (int(listGameOutput[i][0][4:-1]))-1)
    
    OSoutput(dataIndex)   
