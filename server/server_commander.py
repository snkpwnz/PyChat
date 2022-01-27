from mini_games import GamesFactory
from currency import DollarsValueAdapter


class Commander:
    def __init__(self):
        self.COMMANDS = {
            "/help": self.help,
            "/play": self.play,
            "/dollar": self.dollar
            }

    def play(self, data, sock):
        game = GamesFactory.select_game(data.split(' ')[1], sock)
        game.play_game()

    def dollar(self, data, sock):
        rate = DollarsValueAdapter()
        sock.send(f'Current dollar exchange rate: {rate.get()}$'.encode())

    def help(self, data, sock):
        help_message = '''Chat help menu:
                        /help: Display help
                        /play: Select game to play
                        /dollar Current dollar exchange rate'''
        sock.send(help_message.encode())

    def command(self, data, sock):
        for command in self.COMMANDS.keys():
            if data.startswith(command):
                self.COMMANDS[command](data, sock)


commander = Commander()
