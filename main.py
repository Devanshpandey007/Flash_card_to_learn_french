from tkinter import *
import pandas as pd
from random import choice,randint

BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
canv = Canvas(height=600,width=800,bg=BACKGROUND_COLOR,highlightthickness=0)
canv.pack()

word_file = pd.read_csv("data/flash_card_data.csv")
rand_num = 0
x = 0
def random_numb():
    global rand_num,x
    rand_num = randint(2,3001)
    x =rand_num

word = word_file["French"][rand_num]
word1 = word_file["English"][x]
img = PhotoImage(file="images/card_front.png")
img2 = PhotoImage(file="images/card_back.png")
c_box = canv.create_image(405,270,image=img)
head=canv.create_text(400,50,text="French",font=("Arial",40,"italic"))
content =canv.create_text(400,200,text = word,font=("Arial",40))
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
def if_wrong():
    canv.itemconfig(c_box, image=img)
    canv.itemconfig(head, text="French")
    random_numb()
    word = word_file["French"][rand_num]
    canv.itemconfig(content, text=word)
def if_correct():
    canv.itemconfig(c_box,image = img2)
    canv.itemconfig(head,text="English")
    word1 = word_file["English"][x]
    canv.itemconfig(content,text=word1)

cross_button = Button(image=wrong_img,command=if_wrong)
cross_button.place(x=100,y=530)
check_img = Button(image=right_img,command=if_correct)
check_img.place(x=600,y=530)
mainloop()




