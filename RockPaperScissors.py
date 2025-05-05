import random
from tkinter import Tk, Label, Button, Canvas,Entry,Toplevel
from PIL import Image, ImageTk

#Players images path specified
path_ppru = r"C:\Users\MASTER\OneDrive - Jeevay Software Solutions\Desktop\New folder\paperu.png"
path_rocku = r"C:\Users\MASTER\OneDrive - Jeevay Software Solutions\Desktop\New folder\rocked.png"
path_scissoru = r"C:\Users\MASTER\OneDrive - Jeevay Software Solutions\Desktop\New folder\scissor.png"
#computer images path specified


path_gamerule = r"C:\Users\MASTER\OneDrive - Jeevay Software Solutions\Desktop\New folder\Gamerule.png"



class RPSGame(Tk):
    def __init__(self, wtitle):
        super().__init__()
        self.title(wtitle)
        # Variables to store images
        self.image_on_canvas_user = None
        self.image_on_canvas_comp = None
        self.player_count=0
        self.comp_count=0
       # self.geometry("800x680")
        self.create_widgets()

    def create_widgets(self):
        self.canvas2=Canvas(self,width=1300,height=100,bd=2,bg="#001F3F")
        self.canvas2.pack()
        self.canvas = Canvas(self, width=1300, height=680 ,bd=2 , bg='white')
        self.canvas.pack()
        self.label1=Label(self.canvas2,text="ROCK\nPAPER\nSCISSORS\nGAME",font=("Lucida Console",12,"bold"),fg="white",bg="#000080")
        self.label1.place(x=200,y=20)
        self.label1=Label(self.canvas2,text="|\n|\n|\n|",font=("Cinzel",12,"bold"),fg="white",bg="#000080")
        self.label1.place(x=300,y=20)
        self.label2=Label(self.canvas2,text="PLAYER:",font=("Lucida Handwriting",15,"bold"),fg="white",bg="black")
        self.label2.place(x=400,y=20)
        self.entrybox1=Entry(self.canvas2,state="disabled",font=("Helvetica",20),fg="red")
        self.entrybox1.place(x=600,y=20)
        self.entrybox2=Entry(self.canvas2,state="disabled",font=("Helvetica",20),fg="red")
        self.entrybox2.place(x=600,y=70)
        self.label2=Label(self.canvas2,text="Computer:",font=("Lucida Handwriting",15,"bold"),fg="white",bg="black")
        self.label2.place(x=400,y=70)
        self.l1=Label(self,text="Player",font=("Courier",25,"bold"),fg="black")
        self.l2=Label(self,text="Computer",font=("Courier",25,"bold"),fg="black")
        self.l3=Label(self,text="Vs",font=("Courier",40,"bold"),fg="black")
        self.l1.place(x=100,y=150)
        self.l2.place(x=980,y=150)
        self.l3.place(x=580,y=350)
        # Buttons to call rock, paper, and scissor images
        self.rock_b = Button(self, text='ROCK', command=lambda: self.determine_winner(random.randint(1, 3), 2) , font=('Times' , 10 , 'bold'), padx=7, pady=5 , fg='White', bg='Navy' ,activebackground="white",activeforeground='Navy', bd=3)
        self.rock_b.place(x=35, y=570)
        self.paper_b = Button(self, text='PAPER', command=lambda: self.determine_winner(random.randint(1, 3), 1) ,font=('Times' , 10 , 'bold'), padx=7, pady=5 , fg='white', bg='Navy' ,activebackground="white",activeforeground='Navy', bd=3)
        self.paper_b.place(x=140, y=570)
        self.scissor_b = Button(self, text='SCISSOR', command=lambda: self.determine_winner(random.randint(1, 3), 3), font=('Times' , 10 , 'bold'), padx=7, pady=5, fg='white', bg='Navy' ,activebackground="white",activeforeground='Navy', bd=3)
        self.scissor_b.place(x=250, y=570)
        self.reset_b=Button(self.canvas2,text="RESET",command=self.reset_game,font=("Times",10,"bold"),padx=10,pady=5,bg="Navy",fg="White"  , activebackground="white",activeforeground='Navy',bd=3)
        self.reset_b.place(x=1050,y=50)
        self.rules_b = Button(self,text="RULES", command= self.open_rules, font=("Times", 10, "bold"), padx=10, pady=5, bg="Navy", fg="White", activebackground="white",activeforeground='Navy', bd=3)
        self.rules_b.place(x=1150, y=50)

    def open_rules(self):
        rules_window = Toplevel(self)
        rules_window.title("Game Rules")
        rules_window.geometry("600x400") 

        img = Image.open(path_gamerule)
        img = img.resize((600,400))
        rules_image = ImageTk.PhotoImage(img)
        self.image_on_canvas_user=rules_image

        rules_label = Label(rules_window, image=rules_image)
        rules_label.pack()
                 
    def create_image(self, filename, x, y):
        img = Image.open(filename)
        img = img.resize((400, 350))
        return ImageTk.PhotoImage(img)

    def create_user_images(self, player):
        
        if player == 1:
            self.image_on_canvas_user = self.create_image(path_ppru, 500, 350)
        elif player == 2:
            self.image_on_canvas_user = self.create_image(path_rocku, 500, 350)
        else:
            self.image_on_canvas_user = self.create_image(path_scissoru,500, 350)
        self.canvas.create_image(5, 100,anchor="nw",image=self.image_on_canvas_user)

    def create_comp_images(self, computer):
        if computer == 1:
            self.image_on_canvas_comp = self.create_image(path_ppru, 1000, 100)
        elif computer == 2:
            self.image_on_canvas_comp = self.create_image(path_rocku, 1000, 100)
        else:
            self.image_on_canvas_comp = self.create_image(path_scissoru, 1000, 100)
        self.canvas.create_image(1050, 270, image=self.image_on_canvas_comp)

    def determine_winner(self, computer, player):
        player_score,comp_score=self.count_num(player,computer) 
        #Enable the entryboxes
        self.entrybox1.config(state="normal")
        self.entrybox2.config(state="normal")
        self.entrybox1.delete(0,'end')
        self.entrybox2.delete(0,'end')
        self.entrybox1.insert(0,str(player_score))
        self.entrybox2.insert(0,str(comp_score))
        #Disabling the entryboxes
        self.entrybox1.config(state="disabled")
        self.entrybox2.config(state="disabled")
        
        self.canvas.delete('result')  # Clear previous result text

        self.create_comp_images(computer)
        
        
        self.create_user_images(player)

        if player == computer:
            result = 'Draw'
        elif (player == 2 and computer == 3) or \
             (player == 1 and computer == 2) or \
             (player == 3 and computer == 1):
            result = 'Player wins!'
        else:
            result = 'Computer wins!'

        self.after(1000, self.display_result(result)) 
        
    def display_result(self, result):
        self.canvas.delete('result')  # Clear previous result text
        self.canvas.create_text(650, 450, text='Result: ' + result,
                           fill="white", font=('Times', 25,"bold"), tag='result')
    
    def count_num(self,player,computer):
        while True:
            if player==computer:
                return self.player_count,self.comp_count
            elif(player==2 and computer==3) or  (player==1 and computer==2) or (player==3 and computer==1):
                self.player_count+=1
            elif(player==3 and computer==2) or  (player==2 and computer==1) or (player==1 and computer==3):
                self.comp_count+=1
            else:
                break
            return self.player_count,self.comp_count
    
    def reset_game(self):
        #Reset the counts
        self.player_count=0
        self.comp_count=0
        #Enable the Entryboxes
        self.entrybox1.config(state="normal")
        self.entrybox2.config(state="normal")
        #Clear the Entryboxes
        self.entrybox1.delete(0,'end')
        self.entrybox2.delete(0,'end')
        #Disable the Entryboxes
        self.entrybox1.config(state="disabled")
        self.entrybox2.config(state="disabled")
        #Clear the canvas
        self.canvas.delete("all")
        #Reset the images
        
        self.image_on_canvas_user=None
        self.image_on_canvas_comp=None



def main():
    r = RPSGame("Rock Paper Scissors")
    r.mainloop()

main() 
