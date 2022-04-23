user = [['id','username','nama','password','role','saldo'], ['0','admin','admin','admin','admin','0'], ['1','vieri','vieri fajar','123456','user','1234000']]
kepemilikan = [['game_id','user_id'], ['GAME001','0'],['GAME002','']]
riwayat = [['game_id','nama','harga','user_id','tahun_beli'], ['GAME001','Journey','120000','1','2020'], ['GAME002','vieri faja','1213','1','2020']]
game = [['id','nama','kategori','tahun_rilis','harga','stok'],['GAME001','Journey','Adventure','2020','120000','3'],['GAME002','Hitman 3','Action','2021','370000','5']]



def melihatgame(kepemilikan, user, game, username) :
    indeks = 0
    for i in (user) :
        if i[1] == username :
            indeks = i[0]
    
    a = 1
    kondisi = False
    for i in (kepemilikan) :
        if i[1] == indeks :
            kondisi = True
            for j in (game) :
                if j[0] == i[0] :
                    print(f"{a}.{j[0]} | {j[1]} | {j[2]} | {j[3]} | {j[4]}")
                    a += 1
    if kondisi == False :
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")


melihatgame(kepemilikan, user, game, 'vieri')