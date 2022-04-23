from fungsi import length

def login(data_user, has_logged_in):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if cekUsername(data_user, username):
        if cekPassword(data_user, password):
            print(f"Halo {getNama(data_user, username)}! Selamat data_userng di Binomo!")
            has_logged_in = True
        else:
            print("Maaf, password yang Anda masukkan salah")
    else:
        print("Maaf, username salah atau tidak ditemukan")

def cekUsername(data, uname):
    valid = False
    for i in range(length(data)):
        if data[i][1] == uname:
            valid = True
            break
    return valid

def getNama(data, uname):
    for i in range(length(data)):
        if data[i][1] == uname:
            nama = data[i][2]
    return nama

def cekPassword(data, passw):
    valid = False
    for i in range(length(data)):
        if data[i][3] == passw:
            valid = True
            break
    return valid