class SnakesLadders():
    def __init__(self):
        self.players = {'p1': Player(is_next=True, number=1),
                        'p2': Player(is_next=False, number=2),
                       }
        self.shortcuts = {'36':44,'16':6,'49':11,'46':25,'62':19,'64':60,
                          '74':53,'89':68,'92':88,'95':75,'99':80, '2':38,
                          '7':14,'8':31,'15':26,'21':42,'28':84,'51':67,'78':98,
                          '87':94,'71':91}
        self.ongoing = True

    def play(self, die1, die2):
        if self.ongoing:
            player = self.get_this_turns_player()
            player.pos += die1 + die2
            self.check_and_move_shortcut(player)
            if player.pos == 100:
                self.set_game_over()
                return f"Player {player.number} Wins!"
            if player.pos > 100:
                player.pos = 100 - (player.pos - 100)
                self.check_and_move_shortcut(player)
            if not die1 == die2:
                self.switch_turns()
            return player.return_status()
        else:
            return 'Game over!'

    def change_player_pos(player, die_sum):
        return player.pos + die_sum

    def check_and_move_shortcut(self, player):
        if str(player.pos) in self.shortcuts.keys():
            player.pos = self.shortcuts[str(player.pos)]

    def get_this_turns_player(self):
        for p_str, p in self.players.items():
            if p.is_next:
                return self.players[p_str]

    def switch_turns(self):
        self.players['p1'].is_next = not(self.players['p1'].is_next)
        self.players['p2'].is_next = not(self.players['p2'].is_next)

    def set_game_over(self):
        self.ongoing = False


class Player():
    def __init__(self, is_next, number):
        self.pos = 0
        self.is_next = is_next
        self.number = number
        self.status = 'playing'

    def return_status(self):
        return f'Player {self.number} is on square {self.pos}'
