"""Rock_paper_scissor.py

A very simple text-based game, utilizing shelve to save the high score

Author: Daniel Lefevre
August 30, 2017

TODO:
* Save table of high scores instead of just one

"""

import random
from save import save_score, load_score

PLAYS = ['rock', 'paper', 'scissors']
PLAY = True

class Game():
    
    #New game, score starts with 0
    def __init__(self):
        self.player_score = 0
        try:
            self.high_score = load_score()
        except:
            self.high_score = ["", 0]
        if self.high_score[1] != 0:
			print "The current high score is: " + str(self.high_score[1]) + " by player " + self.high_score[0]
        self.player_name = raw_input('Enter your name: ')

    def player_win(self):
        print "You win! :)"
        self.player_score += 1
        
    def player_lose(self):
        print "You lose. :("
        self.player_score -= 1
        
    def tie_game(self):
        print "Tie game... :|"

    def play_round(self):
        player_choice = ""
        computer_choice = random.choice(PLAYS)
        #While loop continues until user makes a valid play
        while player_choice not in PLAYS:
            player_choice = raw_input("To play, type \"rock\", \"paper\", or \"scissors\" ")
            if player_choice not in PLAYS:
                print "Sorry, that wasn't a valid play. Please choose again.\n"
            print "Computer chooses \"" + computer_choice + "\""
        #handle game logic
        if player_choice == 'rock':
            if computer_choice == 'scissors':
                Game.player_win(self)
            if computer_choice == 'paper':
                Game.player_lose(self)
            if computer_choice == 'rock':
                Game.tie_game(self)
        if player_choice == 'paper':
            if computer_choice == 'rock':
                Game.player_win(self)
            if computer_choice == 'scissors':
                Game.player_lose(self)
            if computer_choice == 'paper':
                Game.tie_game(self)
        if player_choice == 'scissors':
            if computer_choice == 'paper':
                Game.player_win(self)
            if computer_choice == 'rock':
                Game.player_lose(self)
            if computer_choice == 'scissors':
                Game.tie_game(self)
        

game1 = Game()
while PLAY:
    game1.play_round()
    print "Your score is: " + str(game1.player_score)
    play_again = ""
    while play_again not in ['y', 'ye', 'yes','n', 'no']:
        play_again = raw_input("type '(y)es' to play again or '(n)o' to quit\n")
    if play_again not in ['y', 'ye', 'yes']:
        if game1.player_score > game1.high_score[1]:
            save_score([game1.player_name, game1.player_score])
        PLAY = False
