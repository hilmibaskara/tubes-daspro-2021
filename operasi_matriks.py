import fungsi as g

def convert_line_to_data(line):
  array_of_data = g.split(line, ";")
  return array_of_data

def convert_array_data_to_real_values(array_data, filecsv):
  arr_cpy = array_data[:]   # membuat copy dari array_of_data
  if filecsv == 'user':
    for i in range(6):        # iterate kolom
      if(i == 0):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i == 5):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy
  elif filecsv == 'kepemilikan':
    for i in range(2):
      if (i == 1):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy   
  elif filecsv == 'riwayat':
    for i in range(5):        # iterate kolom
      if(i == 3):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i == 4):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i == 2):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy
  elif filecsv == 'game':
    for i in range(6):        # iterate kolom
      if(i == 3):
        arr_cpy[i] = int(arr_cpy[i])
      elif (i == 4):
        arr_cpy[i] = int(arr_cpy[i])
      elif(i == 5):
        arr_cpy[i] = int(arr_cpy[i])
    return arr_cpy

def read_csv(path, filecsv):
   # ngebuka file 
    f = open(path, "r")
   # assign variabel yang membaca barisan dan di-assign ke dalam array
    raw_lines = f.readlines()
    f.close()
   # biar habis linenya beres ga langsung spasi, diilangin \n nya
    lines = [g.replace_spasi(raw_line) for raw_line in raw_lines]
    lines = lines[1:]
    datas = []
   # nge-iterate untuk ngeprint barisan satu persatu
    for line in lines:
      array_of_data = convert_line_to_data(line)
      real_values = convert_array_data_to_real_values(array_of_data, filecsv)
      g.append(datas,real_values)
    return datas

def write_csv(data, path):
  f = open(path, 'w')
  row = hitung_baris(data)
  for i in range(row-1):
    kalimat = ''
    for j in range(hitung_kolom(data)-1):
      kalimat += data[i][j] + ";"
      print(kalimat)
    kalimat += data[hitung_baris(data-1)][hitung_kolom] + "\n"
    f.write(kalimat)
  f.close()


def join(arr,joinstr):
  kalimat = ''
  for word in range(g.length(arr)-1):
    kalimat += arr[word] + joinstr
  kalimat += arr[g.length(arr)-1]
  return kalimat


def hitung_baris(data):
  return g.length(data)

def hitung_kolom(data):
  return g.length(data[0])