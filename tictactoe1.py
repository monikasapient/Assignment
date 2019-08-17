#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  7 00:11:15 2019

@author: monahirw
"""

import argparse

class tictactoe:
    def __init__(self,size=3):
        self.size = size
        self.board = [ 'E' for i in range(0,self.size*self.size) ]
        self.moves_list = []
        self.winner = None

    def print_board(self):
        for j in range(0,self.size*self.size,self.size):
            for i in range(self.size):
                if self.board[j+i] == 'E':
                    print("%d |" %(j+i),end='')
                else:
                    print("%s |" %self.board[j+i],end = '')
    
            print("\n")


    def available(self):
        moves = []
        for i,v in enumerate(self.board):
            if v=='E':
                moves.append(i)
        return moves

    def mark(self,marker,pos):
        self.board[pos] = marker
        self.moves_list.append(pos)

    def reset_last_move(self):
        self.board[self.moves_list.pop()] = 'E'
        self.winner = None


    def row_win(self, marker):
        k = 0 
        for i in range(self.size):
            count = 0 
            for j in range(self.size):
                if(self.board[k]==marker):
                    count = count + 1
                k = k+1
            if(count ==self.size):
                return True
        return False
    
        
    def col_win(self, marker):      
        for i in range(self.size):
            k = i
            count = 0 
            for j in range(self.size):
                if(self.board[k]==marker):
                    count = count + 1
                k = k+self.size
            if(count ==self.size):
                return True
        return False
        
        
    def diag_win1(self, marker):
        count =0
        k =0
        for i in range(self.size):
            if(self.board[k]== marker):
                count = count +1
                k = (i+1)*(self.size + 1)
        if count == self.size:
            return True
        return False
 
    def diag_win2(self, marker):
        count =0
        for i in range(self.size):
            k = (i+1)*(self.size - 1)
            if(self.board[k]== marker):
                count = count +1                
        if count == self.size:
            return True
        return False
        

    def any_win_pos(self,marker):
        return self.row_win(marker) or self.col_win(marker) or self.diag_win1(marker) or self.diag_win2(marker)
    
    
    
    def is_gameover(self):
        if self.any_win_pos('X') == True:
            self.winner = 'X'
            return True
        elif self.any_win_pos('O') == True:
            self.winner = 'O'
            return True
        elif 'E' not in self.board:
            self.winner = 'E'
            return True
        return False









    def play(self,player1,player2,b):
        self.p1 = player1
        self.p2 = player2
        for i in range(self.size*self.size):
            self.print_board()            
            if i%2==0:
                if self.p1.type == 'H':
                    print("\n[Human Move]")
                else:
                    print("\n[Computer Move]")
                self.p1.move(self)
            else:
                if self.p2.type == 'H':
                    print("\n[Human Move]")
                else:
                    print("\n[Computer Move]")
                self.p2.move(self)
                
            if self.is_gameover():
                self.print_board()
                if self.winner == 'E':
                    print("\nGame over with Draw")
                else:
                    print("\nWinner : %s" %self.winner)
                    if b == 1:
                        self.reset_last_move()
                return

class Human:
    def __init__(self,marker):
        self.marker = marker
        self.type = 'H'   
    def move(self, gameinstance):
        while True:        
            m = input("Input position:")
            try:
                m = int(m)
            except:
                m = -1        
            if m not in gameinstance.available():
                print("Invalid move. Retry")
            else:
                break    
        gameinstance.mark(self.marker,m)
         
class AI:
    def __init__(self, marker):
        self.marker = marker
        self.type = 'C'
        if self.marker == 'X':
            self.opponentmarker = 'O'
        else:
            self.opponentmarker = 'X'


    def move(self,gameinstance):
        move_position,score = self.maximized_move(gameinstance)
        gameinstance.mark(self.marker,move_position)


    def maximized_move(self,gameinstance):
        bestscore = None
        bestmove = None
        for m in gameinstance.available():
            gameinstance.mark(self.marker,m)        
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.minimized_move(gameinstance)        
            gameinstance.reset_last_move()           
            if bestscore == None or score > bestscore:
                bestscore = score
                bestmove = m
        return bestmove, bestscore


    def minimized_move(self,gameinstance):
        bestscore = None
        bestmove = None
        for m in gameinstance.available():
            gameinstance.mark(self.opponentmarker,m)       
            if gameinstance.is_gameover():
                score = self.get_score(gameinstance)
            else:
                move_position,score = self.maximized_move(gameinstance)       
            gameinstance.reset_last_move()           
            if bestscore == None or score < bestscore:
                bestscore = score
                bestmove = m
        return bestmove, bestscore


    def get_score(self,gameinstance):
        if gameinstance.is_gameover():
            if gameinstance.winner  == self.marker:
                return 1 
            elif gameinstance.winner == self.opponentmarker:
                return -1
        return 0 

        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    parser.add_argument("size", "--board_size", type=int,
                    help="size (n) of n*n board" )
    
    parser.add_argument("p1", "--player1",
                    help="H for human C for computer K for kid" )
    
    parser.add_argument("p2", "--player2",
                    help="H for human C for computer K for kid" )
    
    parser.add_argument("marker","--marker",help="X or O")
    
    parser.add_argument("biased","--biased",help="y or n")
    
    
    s = args.size
    p1 = args.p1
    p2 = args.p2
    marker1 = args.marker
    bias = args.biased 

    game=tictactoe(s) 
    
    if p1 == "H":
        player1 = Human(marker1)
    elif p1 == "C":
        player1 = AI(marker1)
    
    if marker1=="X":
        marker2 = "O"
    else:
        marker2 = "X"
        
    if p2 == "H":
        player2 = Human(marker2)
    elif p2 == "C":
        player2 = AI(marker2)
        
    if bias == 'y':
        b = 0
    else:
        b = 1 
   
    game.play( player1, player2, b)
    
    
#parser.add_