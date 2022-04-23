from fungsiDanish import length, padding, elemen_list

##########################################################
# F07 - Listing game berdasarkan ID, tahun, dan harga

def listing(gamecsv):
    jenis = input("Skema Sorting")
    if jenis == "tahun+" or jenis == "harga+":
        selection_sort_plus(jenis, gamecsv)

    elif jenis == "tahun-" or jenis == "harga-":
        selection_sort_min(jenis, gamecsv)
    
    else:
        print("Masukkan tidak sesuai")
        print('Silahkan ketik "tahun+", "tahun-", "harga+", atau "harga-"')


# {Sorting Algorithms}
# sort ascending
def selection_sort_plus(jenis, gamecsv):
    nama_list = []

    if jenis == "tahun+":
        nama_list = elemen_list(gamecsv, 3)
    elif jenis == "harga+":
        nama_list = elemen_list(gamecsv, 4)


    # array index data game
    dataIndex = [i for i in range(length(nama_list))]
    
    for i in range(len(nama_list)):
        indexMax = i

        for j in range(i+1, len(nama_list)):
            if nama_list[j] < nama_list[indexMax]:
                indexMax = j
        
        nama_list[i], nama_list[indexMax] = nama_list[indexMax], nama_list[i]
        dataIndex[i], dataIndex[indexMax] = dataIndex[indexMax], dataIndex[i]

    OSoutput(dataIndex)

# sort descending
def selection_sort_min(jenis, gamecsv):
    nama_list = []

    if jenis == "tahun-":
        nama_list = elemen_list(gamecsv, 3)
    elif jenis == "harga-":
        nama_list = elemen_list(gamecsv, 4)


    # array index data game
    dataIndex = [i for i in range(length(nama_list))]
    
    for i in range(len(nama_list)):
        indexMin = i

        for j in range(i+1, len(nama_list)):
            if nama_list[j] > nama_list[indexMin]:
                indexMin = j
        
        nama_list[i], nama_list[indexMin] = nama_list[indexMin], nama_list[i]
        dataIndex[i], dataIndex[indexMin] = dataIndex[indexMin], dataIndex[i]

    OSoutput(dataIndex)


# fungsi untuk menuliskan hasil sort ke OS
def OSoutput(dataIndex):
    global gamecsv

    no = 0
    for i in dataIndex:
        no +=1
        teks = f'NO | ID | {padding("Nama Game", 20)}| {padding("Kategori Game", 20)} | {padding("Tahun", 5)} | {"Harga"} | {"Stock"}'
        teks = f'{no} | {gamecsv[i][0]} | {padding(gamecsv[i][1], 20)}| {padding(gamecsv[i][2], 20)} | {padding(gamecsv[i][3], 5)} | {gamecsv[i][4]} | {gamecsv[i][5]}'

        print(teks)


