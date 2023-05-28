from tkinter import *
from PIL import Image, ImageTk
from random import randint
import customtkinter 

def show_window ():

    # main window
    root = Tk()
    root.title("Rock Paper Scissor")

    app = customtkinter.CTk()
    # app.title("Rock Paper Scissor")
    # app.geometry("400x150")

    root.configure(background="#9b59b6")

    #pictures to add

    rock_img_user = ImageTk.PhotoImage(Image.open("user_rock.PNG"))
    paper_img_user = ImageTk.PhotoImage(Image.open("user_paper.PNG"))
    scissor_img_user = ImageTk.PhotoImage(Image.open("user_scissor.PNG"))

    rock_img_com = ImageTk.PhotoImage(Image.open("com_rock.PNG"))
    paper_img_com = ImageTk.PhotoImage(Image.open("com_paper.PNG"))
    scissor_img_com = ImageTk.PhotoImage(Image.open("com_scissor.PNG"))

    # insert pictures
    user_label = Label(root,image=rock_img_user,bg="#9b59b6")
    com_label = Label(root,image=rock_img_com,bg="#9b59b6")

    com_label.grid(row=1,column=0)
    user_label.grid(row=1,column=4)

    #scores
    playerScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white") 
    comScore = Label(root,text=0,font=100,bg="#9b59b6",fg="white") 

    comScore.grid(row=1,column=1)
    playerScore.grid(row=1,column=3)

    #indicators
    user_indicator = Label(root,font=50,text="USER",bg="#9b59b6",fg="white")
    com_indicator = Label(root,font=50,text="COMPUTER",bg="#9b59b6",fg="white")

    user_indicator.grid(row=0,column=4)
    com_indicator.grid(row=0,column=0)


    # Update the choices
    choices = ["rock","paper","scissor"]

    def update_Choices(x):
        # for computer 
        com_choice = choices[randint(0,2)]
        if com_choice == "rock":
            com_label.configure(image=rock_img_com)
        elif x == "paper":
            com_label.configure(image=paper_img_com)
        else:
            com_label.configure(image=scissor_img_com)

        # for user
        if x=="rock":
            user_label.configure(image=rock_img_user)
        elif x == "paper":
            user_label.configure(image=paper_img_user)
        else:
            user_label.configure(image=scissor_img_user)
        
        check_Winner(x,com_choice)
        
    # Messages
    msg = Label(root,font=50,bg="#9b59b6",fg="white")
    msg.grid(row=3,column=2)

    # Update Messages
    def update_Messages(x):
        msg['text'] = x

    # Update User Score
    def update_User_Score():
        score = int(playerScore["text"])
        score+=1
        playerScore["text"] = str(score) 

    # Update Computer Score
    def update_Computer_Score():
        score = int(comScore["text"])
        score+=1
        comScore["text"] = str(score) 

    # Check Winner
    def check_Winner(user,comp):
        if user==comp:
            update_Messages("Its a Tie ^_^")

        elif user == "rock":
            if comp == "paper":
                update_Messages("Computer win!")
                update_Computer_Score()
            else :
                update_Messages("You win!")
                update_User_Score()

        elif user == "paper":
            if comp == "rock":
                update_Messages("You win!")
                update_User_Score()
            else :
                update_Messages("Computer win!")
                update_Computer_Score()
            
        elif user == "scissor":
            if comp == "rock":
                update_Messages("Computer win!")
                update_Computer_Score()
            else :
                update_Messages("You win!")
                update_User_Score()
            
        else:
                pass


    # Buttons
    # customtkinter.CTkButton(app, text="my button", command=button_callback)
    # ,bg="#0ABDE3",fg="white"
    # ,command= lambda:update_Choices("rock")
    rock =   customtkinter.CTkButton(app,width=20,height=2,text="Rock").grid(row=2,column=1,padx=20, pady=20)
    # rock.pack()
    # paper = customtkinter.CTkButton(app,width=20,height=2,text="Paper",bg="#FF3E4D",fg="white",command= lambda:update_Choices("paper")).grid(row=2,column=2)
    # scissor = customtkinter.CTkButton(app,width=20,height=2,text="Scissor",bg="#FAD02E",fg="white",command= lambda:update_Choices("scissor")).grid(row=2,column=3)

    root.mainloop()

show_window()