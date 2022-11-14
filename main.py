#READ THIS: 
#Repl.it is a little buggy when it comes to tkinter. 

####################
#Code2College Post Assessment Assignment
#Start Date: Nov 4th, 2022
#End Date: Nov 12th, 2022
#Total Time Spent: About 2 Hours
#Name: Evgeniy Agaev
#Project Description: Working Connect 4 Game using tkinter gui framework.  
####################

#Take turns between players to play fair. 


import random
import tkinter
from tkinter import *
from PIL import ImageTk, Image



def print_gameboard(): #function to print the gameboard in the terminal
  for row in gameboard:
    for col in row:
      print(col, end="  ")
    print(" ")


def clear_gameboard(): #clears gameboard
    for row in range(width):
        for col in range(height):
            gameboard[row][col] = '-'
    

def drop_piece(collumn, player_token): #drops a piece downt the collumn and ends on top of the last piece.
  for row in range(0, height):
    if(gameboard[row][collumn] != '-'):
      gameboard[row -1][collumn] = player_token 
      return (row - 1) #returns the row the piece was dropped on. 
    

  gameboard[height -1][collumn] = player_token
  return (height - 1) #returns the row the piece was dropped on.

def check_winner(player_token): #checks for the winner
  for row in range(0, height):
    for col in range(0, width): 

        #The pattern for the "winning" combitnations is that all combinations (horizontal, vertical, and diagonal) all
        # had similar starting positions. 


      if(gameboard[row][col] == player_token): #first iterating through each token checking if the token is one team's.
        
        if(row <= 2): #this is to check for all tokens in the top 3 rows of the board. 
          #this method checks for "vertical" lines in 4 lines
          
          if (gameboard[row][col] == gameboard[row + 1][col]) and (gameboard[row + 2][col] == gameboard[row + 3][col]) and(gameboard[row + 1][col] == gameboard[row + 2][col]):
            #checks 4 tiles to see if they won. 
            return True
        if(col <= 2): #this is for horiztonal lines
          if(gameboard[row][col] == gameboard[row][col + 1]) and (gameboard[row][col + 2] == gameboard[row][col + 3]) and(gameboard[row][col + 1] == gameboard[row][col + 2]):

            
            
            
            return True
        
        if(row <=2) and (col <=2): #checking if negative diagonal is the winning combination. 
          #checks if starts in uppermost left corner. 
          if (gameboard[row][col] == gameboard[row + 1][col + 1]) and (gameboard[row + 2][col + 2] == gameboard[row + 3][col + 3]) and(gameboard[row + 1][col + 1] == gameboard[row + 2][col + 2]):
            
            return True
        if(row<= 2) and (col >=3): #checking if positive diagonal is the winning combination. 
          #checks if the start is in the uppermost right corner and counts down from there. 
          if (gameboard[row][col] == gameboard[row + 1][col - 1]) and (gameboard[row + 2][col - 2] == gameboard[row + 3][col - 3]) and(gameboard[row + 1][col-1] == gameboard[row + 2][col -2]):
            
            return True
        
  return False


def play_pressed():
   
    global buttons 
    for widget in root.winfo_children(): #destroys all widgets and wipes the screen clean. 
                widget.destroy()
    root.configure(bg="#d9d9d9") #sets default background color
    
    #each of these buttons connect to a row. If they are clicked, then they are connected to a "drop_piece" function.
    row_1 = tkinter.Button(root, text="Row 1", command=lambda b= 0 : drop_piece_tkinter(b)) 
    row_2 = tkinter.Button(root, text="Row 2", command=lambda b= 1 : drop_piece_tkinter(b))
    row_3 = tkinter.Button(root, text="Row 3", command=lambda b= 2 : drop_piece_tkinter(b))
    row_4 = tkinter.Button(root, text="Row 4", command=lambda b= 3 : drop_piece_tkinter(b))
    row_5 = tkinter.Button(root, text="Row 5", command=lambda b= 4 : drop_piece_tkinter(b))
    row_6 = tkinter.Button(root, text="Row 6", command=lambda b= 5 : drop_piece_tkinter(b))
    buttons = [row_1, row_2, row_3, row_4, row_5, row_6]

#sets up all the buttons in a grid line, and makes them size with the screen.
    row_1.grid(column=0, row= 0, sticky = tkinter.EW)
    row_2.grid(column=1, row = 0, sticky= tkinter.EW)
    row_3.grid(column=2, row= 0, sticky = tkinter.EW)
    row_4.grid(column=3, row = 0, sticky= tkinter.EW)
    row_5.grid(column=4, row= 0, sticky = tkinter.EW)
    row_6.grid(column=5, row = 0, sticky= tkinter.EW) 

    root.grid_columnconfigure((0,1,2,3,4,5), weight=1) #adds weight to each of the collumns, so they size with the window.

    for i in range(width): #sets the placeholder items in a grid, to create a more "realistic image" to the players
        for j in range(height):
            placeholder = tkinter.Label(root, image = placeholder_token)
            placeholder.grid(column=i, row = (j+ 1), pady= 20)
    
    

def drop_piece_tkinter(b): #drops the piece on the screen. 
    global round
    global buttons
    
    
    if (round + first_player)%2 ==0: #round is set and depending on each round, the game will either drop a red or a black piece.
      #every round should be different.

        
      
            
        

        player_move = drop_piece(b, 'X') + 1 #sets player move as a value. 
        
        label = tkinter.Label(root, image=red_token)
        label.grid(column = b, row= player_move) #places the piece based on the player_move
        round = round + 1 #increments the round by 1
        if(check_winner('X')): #checks the winnder each round. 
            for widget in root.winfo_children(): #destoys everything on the screen. 
                widget.destroy()
            root.configure(bg='#c41a1a') #sets background to red
            win_label = tkinter.Label(root, text="Red won", font="Helvetica 25 bold") #red won label
            win_label.place(relx= 0.5, rely= 0.5, anchor=tkinter.CENTER) #places label in center

             #a play again button connects to the play_pressed function before. 
            play_again_button = tkinter.Button(root, text="Play Again?", command=play_pressed)
            play_again_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            clear_gameboard() #clears the "data framework" of the board array. 
        
    else:
        player_move = drop_piece(b, 'O') + 1 #drops piece with the black token on the screen and the '0' token in the array. 
        

        label = tkinter.Label(root, image=black_token)
        label.grid(column = b, row= player_move) #places a black token based on player move. 
        round = round + 1 #increments the round
        if(check_winner('O')): #checks if black won
            for widget in root.winfo_children():
                widget.destroy() #if black won, everything on screen is destroyed
            root.configure(bg='#525252') #dark grey background. 
            win_label = tkinter.Label(root, text="Black won", font="Helvetica 25 bold") #black won
            win_label.place(relx= 0.5, rely= 0.5, anchor=tkinter.CENTER)
            play_again_button = tkinter.Button(root, text="Play Again?", command=play_pressed) #play again button
            play_again_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
            clear_gameboard() #clears the virtual board. 
            
    



##############          

#really the entire program loop happens below this line. 
#this is the gameboard
gameboard = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
gameboard_size = width, height = len(gameboard), len(gameboard[0])  #sets width and height of board. 
first_player = int(random.randrange(50,101)/50 +0.5) #half chance that black or red is first.

round = 1 #sets the round to be 1
buttons = None #buttons for each row. 

root = tkinter.Tk() #entire window
root.title("Connect 4") #title
root.geometry("500x500") #size of window
bt_img = Image.open("Tokens/Black_Token.png") #gets the black token png file. 

bt_img = bt_img.resize((50,50), Image.ANTIALIAS) #resizes the token to be a little smaller. 

black_token = ImageTk.PhotoImage(bt_img) #sets the black token to be actually used in the program


#this section does the same just for a red token.
rt_img = Image.open("Tokens/Red_Token.png")
rt_img = rt_img.resize((50, 50), Image.ANTIALIAS)
red_token = ImageTk.PhotoImage(rt_img)

ph_img = Image.open("Tokens/Gray_PlaceHolder.png")
ph_img = ph_img.resize((30,30), Image.ANTIALIAS)
placeholder_token = ImageTk.PhotoImage(ph_img)
 ###########################


play = tkinter.Button(root, text="Play", command=play_pressed) #connects the play button to the play pressed event
play.place(relx = 0.5, rely= 0.5, anchor=CENTER)#places the play button in the middle. 


root.mainloop() #runs the tkinter loop


#noticable bugs to fix later. 

#1. The "tokens" can be placed one more time than needed, in over words overflowing. 
#2. the colors seem a little weird. 

  

  





