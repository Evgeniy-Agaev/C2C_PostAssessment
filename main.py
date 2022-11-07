####################
#Code2College Post Assessment Assignment
#Start Date: Nov 4th, 2022
#End Date: 
#Total Time Spent: 
#Name: Evgeniy Agaev
#Project Description: Working Connect 4 Game using tkinter gui framework.  
####################

def print_gameboard():
  for row in gameboard:
    for col in row:
      print(col, end="  ")
    print(" ")

def drop_piece(collumn, player_token):
  for row in range(0, height):
    if(gameboard[row][collumn] != '-'):
      gameboard[row -1][collumn] = player_token
      return gameboard
    

  gameboard[height -1][collumn] = player_token
  return gameboard

def check_winner(player_token):
  for row in range(0, height):
    for col in range(0, width):
      if(gameboard[row][col] == player_token):
        # print(gameboard[row][col] ," == " , player_token,"???")
        if(row <= 2):
          #checking horizontal row
          if (gameboard[row][col] == gameboard[row + 1][col]) and (gameboard[row + 2][col] == gameboard[row + 3][col]) and(gameboard[row + 1][col] == gameboard[row + 2][col]):
            print("made it to the col check")
            return True
        if(col <= 2):
          if(gameboard[row][col] == gameboard[row][col + 1]) and (gameboard[row][col + 2] == gameboard[row][col + 3]) and(gameboard[row][col + 1] == gameboard[row][col + 2]):

            
            
            print("made it to the row check")
            return True
        
        if(row <=2) and (col <=2):
          if (gameboard[row][col] == gameboard[row + 1][col + 1]) and (gameboard[row + 2][col + 2] == gameboard[row + 3][col + 3]) and(gameboard[row + 1][col + 1] == gameboard[row + 2][col + 2]):
            print("made it to the diagonal negative check")
            return True
        if(row<= 2) and (col >=3):
          print("is in the top right")
          if (gameboard[row][col] == gameboard[row + 1][col - 1]) and (gameboard[row + 2][col - 2] == gameboard[row + 3][col - 3]) and(gameboard[row + 1][col-1] == gameboard[row + 2][col -2]):
            print("made it to the diagonal positive check")
            return True
        
  return False          
            
      
gameboard = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
gameboard_size = width, height = len(gameboard), len(gameboard[0])    


import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()
frame = ttk.Frame(window)
window.title("Hello wold")
window.geometry("300x300")




tk.mainloop()



print("Hello this is a Connect 4 Game!")
print("You are player X, while the computer is player Y")
print("To play the game, input a number from 1-6 each time it is your turn")
print("This will be the collumn you will be dropping your piece")


first_player = int(random.randrange(50,101)/50 +0.5)

game_running = True
round = 1
while game_running:

  if(round + first_player)%2 ==0:
    
  
    #computer moves
    playerOne_move = random.randrange(1, 7)
    drop_collumn = playerOne_move -1
    drop_piece(drop_collumn, "X")
    print_gameboard()
    if(check_winner("X")):
      print("Computer won!")
      break
  else:
    
    playerTwo_move = int(input("What is your move? (1-6)"))
    drop_collumn = playerTwo_move -1
    drop_piece(drop_collumn, "O")
    print_gameboard()
    if(check_winner("O")):
      print("You won!")
      break
    
  round +=1

  ##check if anyone won
  

  





