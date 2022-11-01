import os
from fungsiDanish import *
"""Buat ngecek"""
"""data_user = [['id','username','nama','password','role,saldo'], ['0','admin','admin','admin','admin','0'], ['1','vieri','vieri fajar','123456','user','1234000']]
data_kepemilikan = [['game_id','user_id'], ['GAME001','0'], ['GAME001','2']]
data_riwayat = [['game_id','nama','harga','user_id','tahun_beli'], ['GAME001','Journey','120000','1','2020'], ['aaaaaaaaaaaaaaaaaaaaaaaaaaa','asads','1213','1','2020']]
data_game = [['id;nama;kategori','tahun_rilis','harga','stok'],['GAME001','Journey','Adventure','2020','120000','3'],['GAME002'',Hitman 3','Action','2021','370000','5']]"""

def Length(x) :
    if(type(x)==type(1)) :
        temp=x
        length=0

        while(temp>0) :
            length+=1
            temp=temp//10
    else :
        length=0
        for i in x :
            length+=1
    return length

def dftostr(df):
    string=[]
    for x in df:
        tem=''
        count=1
        for i in x:
            if count!=Length(x):
                tem=tem+str(i)+';'
            elif count==Length(x):
                tem+=str(i)
            count+=1
        string+=[tem]
    return string
    
def nambahjudul(list, listasli):
    for i in range(length(listasli)):
        list = myappend(list, listasli[i])
    return list

def save(data_user, data_kepemilikan, data_riwayat, data_game):
    data_user1 = [["id", "username", "nama", "password", "role", "saldo"]]
    data_kepemilikan1 = [["game_id", "user_id" ]]
    data_riwayat1 = [["game_id", "nama", "harga", "user_id", "tahun_beli"]]
    data_game1 = [["id", "nama", "kategori", "tahun_rilis", "harga", "stok", ]]

    data_user1 = nambahjudul(data_user1, data_user)
    data_kepemilikan1 = nambahjudul(data_kepemilikan1, data_kepemilikan)
    data_riwayat1 = nambahjudul(data_riwayat1, data_riwayat)
    data_game1 = nambahjudul(data_game1, data_game)
    nama_folder=input("Masukkan nama folder: ")
    if not (os.path.exists(nama_folder)):
        os.makedirs(nama_folder)

    print(data_user1)
    print(data_kepemilikan1)
    user=dftostr(data_user1)
    kepemilikan=dftostr(data_kepemilikan1)
    riwayat=dftostr(data_riwayat1)
    game=dftostr(data_game1)
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


