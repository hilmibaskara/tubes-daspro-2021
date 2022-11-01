user = [['id','username','nama','password','role','saldo'], ['0','admin','admin','admin','admin','0'], ['1','vieri','vieri fajar','123456','user','1234000']]
kepemilikan = [['game_id','user_id'], ['GAME001','0'],['GAME002','']]
riwayat = [['game_id','nama','harga','user_id','tahun_beli'], ['GAME001','Journey','120000','1','2020'], ['GAME002','vieri faja','1213','1','2020']]
game = [['id','nama','kategori','tahun_rilis','harga','stok'],['GAME001','Journey','Adventure','2020','120000','3'],['GAME002','Hitman 3','Action','2021','370000','5']]

from fungsiDanish import *

def melihatgame(user_id, kepemilikancsv, gamecsv) :
    dataIndex = []
    for row in range(length(kepemilikancsv)):
        if kepemilikancsv[row][1] == user_id:
            dataIndex = myappend(dataIndex, row)
    if length(dataIndex) == 0:
        print("Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.")
    else:
        OSoutput(dataIndex, gamecsv)