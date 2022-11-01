# output yang berulang di main.py ditulis di sini supaya efisien

# print menu hanya dapat diakses admin
def admin_only():
   print("Maaf, fungsi ini hanya bisa diakses oleh admin")

# print menu hanya dapat diakses user
def user_only():
   print("Maaf, fungsi ini hanya bisa diakses oleh user")

# print menu hanya dapat diakses ketika sudah login
def login_first():
   print("Silakan login terlebih dahulu")

# print menu klik enter untuk melanjutkan
def enter_done():
   print("\nKlik enter untuk melanjutkan")
   input("")