import os 
from fungsi import length

"""Buat ngecek"""
"""data_user = [['id','username','nama','password','role,saldo'], ['0','admin','admin','admin','admin','0'], ['1','vieri','vieri fajar','123456','user','1234000']]
data_kepemilikan = [['game_id','user_id'], ['GAME001','0'], ['GAME001','2']]
data_riwayat = [['game_id','nama','harga','user_id','tahun_beli'], ['GAME001','Journey','120000','1','2020'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaa','asads','1213','1','2020']]
data_game = [['id;nama;kategori','tahun_rilis','harga','stok'],['GAME001','Journey','Adventure','2020','120000','3'],['GAME002'',Hitman 3','Action','2021','370000','5']]"""



def dftostr(df):
    string=[]
    for x in df:
        tem=''
        count=1
        for i in x:
            if count!=length(x):
                tem=tem+i+';'
            elif count==length(x):
                tem+=i
            count+=1
        string+=[tem]
    return string
def save(data_user, data_kepemilikan, data_riwayat, data_game):
    nama_folder=input("Masukkan nama folder: ")
    if not (os.path.exists(nama_folder)):
        os.makedirs(nama_folder)

    user=dftostr(data_user)
    kepemilikan=dftostr(data_kepemilikan)
    riwayat=dftostr(data_riwayat)
    game=dftostr(data_game)
    with open(f"{nama_folder}/user.csv",'w') as file:
        for i in user:
            file.write(i+"\n")
    with open(f"{nama_folder}/kepemilikan.csv",'w') as file:
        for i in kepemilikan:
            file.write(i+"\n")
    with open(f"{nama_folder}/riwayat.csv", 'w') as file:
        for i in riwayat:
            file.write(i+"\n")
    with open(f"{nama_folder}/game.csv", 'w')  as file:
        for i in game:
            file.write(i+"\n")   


