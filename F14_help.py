def help_menu():
   global data_user, user_id
   if data_user[user_id][4] == 'admin':
      print("1. register - Untuk melakukan registrasi user baru")
      print("2. login - melakukan login ke dalam sistem")
      print("3. tambah_game - Untuk menambah game yang dijual pada toko")
      print("4. ubah_game - Untuk mengubah game pada toko game")
      print("5. ubah_stok - Untuk mengubah stok sebuah game pada toko")
      print("6. list_game_toko - Untuk melihat list game yang dijual pada toko")
      print("7. search_game_at_store - Untuk melakukan pencarian pada toko")
      print("8. topup - Untuk menambahkan saldo kepada User")
      print("9. Help - Untuk memberikan panduan penggunaan sistem")
      print("10. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")
      print("11. exit - Untuk keluar")


   elif data_user[user_id][4] == 'user':
      print("1. login - Untuk melakukan login ke dalam sistem")
      print("2. list_game_toko - Untuk melihat liost game yang dijual pada toko")
      print("3. buy_game - Untuk membeli game")
      print("4. list_game - Untuk melihat game yang dimiliki")
      print("5. search_my_game - Untuk mendapatkan informasi pada inventory")
      print("6. search_game_at_store - Untuk melakukan pencarian pada toko")
      print("7. riwayat - Untuk melihat riwayat pembelian game")
      print("8. help - Untuk memberikan panduan penggunaan sistem")
      print("9. save - Untuk melakukan penyimpanan data ke dalam file setelah dilakukan perubahan")