import operasi_matriks as m
import fungsi as g

def register(data_user):
   nama = str(input("Masukkan nama: "))
   username = str(input("Masukkan username: "))

   if validasiUsername(username):
      if cekUsername(data_user, username):
         password = str(input("Masukkan password: "))
         id = hitungID(data_user) + 1
         arr_masukan = []
         g.append(arr_masukan, id)
         g.append(arr_masukan, username)
         g.append(arr_masukan, nama)
         g.append(arr_masukan, password)
         g.append(arr_masukan, 'user')
         g.append(arr_masukan, 0)
         g.append(data_user, arr_masukan)
      else:
         print("Username " + username + " sudah terpakai, silakan menggunakan username lain")
   else:
      print("Username tidak valid")

def validasiUsername(username):
    ValidChar = ['0', "1", "2", "3", "4", "5", "6", "7", "8", "9", \
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\
                 "_", "-"]
    valid = True
    for i in username:
        if i not in ValidChar:
            valid = False
            break
    return valid

def cekUsername(data, username):
   valid = True
   for i in range (hitungID(data)):
      if data[i][1] == username:
         valid = False
         break
   return valid

def hitungID(data):
   return m.hitung_baris(data)