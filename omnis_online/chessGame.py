import chess
import recognition as r
import playsound as ps
from fuzzywuzzy import fuzz

'''comments marked with """""" are failed attempts to use some tools. comments marke with # are explaining the code'''

def print_board(board):
    print(board)

#fuzzywuzzy failed application
""" def bestCorrespond(move, targetCoord):
    best_match = None
    highest_ratio = 0
    for coord in targetCoord:
        ratio = fuzz.ratio(move.lower(), coord)
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = coord
    return best_match, highest_ratio """

#class Chess created for better usage of the code in recognition.py
class Chess:
    def __init__(self):
        self.board = chess.Board()
        self.move = None
    
    def play_game(self):
        # creates object from class reconhecimento (reconhecimento.Reconhecimento())
        rec1 = r.Reconhecimento()

        # defines the board as the chessboard in class Board from python-chess library
        self.board = chess.Board()
        player_turn = "White"  # White starts the game
        print_board(self.board)
        move1 = 0
        move2 = 0
        while not self.board.is_game_over():
            print(f"{player_turn}'s turn")
            """ move = input("Enter your move in UCI format (e.g., e2e4): ")
            letras = 'abcdefgh'
            numeros = '12345678'
            targetCoord = [
                f"{letter1}{number1}{letter2}{number2}" for letter1 in letras for number1 in numeros for letter2 in letras for number2 in numeros] """
            
            # defines move as user's audio
            moves = rec1.reconhecerJogada()
            move1 = moves[0][0]
            move2 = moves[0][1]

            '''if move1 not in targetCoord or move2 not in targetCoord:
                move1 = bestCorrespond(move1, targetCoord)
                move2 = bestCorrespond(move2, targetCoord)'''
            
            self.move = move1 + move2

            """ move = bestCorrespond(move, targetCoord)[0] """

            print(self.move)

            '''print(f"{move} é o movimento desejado? (sim ou não)")
            keyValid = rec1.reconhecerAudio()
            if keyValid == "não":
                pass #função para voltar e reconhecer novamente
            # print(rec1.jogada_f)'''

            try:
                print_board()
                self.board.push_uci(self.move)
            except ValueError:
                print("Formato inválido ou movimento ilegal. Tente novamente")
                continue

            print_board(self.board)
            player_turn = "Black" if player_turn == "White" else "White"

        print("Fim de jogo!")
        print("Resultado: ", self.board.result())

