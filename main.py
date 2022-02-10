from operator import itemgetter


class Player():
    def __init__(self, id, score, played_oppo, mini_score=0, rank=0):
        self.id = id
        self.score = score
        self.played_oppo = played_oppo

    def one_vs_one():
        pass

    @property
    def get_info(self):
        return list((self.id, self.score, self.played_oppo))

    @property
    def get_score(self):
        return list((self.id, self.score))


class RoundSys():
    ''' Tournament Round Setup System
    '''

    def __init__(self, round, players):
        self.round = round
        self.players = players
        self.sorted_score_list = self.sort_score(players)

    def is_played_player(self, player1, player2):
        if player2.id in player1.played_oppo:
            return True
        else:
            return False

    def avail_oppo(self, player_status):
        for i in range(len(player_status)):
            pass

    def sort_score(self, players):
        score_list = []
        for item in players:
            score_list.append(item.get_info)
        print(score_list)
        if self.round % 2 == 1:     # odd round
            s = sorted(score_list, key=lambda id: id[0])
            sorted_score = sorted(
                s, key=lambda player: player[1], reverse=True)
        else:   # even round
            sorted_score = sorted(
                score_list, key=itemgetter(1, 0), reverse=True)
        # print(sorted_score)
        return sorted_score

    def pair_oppo(self, sorted_score_list):
        for i in range(1, 10):
            player1 = sorted_score_list[0][0]
            player2 = sorted_score_list[i][0]
            player2_played_list = sorted_score_list[i][2]
            if player1 not in player2_played_list:
                del self.sorted_score_list[0]
                del self.sorted_score_list[i-1]
                return str(player1) + " - " + str(player2)
            else:
                continue

    def match_arrangement(self):
        for item in self.sorted_score_list:
            print(item)
        print()
        while self.sorted_score_list:
            # print(self.sorted_score_list)
            print(self.pair_oppo(self.sorted_score_list))


p1 = Player(3, 6, [2, 5])
p2 = Player(1, 0, [6, 1])
p3 = Player(19, 8, [3, 7])
p4 = Player(7, 8, [19, 16])
p5 = Player(10, 4, [1, 2])
p6 = Player(33, 4, [4, 16])
# p7 = Player(31, 2, [3, 11])
all_player_status = [p1, p2, p3, p4, p5, p6]
# print(p1.get_info)
sys = RoundSys(5, all_player_status)
sys.match_arrangement()
# sys.sort_score(all_player_status)
