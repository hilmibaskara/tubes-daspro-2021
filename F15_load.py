from operasi_matriks import read_csv
import argparse

def load(folder):
   data_user = read_csv(folder + "user.csv", 'user')
   data_game = read_csv(folder + "game.csv", 'game')
   data_kepemilikan = read_csv(folder + "kepemilikan.csv", 'kepemilikan')
   data_riwayat = read_csv(folder + "riwayat.csv", 'riwayat')
   return data_user, data_game, data_kepemilikan, data_riwayat

