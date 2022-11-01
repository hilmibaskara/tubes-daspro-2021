# Import modul yang dibutuhkan
import operasi_matriks as m
import fungsi as g


def register(data_user):
   # KAMUS LOKAL
   # nama, username, password : string
   # id                       : integer
   # arr_temp              : list
   # data_user                : array of list

   # Algoritma
   while True:
      nama = str(input("Masukkan nama: "))                  # input nama dan username
      username = str(input("Masukkan username: ")) 
      if nama == '' or username == '':                      # nama dan username yang diinput tidak boleh kosong
         print("Nama dan username tidak boleh kosong. Silakan masukkan ulang!")
      else:
         break

   if validasiUsername(username):                           # jika username berhasil divalidasi maka program akan meminta input password
      if cekUsername(data_user, username):
         password = str(input("Masukkan password: "))
         while True:
            if password == '':                              # jika password yang diinput kosong. Maka program akan meminta input lagi sampai benar
               print("Password tidak boleh kosong. Silakan masukkan ulang!")
            else:                                           # karakter password sudah benar. Akan melakukan append dari data yang dimiliki pada akun ke array
               id = hitungID(data_user) + 1                 # user_id yang didapat pada akun baru dihitung dari id terbesar sebelumnya + 1
               arr_temp = []
               g.append(arr_temp, id)
               g.append(arr_temp, username)
               g.append(arr_temp, nama)
               g.append(arr_temp, password)
               g.append(arr_temp, 'user')                # akun yang terdaftar secara otomatis memiliki role user
               g.append(arr_temp, 0)
               g.append(data_user, arr_temp)             # append array akun baru ke data_user keseluruhan
               print("Username" + username + "telah berhasil register ke dalam Binomo")
               break            
      else:
         print("Username " + username + " sudah terpakai, silakan menggunakan username lain")
   else:
      print("Username tidak valid")

def validasiUsername(username):       # Validasi username hanya boleh menggunakan karakter tertentu. Mereturn True jika validasi berhasil. False jika tidak berhasil.
   # karakter yang diperbolehkan
    ValidChar = ['0', "1", "2", "3", "4", "5", "6", "7", "8", "9", \
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', \
                 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'\
                 "_", "-"]
    valid = True
    # pengecekan dengan melakukan iterasi pada setiap karakter username dengan ValidChar
    for i in username:
        if i not in ValidChar:
            valid = False
            break
    return valid

# Melakukan cek apakah username sudah terpakai atau belum pada akun yang sudah terdaftar
def cekUsername(data, username):
   valid = True
   # pengecekan dilakukan dengan iterasi username pada setiap indeks[i][1] pada matriks yang berisi username
   for i in range (hitungID(data)):
      if data[i][1] == username:
         valid = False
         break
   return valid

# melakukan hitung id dengan memanfaatkan banyaknya row pada matriks. Mereturn banyak id yang sudah terdaftar.
def hitungID(data):
   return m.hitung_baris(data)