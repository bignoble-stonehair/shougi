import numpy as np

OUT_OF_BOARD = 64
EMPTY = 0
FU = 1
KYOU = 2
KEI = 3
GIN = 4
KIN = 5
KAKU = 6
HI = 7
GYOKU = 8
PROMOTION = 8
TO = PROMOTION + FU
N_KYOU = PROMOTION + KYOU
N_KEI = PROMOTION + KEI
N_GIN = PROMOTION + GIN
UMA = PROMOTION + KAKU
RYU = PROMOTION + HI
OPPONENT = 16
OPP_FU = OPPONENT + FU
OPP_KYOU = OPPONENT + KYOU
OPP_KEI = OPPONENT + KEI
OPP_GIN = OPPONENT + GIN
OPP_KIN = OPPONENT + KIN
OPP_KAKU = OPPONENT + KAKU
OPP_HI = OPPONENT + HI
OPP_GYOKU = OPPONENT + GYOKU
OPP_TO = OPPONENT + TO
OPP_N_KYOU = OPPONENT + N_KYOU
OPP_N_KEI = OPPONENT + N_KEI
OPP_N_GIN = PROMOTION + N_GIN
OPP_UMA = PROMOTION + UMA
OPP_RYU = PROMOTION + RYU

koma_char = ["　　","△歩","△香","△桂","△銀","△金","△角","△飛","△玉",
           "△と","△杏","△圭","△全","△金","△馬","△竜",
           "　　","▼歩","▼香","▼桂","▼銀","▼金","▼角","▼飛","▼王",
           "▼と","▼杏","▼圭","▼全","▼金","▼馬","▼竜"]

hand = np.zeros((2, HI + 1))
board = [[OPP_KYOU,OPP_KEI,OPP_GIN,OPP_KIN,OPP_GYOKU,OPP_KIN,OPP_GIN,OPP_KEI,OPP_KYOU],
         [EMPTY,OPP_HI,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,OPP_KAKU,EMPTY],
         [OPP_FU,OPP_FU,OPP_FU,OPP_FU,OPP_FU,OPP_FU,OPP_FU,OPP_FU,OPP_FU],
         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
         [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
         [FU,FU,FU,FU,FU,FU,FU,FU,FU],
         [EMPTY,KAKU,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,HI,EMPTY],
         [KYOU,KEI,GIN,KIN,GYOKU,KIN,GIN,KEI,KYOU]]
situation = [hand, board]

def display_kyokumen(situation):
    print("先手 持ち駒 \n")
    for koma in range(FU, HI + 1):
        if hand[0][koma] == 1:
            print("%s " % koma_char[koma])
        elif hand[0][koma] > 1:
            print("%s%d " % (koma_char[koma], (situation[0])[1][koma]))
    dan = ["｜一\n","｜二\n","｜三\n","｜四\n","｜五\n","｜六\n","｜七\n","｜八\n","｜九"]
    print("  ９　８　７　６　５　４　３　２　１" )
    print("--------------------------------------")
    for i in range(0, 9):
        print("|", end='')
        for suji in range(0, 9):
            print("%s" % koma_char[(situation[1])[i][suji]], end='')
        print(dan[i])
    print("--------------------------------------")
    print("後手 持ち駒 \n")
    for koma in range(FU, HI + 1):
        if hand[1][koma] == 1:
            print("%s " % koma_char[koma])
        elif hand[1][koma] > 1:
            print("%s%d " % (koma_char[koma],(situation[0])[1][koma]))
     
display_kyokumen(situation)

def isOpponent(koma):
    if(koma > 16):
        return True
    else:
        return False

if(isOpponent(board[0][1])):
    print("敵です")


