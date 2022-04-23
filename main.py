# from menu import menu
# import fungsi as g
# from F02_register import register
# from F03_login import login
# from F14_help import help_menu
from F15_load import load
# from F16_save import save

folder = "Sem2/tubes/Data/"

data_user, data_game, data_kepemilikan, data_riwayat = load(folder)

has_logged_in = False
user_id_logged_in = 0
username_logged_in = ''
print(data_user)

# while True:
#    menu()
#    print("Silakan masukkan command fungsi yang diinginkan: ")
#    command = input(">>> ")
#    if command == 'register':
#       register(data_user)
#    elif command == 'login':
#       login(data_user)
#       username = g.getUsername(data_user, user_id_logged_in)
   # elif command == 'tambah_game':
   # elif command == 'ubah_game':
   # elif command == 'ubah_stok':
   # elif command == 'list_game_toko':
   # elif command == 'buy_game':
   # elif command == 'list_game':
   #    melihatgame(data_kepemilikan, user, game, username)
   # elif command == 'search_my_game':
   # elif command == 'search_game_at_store':
   # elif command == 'topup':
   # elif command == 'riwayat':
   # elif command == 'save':
   #    save(data_user, data_kepemilikan, data_riwayat, data_game)
   # elif command == 'help':
   #    help_menu()
   # elif command == 'exit':
   #    break