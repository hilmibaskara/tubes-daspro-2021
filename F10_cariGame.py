from fungsiDanish import *
##########################################################
# F10

def cariGameF10(user_id):

    # Ngelist game yg dimiliki dari kepemilikan.csv
    
    dataIndex = []
    kepemilikancsv = bacafile("kepemilikan.csv")
    for row in range(length(kepemilikancsv)):
        if kepemilikancsv[row][1] == user_id:
            dataIndex = myappend(dataIndex, row)
    
    list_punya = []
    for i in dataIndex:
        list_punya = myappend(list_punya, gamecsv[i]) #list game yang dimiliki
    
    ####
    listIdGame = elemen_list(list_punya, 0) 
    cariID = input("Masukkan ID Game: ")
    cariTahun = input("Masukkan Tahun Rilis Game: ")
    listIdPunya = []

    # check ID
    if cariID != "":
        dataIndex2 = []
        for i in range(length(listIdGame)):
            if listIdGame[i] == cariID:
                dataIndex2 = myappend(dataIndex2, i)
        for i in dataIndex2:
            listIdPunya = myappend(listIdPunya, list_punya[i])
    else:
        listIdPunya = list_punya
        dataIndex2 = dataIndex
    
    
    if cariTahun != "":
        dataIndex3 = []
        for i in range(length(listIdPunya)):
            if listIdPunya[i][3] == int(cariTahun):
                dataIndex3 = myappend(dataIndex3, i)
    else:
        dataIndex3 = dataIndex2

    OSoutput(dataIndex3)   
