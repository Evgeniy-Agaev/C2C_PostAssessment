####################
#Code2College Post Assessment Assignment
#Start Date: Nov 4th, 2022
#End Date: 
#Name: Evgeniy Agaev
#Project Description: Working Connect 4 Game using tkinter gui framework.  
####################


# import tkinter as tk

# window = tk.Tk()
# window.title("Hello wold")
# window.geometry("300x300")




# tk.mainloop()

def print_gameboard():
  for row in gameboard:
    print(row)

def drop_piece(gameboard, collumn, player_token):
  for row in range(0, height):
    if(gameboard[row][collumn] != '-'):
      gameboard[row -1][collumn] = player_token
      return gameboard
    

  gameboard[height -1][collumn] = player_token
  return gameboard
  
  



gameboard = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]
gameboard_size = width, height = len(gameboard), len(gameboard[0])


print("Hello this is a Connect 4 Game!")
print("You are player X, while the computer is player Y")



