import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Initialize the game board
root = tk.Tk()
root.title("Tic Tac Toe")
# Create a label for instructions
instructions_label = tk.Label(root, text="Welcome to \n Tic Tac Toe!\n\nINSTRUCTIONS\n\nchoose one of the move from the given moves\n ROCK as R\n PAPPER as P\n SCISSOR as S\n\nEnter your move and Click on 'OK' to start the game",font=("Arial", 14))
instructions_label.pack()
# Function to handle the "OK" button click
def start_game():
 import random
 C=('R','P','S')
 #A=input('choose one of the move from the given moves\n ROCK as R\n PAPPER as P\n SCISSOR as S\nENTER HERE :')
 A=entry.get()
 print("Your's: ",A)
 B=random.choice(C)
 if ((A=='R'and B=='S') or (A=='S'and B=='R')):
     print("computer's: ",B)
     if A=='R':
         print('You are the winner')
     else:
         print('computer is the winner')
 elif ((A=='P'and B=='R') or (A=='R'and B=='P')):
     print("computer's: ",B)
     if A=='P':
         print('You are the winner')
     else:
         print(' computer is winner')
 elif ((A=='S'and B=='P') or (A=='P'and B=='S')):
     print("computer's: ",B)
     if A=='S':
         print('You are the winner')
     else:
         print(' computer is winner')
 elif (A==B):
     print("computer's: ",B)
     print("It's a Tie")
 else:
     print("computer's: ",B)
     print('computer is winner')
 print("Do you want to play agin !!!\n**PLEASE CLICK ON 'CLEAR ENTRY' BUTTON TO CLEAR THE ENRTY** \n**NOW CLICK  ON 'OK' TO START**")

#label
label=tk.Label(root,text="Enter Your Move",font=("Arial", 25)).pack()
#entry box
entry=tk.Entry(root,width=20)
entry.pack()
# Create an "OK" button
ok_button = tk.Button(root, text="OK",command=start_game,font=("Arial", 25))
ok_button.pack()
#create a button to clear entry box
clear_button=tk.Button(root,text="CLEAR ENTRY",font=("Arial", 25))
clear_button.pack()
clear_button.config(command=lambda: entry.delete(0,tk.END))






