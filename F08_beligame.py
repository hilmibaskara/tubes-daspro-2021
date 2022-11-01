from fungsiDanish import *

def beligame(user_id, gamecsv, usercsv,  kepemilikancsv, riwayatcsv):
    
    dataIndex = []
    for row in range(length(kepemilikancsv)):
        if kepemilikancsv[row][1] == user_id:
            dataIndex = myappend(dataIndex, row)
    
    list_punya = []
    for i in dataIndex:
        list_punya = myappend(list_punya, gamecsv[i]) #list game yang dimiliki
  
    idbeli = input("Masukkan ID Game: ")

    found = False
    for i in range(length(gamecsv)):
        if gamecsv[i][0] == idbeli:
            index = i
            found = True

    if found == True:
        berhasil = True
        #chek kepemilikan
        for i in range(length(list_punya)):
            if list_punya[i][0] == idbeli:
                print("Anda sudah memiliki Game tersebut")
                berhasil = False

        # chek saldo
        if usercsv[user_id-1][5] < gamecsv[index][4]:
            print("Maaf, Saldo tidak mencukupi")
            berhasil = False

        # chek stock
        if int(gamecsv[index][5]) <=0:
            print("Stock sedang habis")
            berhasil = False

        if berhasil == True:
            print(f"Game {gamecsv[index][1]} berhasil dibeli")

            riwayatcsv = myappend(riwayatcsv, [gamecsv[index][0], gamecsv[index][1], gamecsv[index][4], user_id, 2022])
            kepemilikancsv = myappend(kepemilikancsv, [gamecsv[index][0], user_id])

    elif found == False:
        print("Game tersebut tidak ada di toko kami")
        print("Apakah anda ingin mencari game lain?")
        yn = input("(y/n)")
        while True:
            if yn == "y" or yn == "Y":
                beligame(user_id, gamecsv, usercsv,  kepemilikancsv, riwayatcsv)
            elif yn == 'n' or yn == 'N':
                break
            else:
               print("Silakan putuskan y/n!")
    
    return kepemilikancsv, riwayatcsv