from menu import menu
import fungsi as g
from F02_register import register
from F03_login import login
from F07_listingGame import listing
from F10_cariGame import cariGameF10
from F11_cariGame import cariGameF11
from F12_topup import topup
from F14_help import help_menu
from F15_load import load
# from F16_save import save

folder = "Sem2/tubes/Data/"

data_user, data_game, data_kepemilikan, data_riwayat = load(folder)

has_logged_in = False
user_id_logged_in = 1
username_logged_in = ''
print(data_user)

while True:
   menu()
   print("Silakan masukkan command fungsi yang diinginkan: ")
   command = input(">>> ")

   # F01
   if command == 'register':
      register(data_user)

   # F02
   elif command == 'login':
      login(data_user)
      username = g.getUsername(data_user, user_id_logged_in)
   

   # elif command == 'tambah_game':
   # elif command == 'ubah_game':
   # elif command == 'ubah_stok':

   # F07
   elif command == 'list_game_toko':
      listing(data_game)


   # elif command == 'buy_game':
   # elif command == 'list_game':
   #    melihatgame(data_kepemilikan, user, game, username)

   # F10
   elif command == 'search_my_game':
      cariGameF10(user_id_logged_in)

   # F11
   elif command == 'search_game_at_store':
      cariGameF11(data_game)

   # F12
   elif command == 'topup':
      topup(user_id_logged_in, data_game)

   # elif command == 'riwayat':
   # elif command == 'save':
   #    save(data_user, data_kepemilikan, data_riwayat, data_game)
   elif command == 'help':
      help_menu()
   elif command == 'exit':
      break