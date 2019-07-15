from tkinter import*
import random
import time
import datetime


root=Tk()
root.geometry("1350x750+0+0")
root.title("Cafe Billing System")
root.configure(background='black')

Tops = Frame(root,width =1350, height = 100, bd=14,relief="raise")
Tops.pack(side=TOP)
Tops.configure(background='black')
label = Label(Tops, font=('arial',70,'bold'),text="Cafe Billing System",bd =10)
label.grid(row=0,column=0)

left_frame = Frame(root,width =900, height = 650, bd=8,relief="raise")
left_frame.pack(side=LEFT)
left_frame.configure(background='black')

right_frame = Frame(root,width =440, height = 650, bd=8,relief="raise")
right_frame.pack(side=RIGHT)
right_frame.configure(background='black')

left_frameChild = Frame(left_frame,width = 900, height = 330, bd=8,relief="raise")
left_frameChild.pack(side=TOP)

left_frameChild2 = Frame(left_frame,width = 900, height = 320, bd=8,relief="raise")
left_frameChild2.pack(side=BOTTOM)


right_frameChild = Frame(right_frame,width = 440, height = 650, bd=12,relief="raise")
right_frameChild.pack(side=TOP)

right_frameChild2 = Frame(right_frame,width = 440, height = 50, bd=16,relief="raise")
right_frameChild2.pack(side=BOTTOM)

#########
left_frame_G_Child = Frame(left_frameChild,width = 400, height = 330, bd=16,relief="raise")
left_frame_G_Child.pack(side=LEFT)

left_frame_G_Child2 = Frame(left_frameChild,width = 400, height = 330, bd=16,relief="raise")
left_frame_G_Child2.pack(side=RIGHT)


right_frame_G_Child = Frame(left_frameChild2,width = 450, height = 330, bd=14,relief="raise")
right_frame_G_Child.pack(side=LEFT)

right_frame_G_Child2 = Frame(left_frameChild2,width = 450, height = 330, bd=14,relief="raise")
right_frame_G_Child2.pack(side=RIGHT)

root.mainloop()
