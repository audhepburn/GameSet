import numpy as np
import enum


class Player():
    def __init__(self, id, score, played_oppo):
        self.id = id
        self.score = score
        self.played_oppo = played_oppo

    def one_vs_one():
        pass


class RoundSys():
    ''' 积分循环编排系统
    '''

    def __init__(self, round):
        self.round = round

    def pvp(self, player1, player2):
        if player2.id in player1.played_oppo:
            return False
        elif player1.score == player2.score:
            return "player match"
        else:
            return "not same score"

    def avail_oppo(self, player_status):
        for i in range(len(player_status)):
            pass


p1 = Player(3, 6, [2, 5])
p2 = Player(19, 6, [3, 4])
p3 = Player(1, 0, [6, 1])

sys = RoundSys(5)
flag = sys.pvp(p1, p2)
# print(flag)
sys.avail_oppo([p1, p2, p3])
