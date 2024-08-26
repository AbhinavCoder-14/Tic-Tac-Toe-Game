from tkinter import *
import tkinter.messagebox as msg


def intro():
    global count, text, newText, Intro
    if count >= len(text):
        # count = -1
        newText = ''
        Intro.config(text=text[:count:])
        Intro.pack(side=TOP)

    else:
        newText = newText + text[count]
        Intro.config(text=newText)
        Intro.pack(side='top', pady=10)
    count += 1
    Intro.after(200, intro)


main = Tk()
main.title('tic tac Toc')
Intro = Label(main, text='', font='arial 30 bold')
main.geometry('810x550')

count = 0
newText = ''
text = 'Welcome To Tic Tac Toc Game'
intro()
barLabel = Label(main, text='---------------------------------------------------------------------------------------------------------------------------------------')
barLabel.pack(side=TOP)

Value = True
Erase1 = False
Erase2 = False
Erase3 = False
Erase4 = False
Erase5 = False
Erase6 = False
Erase7 = False
Erase8 = False
Erase9 = False


def detecter(button):
    global Value
    if button['text'] == ' ' and Value == True:
        button['text'] = 'X'
        Value = False
        MainLogic()
    elif button['text'] == ' ' and Value == False:
        button['text'] = '0'
        Value = True
        MainLogic1()


def Resat():
    global Value
    # PlayerY.set(0)
    # PlayerX.set(0)
    Value = True
    B1['text'] = ' '
    B2['text'] = ' '
    B3['text'] = ' '
    B4['text'] = ' '
    B5['text'] = ' '
    B6['text'] = ' '
    B7['text'] = ' '
    B8['text'] = ' '
    B9['text'] = ' '

    B1.config(bg='white')
    B2.config(bg='white')
    B3.config(bg='white')
    B4.config(bg='white')
    B5.config(bg='white')
    B6.config(bg='white')
    B7.config(bg='white')
    B8.config(bg='white')
    B9.config(bg='white')


def Newgame():
    global Value
    Value = True
    B1['text'] = ' '
    B2['text'] = ' '
    B3['text'] = ' '
    B4['text'] = ' '
    B5['text'] = ' '
    B6['text'] = ' '
    B7['text'] = ' '
    B8['text'] = ' '
    B9['text'] = ' '
    PlayerX.set(0)
    PlayerY.set(0)
    B1.config(bg='white')
    B2.config(bg='white')
    B3.config(bg='white')
    B4.config(bg='white')
    B5.config(bg='white')
    B6.config(bg='white')
    B7.config(bg='white')
    B8.config(bg='white')
    B9.config(bg='white')


def MainLogic():

    if B1['text'] == 'X' and B2['text'] == 'X' and B3['text'] == 'X':
        Erase1 = True
        B1.config(bg='skyblue')
        B2.config(bg='skyblue')
        B3.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B4['text'] == 'X' and B5['text'] == 'X' and B6['text'] == 'X':
        Erase2 = False
        B4.config(bg='skyblue')
        B5.config(bg='skyblue')
        B6.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B7['text'] == 'X' and B8['text'] == 'X' and B9['text'] == 'X':
        Erase3 = False
        B7.config(bg='skyblue')
        B8.config(bg='skyblue')
        B9.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B1['text'] == 'X' and B4['text'] == 'X' and B7['text'] == 'X':
        Erase4 = False
        B4.config(bg='skyblue')
        B7.config(bg='skyblue')
        B4.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B2['text'] == 'X' and B5['text'] == 'X' and B8['text'] == 'X':
        Erase5 = False
        B5.config(bg='skyblue')
        B2.config(bg='skyblue')
        B8.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B3['text'] == 'X' and B6['text'] == 'X' and B9['text'] == 'X':
        Erase6 = True
        B6.config(bg='skyblue')
        B9.config(bg='skyblue')
        B3.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B1['text'] == 'X' and B5['text'] == 'X' and B9['text'] == 'X':
        Erase7 = False
        B1.config(bg='skyblue')
        B5.config(bg='skyblue')
        B9.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')

    elif B3['text'] == 'X' and B5['text'] == 'X' and B7['text'] == 'X':
        Erase8 = False
        B3.config(bg='skyblue')
        B5.config(bg='skyblue')
        B7.config(bg='skyblue')
        Score_X = PlayerX.get()
        Score_X += 1
        PlayerX.set(Score_X)
        msg.showinfo('info', f'player - X {Score_X}')


# ----------------------------------------------------------------- O Time :--

def MainLogic1():

    if B1['text'] == '0' and B2['text'] == '0' and B3['text'] == '0':
        B1.config(bg='blue')
        B2.config(bg='blue')
        B3.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B4['text'] == '0' and B5['text'] == '0' and B6['text'] == '0':
        B4.config(bg='blue')
        B5.config(bg='blue')
        B6.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B7['text'] == '0' and B8['text'] == '0' and B9['text'] == '0':
        B7.config(bg='blue')
        B8.config(bg='blue')
        B9.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B1['text'] == '0' and B4['text'] == '0' and B7['text'] == '0':
        B1.config(bg='blue')
        B4.config(bg='blue')
        B7.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B2['text'] == '0' and B5['text'] == '0' and B8['text'] == '0':
        B2.config(bg='blue')
        B5.config(bg='blue')
        B8.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B3['text'] == '0' and B6['text'] == '0' and B9['text'] == '0':
        B3.config(bg='blue')
        B6.config(bg='blue')
        B9.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B1['text'] == '0' and B5['text'] == '0' and B9['text'] == '0':
        B1.config(bg='blue')
        B5.config(bg='blue')
        B9.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')

    elif B3['text'] == '0' and B5['text'] == '0' and B7['text'] == '0':
        B3.config(bg='blue')
        B5.config(bg='blue')
        B7.config(bg='blue')
        Score_O = PlayerY.get()
        Score_O += 1
        PlayerY.set(Score_O)
        msg.showinfo('info', f'player - O {Score_O}')


'''
B1,B2,B3
B4,B5,B6
B7,B8,B9
1,5,9
3,5,7
1,4,7
2,5,8
3,6,9
'''

Mainframe1 = Frame(main, width=5, bg='black', borderwidth=7)
Mainframe1.pack(side=TOP, anchor='n', pady=10, fill='x')

GameFrame = Frame(Mainframe1, bg='grey', borderwidth=6, width=6)
GameFrame.pack(side=LEFT, anchor='n', pady=10, padx=20)

B1 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B1))
B1.grid(row=1, column=1)

B2 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B2))
# B2.pack(side='left',anchor='nw')
B2.grid(row=1, column=2)

B3 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B3))
# B3.pack(side=RIGHT,anchor='ne')
B3.grid(row=1, column=3)

B4 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B4))
B4.grid(row=2, column=1)

B5 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B5))
B5.grid(row=2, column=2)

B6 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B6))
B6.grid(row=2, column=3)

B7 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B7))
B7.grid(row=3, column=1)

B8 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B8))
B8.grid(row=3, column=2)

B9 = Button(GameFrame, text=' ', width=20, height=7, borderwidth=5,
            font='Arial 9 bold', command=lambda: detecter(B9))
B9.grid(row=3, column=3)


Info_Frame = Frame(Mainframe1, bg='grey', borderwidth=7)
Info_Frame.pack(side=RIGHT, padx=10, pady=20, anchor='n')

Info_Frame1 = Frame(Info_Frame, bg='black', borderwidth=5)
Info_Frame1.grid(row=1, column=1)


Player_X_Label = Label(
    Info_Frame1, text='Player (X) - 1 :', font='arial 14 bold')
Player_X_Label.grid(row=1, column=1)

Player_Y_Label = Label(
    Info_Frame1, text='Player (O) - 2 :', font='arial 14 bold')
Player_Y_Label.grid(row=2, column=1)
PlayerX = IntVar()
PlayerX.set(0)
Player_X_Entry = Entry(Info_Frame1, font='arial 13 bold',
                       textvariable=PlayerX, width=4, justify=LEFT)
Player_X_Entry.grid(row=1, column=2)
PlayerY = IntVar()
PlayerY.set(0)

Player_Y_Entry = Entry(Info_Frame1, font='arial 13 bold',
                       textvariable=PlayerY, width=4, justify=LEFT)
Player_Y_Entry.grid(row=2, column=2)

ResetButton = Button(Info_Frame1, text='Reset', borderwidth=4,
                     font='Arial 14 bold', width=13, command=Resat)
ResetButton.grid(row=3, column=1, pady=20, columnspan=2)

NewGameButton = Button(Info_Frame1, text='New Game', borderwidth=4,
                       font='arial 14 bold', width=13, command=Newgame)
NewGameButton.grid(row=4, column=1, columnspan=2)

MainLogic()

main.mainloop()

# iron - grey
# copper = Blue
# iron = ?
