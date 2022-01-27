import abc
import random
import time
from abc import ABCMeta
from socket import SHUT_RDWR


class Game(metaclass=ABCMeta):

    @abc.abstractmethod
    def play_game(self):
        pass


class Roulette(Game):
    def __init__(self, sock):
        self.__sock = sock

    def play_game(self):
        self.__sock.send('Let\'s play roulette!\nLoading the gun..'.encode())
        result = random.randint(0,1)
        time.sleep(2)
        if result == 0:
            self.__sock.send('BOOM!\nYou died'.encode())
            time.sleep(5)
            self.__sock.shutdown(SHUT_RDWR)
        else:
            self.__sock.send('Huh.. You are alive!'.encode())


class SimpleGame(Game):
    def __init__(self, sock):
        self.__sock = sock

    def play_game(self):
        while True:
            self.__sock.send("Enter player \n 1. Rock \n 2. Paper \n 3. Scissor".encode())
            game_dict = {1: 3, 2: 2, 3: 1}
            player = int(self.__sock.recv(1024).decode().split(' - ')[1])

            while player > 3 or player < 1:
                self.__sock.send("Please enter a valid number!".encode())
                player = int(self.__sock.recv(1024).decode().split(' - ')[1])

            comp = random.randint(1, 3)

            if comp == 1:
                comp_choice_name = 'Rock'
            elif comp == 2:
                comp_choice_name = 'Paper'
            else:
                comp_choice_name = 'Scissor'

            self.__sock.send(f"Computer choice is: {comp_choice_name}".encode())

            players_choice = game_dict.get(player)
            comps_choice = game_dict.get(comp)
            dif = players_choice - comps_choice

            if dif in [-1, 2]:
                self.__sock.send('You Win!.'.encode())
            elif dif in [-2, 1]:
                self.__sock.send('Comp Wins.'.encode())
            else:
                self.__sock.send('Draw, Please continue. '.encode())

            self.__sock.send('Do you wanna play again? (Y/N)'.encode())
            answer = self.__sock.recv(1024).decode().split(' - ')[1]
            if answer == "N" or answer == "n":
                break

        self.__sock.send("Thanks for playing".encode())


class GamesFactory:
    @staticmethod
    def select_game(game_name, sock):
        if game_name == 'roulette':
            return Roulette(sock)
        if game_name == 'simple':
            return SimpleGame(sock)
