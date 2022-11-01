# Import modul dan fungsi yang dibutuhkan
from fungsi import length

def login(data_user, has_logged_in):
    # Kamus lokal
    # username, password: string
    # user_id : integer
    # has_logged_in : boolean

    # ALGORITMA
    username = input("Masukkan username: ")         # menerima input username dan password
    password = input("Masukkan password: ")
    if cekUsername(data_user, username):            # melakukan cek apakah username ada dan sesuai
        if cekPassword(data_user, password):        # melakukan cek apakah password dari username benar
            print(f"Halo {getNama(data_user, username)}! Selamat datang di Binomo!")
            has_logged_in = True                    # parameter has_logged_in menjadi True
            user_id = getID(data_user, username)
        else:                                       # jika salah
            has_logged_in = False
            user_id = 0
            print("Maaf, password yang Anda masukkan salah")
    else:
        has_logged_in = False
        user_id = 0
        print("Maaf, username salah atau tidak ditemukan")

    return has_logged_in, user_id                   # mereturn has_logged_in dan user_id untuk selanjutnya digunakan oleh fungsi lain pada main.py

# Fungsi-fungsi yang membantu

# Fungsi untuk mengecek username
def cekUsername(data, uname):
    valid = False
    for i in range(length(data)):   # melakukan pencocokkan data dengan iterasi pada array data
        if data[i][1] == uname:
            valid = True
            break
    return valid

# Fungsi untuk mendapatkan nama dari username pada data
def getNama(data, uname):
    for i in range(length(data)):   # melakukan pencocokkan data dengan iterasi pada array data
        if data[i][1] == uname:
            nama = data[i][2]
    return nama

# Fungsi untuk mendapatkan user_id dari username pada data
def getID(data, uname):
    for i in range(len(data)):      # melakukan pencocokkan data dengan iterasi pada array data
        if data[i][1] == uname:
            user_id = data[i][0]
    return user_id

# Fungsi untuk mengecek password
def cekPassword(data, passw):
    valid = False
    for i in range(length(data)):   # melakukan pencocokkan data dengan iterasi pada array data
        if data[i][3] == passw:
            valid = True
            break
    return valid