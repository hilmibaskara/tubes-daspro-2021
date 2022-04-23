
# F12

def topup(user_id, gamecsv):
    saldo = int(input("Masukkan saldo: "))
    gamecsv[user_id-1][5] += saldo
    print("")
    print(f"Top up berhasil, Saldo {gamecsv[user_id-1][2]} bertambah menjadi {gamecsv[user_id-1][5]}")

