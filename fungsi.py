def length(array):
   count = 0
   for i in array:
      count += 1
   return count

def append(array,s):
    array += [s]

def panjang_baris(array):
  n = 0
  for i in array:
    n += 1
  return n

def split(string, delimit):
    kata = []
    kata_sekarang = ""
    for char in string:
        if char == delimit:
            append(kata, kata_sekarang)
            kata_sekarang = ""
        else:
            kata_sekarang += char
    append(kata, kata_sekarang)        
    return kata

def replace_spasi(n):
  data = []
  for i in range(length(n)-1):
    append(data, n[i])
  return data

def join(arr,joinstr):
  kalimat = ''
  for word in range(length(arr)-1):
    kalimat += arr[word] + joinstr
  kalimat += arr[length(arr)-1]
  return kalimat

def getUsername(data, user_id):
  return data[user_id-1][1]

def getRole(data, user_id):
  return data[user_id-1][4]