from tkinter import *
from tkinter import messagebox
turn = 0
board = [['', '', ''], ['', '', ''], ['', '', '']]

#Whenever the user selects the quit option, this message is displayed
def Quit():
    global root

    msg = messagebox.askquestion("Quit?????")
    if msg == "yes":
        root.destroy()

#Break the winner window and game window
def breakWin():
    global winnerWindow

    winnerWindow.destroy()

#replay button
def replay():
    global board, root, turn
    root.destroy()
    turn = 0
	#Reset board
    board = [['', '', ''],
        ['', '', ''],
        ['', '', '']]
    TicTacToeGUI()

#Displays the winning condition
def displayWinner(winner):
    global root, winnerWindow, ID
	
    winnerWindow = Tk()
    winnerWindow.title("Winner Window")
    winnerWindow.configure(bg="Black")
    l1 = Label(winnerWindow, text="THE WINNER IS: ", font=("COMIC SANS MS",15),bg="Black",fg="White")
    l1.pack()
    l2 = Label(winnerWindow,text=winner,font=("COMIC SANS MS",15),bg="Black",fg="White")
    l2.pack()
    bBack = Button(winnerWindow,text="Back",font=("COMIC SANS MS",10,"bold"),command=breakWin)
    bBack.pack()

#Checks for the winner        
def checkWinner():
    global turn, board

	#check all X case
    if ((board[0][0] == board[0][1] == board[0][2] == "X") or 
	(board[1][0] == board[1][1] == board[1][2] == "X") or 
	(board[2][0] == board[2][1] == board[2][2] == "X") or
    (board[0][0] == board[1][0] == board[2][0] == "X") or 
	(board[0][1] == board[1][1] == board[2][1] == "X") or 
	(board[0][2] == board[1][2] == board[2][2] == "X") or
    (board[0][0] == board[1][1] == board[2][2] == "X") or 
	(board[0][2] == board[1][1] == board[2][0] == "X")):
        displayWinner("Player X")

	#check all O case
    elif ((board[0][0] == board[0][1] == board[0][2] == "O") or 
	(board[1][0] == board[1][1] == board[1][2] == "O") or 
	(board[2][0] == board[2][1] == board[2][2] == "O") or
    (board[0][0] == board[1][0] == board[2][0] == "O") or 
	(board[0][1] == board[1][1] == board[2][1] == "O") or 
	(board[0][2] == board[1][2] == board[2][2] == "O") or
    (board[0][0] == board[1][1] == board[2][2] == "O") or 
	(board[0][2] == board[1][1] == board[2][0] == "O")):
        displayWinner("Player O")

	#Tie case
    elif turn == 9:
        displayWinner("NONE! IT IS A TIE!")

#Changes the value of the button
def changeVal(button,boardValRow,boardValCol):
    global turn

    #Checking if button is available
    if button["text"] == "":
        if (turn%2) == 0:
            button["text"] = "X"
            l1 = Label(root,text="PLAYER2 : (O)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol] = "X"
        else:
            button["text"] = "O"
            l1 = Label(root,text="PLAYER1 : (X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white").grid(row=0,column=0)
            board[boardValRow][boardValCol] = "O"

        turn = turn+1

		#Start checking a winner while turn is more than 4
        if turn > 4:
            checkWinner()
    else:
        messagebox.showerror("Error","This box already has a value!")

#Displays the GUI 
def TicTacToeGUI():
    global root

    root = Tk()
    root.title("TIC TAC TOE")
    root.configure(bg="white")  #Making the background of the window as white

    #Displaying the player
    l1 = Label(root,text="PLAYER1 : (X)",height=3,font=("COMIC SANS MS",10,"bold"),bg="white")
    l1.grid(row=0,column=0)

    #Replay button
    replayButton = Button(root,text="Replay",command=replay,font=("COMIC SANS MS",10,"bold"))
    replayButton.grid(row=0,column=1)


    #Quit button
    exitButton = Button(root,text="Quit",command=Quit,font=("COMIC SANS MS",10,"bold"))
    exitButton.grid(row=0,column=2)

    
    #Grid buttons 3x3
    b1 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b1,0,0))
    b2 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b2,0,1))
    b3 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b3,0,2))
    b4 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b4,1,0))
    b5 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b5,1,1))
    b6 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b6,1,2))
    b7 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b7,2,0))
    b8 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b8,2,1))
    b9 = Button(root,text="",height=4,width=8,bg="black",activebackground="white",fg="black",font="Times 15 bold",command=lambda: changeVal(b9,2,2))

    b1.grid(row=2,column=0)
    b2.grid(row=2,column=1)
    b3.grid(row=2,column=2)

    b4.grid(row=3,column=0)
    b5.grid(row=3,column=1)
    b6.grid(row=3,column=2)

    b7.grid(row=4,column=0)
    b8.grid(row=4,column=1)
    b9.grid(row=4,column=2)

    backButton = Button(root,text="Main Menu",command=backMenu,font=("COMIC SANS MS",12,"bold"))
    backButton.grid(row=5,column=1)

#Back to main menu
def backMenu():
	global root

	root.destroy()
	homepage()

#Display homepage
def homepage():
	global root

	root = Tk()
	root.title("Main Menu")
	l = Label(root, text="Welcome to my TICTACTOE game", height=1, font=("COMIC SANS MS", 18, "bold"), bg="white")
	l.grid(row=0, column=0)

	#Make Choice
	c1 = Button(root,text="Play",command=replay,font=("COMIC SANS MS",18,"bold"))
	c1.grid(row=1,column=0)
	c3 = Button(root,text="Quit",command=Quit,font=("COMIC SANS MS",18,"bold"))
	c3.grid(row=3,column=0)

homepage()
root.mainloop()
