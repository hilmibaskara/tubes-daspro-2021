


# {Fungsi-fungsi pembantu}
# bikin fungsi len sendiri // menghitung jumlah karakter dlm suatu variabel
def length(listName):
    n = 0
    for i in listName:
        n += 1
    return n

# bikin fungsi append sendiri // menambahkan sesuatu ke list
def myappend(list, word):
  temp = [0 for i in range(length(list)+1)]
  for i in range(length(list)):
    temp[i] = list[i]
  temp[-1] = word
  list = temp
  return list

# bikin fungsi split sendiri // memisahkan string berdasarkan sebuah char kedalam sebuah list
def mysplit(word, char):
  # list = [0 for i in length(word)]
  li = []
  kata = ""
  n = length(word)
  a=0

  for i in word:
    a+=1
    if i != char:
      kata += i
    else:
      li = myappend(li, kata)
      kata = ""
    
    if a == n:
      li = myappend(li, kata)

  return li

# bikin fungsi replace sendiri // mengubah suat char pada suatu string dengan char lain
def myreplace(word, ori, change):
  hasil = ""
  for i in word:
    if i == ori:
      hasil += change
    else:
      hasil += i
  
  return hasil

# Fungsi untuk membaca suatu row pada file csv dan return sebagai list
def bacafile(namafile):
    global data
    data = []
    
    f = open(namafile,"r")
    raw_lines = f.readlines()
    f.close()
    lines = [myreplace(raw_line, "\n", "") for raw_line in raw_lines]


    def jadikan_int(array_data):
        temp = [i for i in mysplit(array_data, ";")]

        for i in range(length(lines[0])):
            try:
                temp[i] = int(temp[i])
            except:
                pass
        return temp

    for line in lines[1:]:
        nilaireal = (jadikan_int(line))
        data = myappend(data, nilaireal)
    return data

# Fungsi untuk membuat suatu list tunggal dari list csv
def elemen_list(listnya, elemenya):
    data = []
    n = length(listnya)
    for i in range(n):
        data = myappend(data, listnya[i][elemenya])
    return data

# fungsi untuk membatasi jumlah huruf yg keluar pada OS
def padding(word, no):
    teks = str(word) + " "*20
    teks_output = ""
    for i in range(no):
        teks_output += teks[i]
    
    return teks_output

def cariDlmList(list, ygDicari, index):
    if ygDicari != "":
        listTemp = []
        for i in range(length(list)):
            if list[i][index] == ygDicari:
                listTemp = myappend(listTemp, list[i])
    
    else:
        listTemp = list
    return listTemp

# fungsi untuk menuliskan hasil sort ke OS
def OSoutput(dataIndex, gamecsv):

    if (length(dataIndex)) != 0:
        judul = f'NO |   ID    | {padding("Nama Game", 20)}| {padding("Kategori Game", 20)} | {padding("Tahun", 5)} | {"Harga"} | {"Stock"}'
        print(judul)

        no = 0
        for i in dataIndex:
            no +=1
            teks = f'{no}  | {padding((gamecsv[i][0]),7)} | {padding(gamecsv[i][1], 20)}| {padding(gamecsv[i][2], 20)} | {padding(gamecsv[i][3], 5)} | {gamecsv[i][4]} | {gamecsv[i][5]}'
            print(teks)

    else:
      print("--------Tidak ada game yang memenuhi kriteria------")

    print("")
