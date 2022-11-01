
# F12

def topup(user_id, gamecsv):
    saldo = int(input("Masukkan saldo: "))
    hasil = gamecsv[user_id][5] + saldo
    print("")
    print(f"Top up berhasil, Saldo {gamecsv[user_id][2]} bertambah menjadi {hasil}")
    print("")
    return hasil
