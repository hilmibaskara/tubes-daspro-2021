# Import library bawaan python
import os
import argparse

# Import modul yang berisi fungsi penunjang program
import fungsi as g            # berisi fungsi penunjang
import zconstant as c         # berisi output keluaran pada kondisi tertentu yang berulang supaya tidak memenuhi main.py
from menu import menu         # berisi output menu utama
from fungsiDanish import *    # berisi fungsi penunjang lainnya

# Import Modul Fungsi sesuai spesifikasi
from F02_register import register
from F03_login import login
from F04_tambahgame import TambahGame
from F05_ubahgame import UbahGame
from F06_ubahstok import UbahStok
from F07_listingGame import listing
from F08_beligame import beligame
from F09_melihatgame import melihatgame
from F10_cariGame import cariGameF10
from F11_cariGame import cariGameF11
from F12_topup import topup
from F13_riwayat import riwayat
from F14_help import help_menu
from F15_load import load
from F16_save import save
from F17_exit import fungsi_exit

# folder = "tubes/Data/"
# Inisialisasi variabel
has_logged_in = False      # kondisi yang menandakan pengguna sudah/belum login
user_id_logged_in = 0      # user_id akun yang berhasil login
username_logged_in = ''    # username akun yang berhasil login
role = ''                  # role akun yang berhasil login

# list command yang tidak dapat diakses sebelum login
command_before_login = ['register', 'tambah_game', 'ubah_game', 'ubah_stok', 'list_game_toko', 'buy_game', 'list_game', 'search_my_game', 
                        'search_game_at_store', 'topup', 'riwayat', 'save', '1', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12','14']

# program utama
if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument('inputfolder', type=str, help="Masukkan nama folder! ")
   args = parser.parse_args()

   #Kondisi Folder file ditemukan atau tidak
   if not (os.path.exists(args.inputfolder)) :
      print("Tidak ada nama folder yang diberikan. Silakan masukkan ulang!")
   else :  #Main Program
      os.chdir(args.inputfolder)

      data_user, data_game, data_kepemilikan, data_riwayat = load()  # melakukan loading data dari csv menjadi matriks

      # pengulangan pada menu utama
      while True:
         os.system('cls')                                                  # melakukan clear output ketika sudah berhasil menjalankan satu fungsi
         menu()                                                            # print main menu
         print("Silakan masukkan command fungsi yang diinginkan: ")        # memasukkan command input
         command = input(">>> ")

         # menu yang dapat diakses ketika belum login
         if has_logged_in == False:
            # F02 - Login
            if command == 'login' or command == '2':
               has_logged_in, user_id_logged_in = login(data_user, has_logged_in)   # mereturn kondisi has_logged_in dan user_id yang berhasil login
               if has_logged_in:
                  username_logged_in = g.getUsername(data_user, user_id_logged_in)  # mereturn username dan role ketika berhasil login
                  role = g.getRole(data_user, user_id_logged_in)
                  c.enter_done()
            # F03 - Help
            elif command == 'help' or command == '13':
               help_menu(role, has_logged_in)
               c.enter_done()
            # F17 - exit
            elif command == 'exit' or command == '15':
               exit()
            else:
               ada = False
               # Algoritma untuk melakukan keterangan output "harus login dulu" ketika command yang diinput merupakan salah satu dari command yang ada
               for i in range(g.length(command_before_login)):
                  if command == command_before_login[i]:
                     c.login_first()
                     ada = True
                     c.enter_done()
                     break
               # jika tidak ada akan mengeluarkan "command tidak tersedia"
               if ada == False:
                  print("Command tidak tersedia")
                  c.enter_done()

         # menu yang dapat diakses ketika sudah login
         else:                                                 # has_logged_in = True, sudah login
            # F02 - Register. Akses: admin.
            if command == 'register' or command == '1':
               if role == 'user':
                  c.admin_only()
                  c.enter_done()
               else:
                  register(data_user)
                  print(data_user)
                  c.enter_done()

            # F03 - Login
            elif command == 'login' or command == '2':
               print("Anda sudah login!")
               c.enter_done()
            
            # F04 - Tambah Game. Akses: admin.
            elif command == 'tambah_game' or command == '3':
               if role == 'user':
                  c.admin_only()
                  c.enter_done()
               else:
                  data_game = TambahGame(data_game)
                  print(data_game)
                  c.enter_done()

            # F05 - Ubah Game. Akses: admin.
            elif command == 'ubah_game' or command == '4':
               if role == 'user':
                  c.admin_only()
                  c.enter_done()
               else:
                  data_game = UbahGame(data_game)
                  print(data_game)
                  c.enter_done()

            # F06 - Ubah Stok. Akses: admin.
            elif command == 'ubah_stok' or command == '5':
               if role == 'user':
                  c.admin_only
                  c.enter_done()
               else:
                  UbahStok(data_game)
                  print(data_game)
                  c.enter_done()

            # F07 - Melihat list game yang ada di toko. Akses: admin & user.
            elif command == 'list_game_toko'  or command == '6':
               listing(data_game)
               c.enter_done()

            # F08 - Membeli game. Akses: user.
            elif command == 'buy_game' or command == '7':
               if role == 'admin':
                  c.user_only()
                  c.enter_done()
               else:
                  data_kepemilikan, data_riwayat = beligame(user_id_logged_in, data_game, data_user, data_kepemilikan, data_riwayat)
                  print(data_riwayat)
                  c.enter_done()

            #F09 - Melihat list game yang dimiliki oleh user. Akses: user.
            elif command == 'list_game' or command == '8':
               if role == 'admin':
                  c.user_only()
                  c.enter_done()
               else:
                  melihatgame(user_id_logged_in, data_kepemilikan, data_game)
                  c.enter_done()

            # F10 - Mencari game yang dimiliki user. Akses: user.
            elif command == 'search_my_game' or command == '9':
               if role == 'admin':
                  c.user_only()
                  c.enter_done()
               else:
                  cariGameF10(user_id_logged_in, data_game, data_kepemilikan)
                  c.enter_done()

            # F11 - Mencari game yang ada di toko. Akses = user, admin
            elif command == 'search_game_at_store' or command == '10':
               cariGameF11(data_game)
               c.enter_done()

            # F12. Akses: admin.
            elif command == 'topup' or command == '11':
               if role == 'user':
                  c.admin_only()
                  c.enter_done()
               else:
                  username = input("Masukkan Username: ")
                  for i in range(length(data_user)):
                     if data_user[i][1] == username:
                        user_id = i
                  data_user[user_id][5] = topup(user_id, data_user)
                  c.enter_done()

            # F13 - Melihat riwayat pembelian user. Akses: admin.
            elif command == 'riwayat' or command == '12':
               if role == 'admin':
                  c.user_only()
                  c.enter_done()
               else:
                  riwayat(user_id_logged_in, data_riwayat)
                  c.enter_done()
            
            # F16 - save. Akses: admin & user.
            elif command == 'save' or command == '14':
               save(data_user, data_kepemilikan, data_riwayat, data_game)
               c.enter_done()

            # F15 - Load
            elif command == 'help' or command == '13':
               help_menu(role, has_logged_in)
               c.enter_done()

            # F16 - Save
            elif command == 'exit' or command == '15':
               fungsi_exit(data_user, data_kepemilikan, data_riwayat, data_game)

            # Output ketika command tidak tersedia
            else:
               print("Maaf, command tidak tersedia di program BNMO!")