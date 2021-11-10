from tkinter import *

#main root/frame
root = Tk()
root.title("Food Choice Randomizer ")
root.geometry("350x300")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

#function

import random


breakfast = ["Cereal","Pancakes","PB Toast","Fruit","Oatmeal","Protein Shake","Waffles" ]
lunch = ["PB and j" , "Ramen" , "Pasta","Salad","Sanwich","Rice" ,"Rice Cake"]
dinner = ["Burger" , "Chicken Strips" , "Pizza", "Chinese" , "Fruit bowl" ,"Chicken & Rice"]


def call():
    text_val = e.get()    print(text_val)
    if text_val == "breakfast":
        print(random.choice(breakfast))
    elif text_val == "lunch":
        print(random.choice(lunch))
    elif text_val == "dinner":
        print(random.choice(dinner))
    else:
        print("nothing")
#buttons and widgets

button = Button(bottomFrame, text="Randomize!",command='call')
button.pack(pady=20)
button.config(command=call)

#button2 = Button(bottomFrame,text="randomize!",command=)
#button2.pack()



e = Entry(root, width = 40,)
e.insert(0," ")
e.pack()



#text
label= Label(root,text = "breakfast , lunch or dinner?", font="times 13")
label.pack()

#messagebox.showinfo("choice","your choice is: %s" % (call))
root.mainloop()
