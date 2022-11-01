from fungsiDanish import length, elemen_list, OSoutput

##########################################################
# F07 - Listing game berdasarkan ID, tahun, dan harga

def listing(gamecsv):
    print('Skema sorting yg dapat dipilih: "tahun+", "tahun-", "harga+", atau "harga-"')
    jenis = input("Pilih Skema Sorting: ")
    if jenis == "tahun+" or jenis == "harga+":
        selection_sort_plus(jenis, gamecsv)

    elif jenis == "tahun-" or jenis == "harga-":
        selection_sort_min(jenis, gamecsv)
    
    else:
        print("Masukkan tidak sesuai")
        print('Silahkan ketik "tahun+", "tahun-", "harga+", atau "harga-"')

    print("Apakah ingin melihat skema sorting lain?")
    yn = input('y/n?\n')
    if yn == 'y' or yn == 'Y':
        listing(gamecsv)
    elif yn == 'n' or yn == 'N':
        pass
    else:
        print('Input tidak valid. Silakan masukkan ya/tidak(y/n)')
    

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

    OSoutput(dataIndex, gamecsv)

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

    OSoutput(dataIndex, gamecsv)


