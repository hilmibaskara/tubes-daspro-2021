from operasi_matriks import read_csv
from time import sleep

def load():
   # kamus lokal
   # data_user, data_kepemilikan, data_riwayat, data_game : array of list
   
   # algoritma
   print("Loading.", end = '')
   sleep(0.50)
   print(".", end = '')
   sleep(0.50)
   print(".")
   sleep(0.50)

   data_user = read_csv("user.csv", 'user')
   data_game = read_csv("game.csv", 'game')
   data_kepemilikan = read_csv("kepemilikan.csv", 'kepemilikan')
   data_riwayat = read_csv("riwayat.csv", 'riwayat')
   return data_user, data_game, data_kepemilikan, data_riwayat
