from tkinter import*
from tkinter import messagebox 
import random
import time
import datetime


root=Tk()
root.geometry("1070x750+0+0")
root.title("Cafe Billing System")
root.configure(background='grey')

Tops = Frame(root,width =1350, height = 100, bd=10,relief="raise")
Tops.pack(side=TOP)

Tops.configure(background='grey')
label = Label(Tops,font=('arial',50,'bold'),text="       Cafe  Billing  System       ",bd =8)
label.grid(row=0,column=0)

left_frame = Frame(root,width =900, height = 650, bd=8,relief="raise")
left_frame.pack(side=LEFT)
left_frame.configure(background='grey')

right_frame = Frame(root,width =440, height = 650, bd=8,relief="raise")
right_frame.pack(side=RIGHT)
right_frame.configure(background='grey')

left_frameChild = Frame(left_frame,width = 440, height = 320, bd=8,relief="raise")
left_frameChild.pack(side=TOP)

left_frameChild2 = Frame(left_frame,width = 440, height = 320, bd=8,relief="raise")
left_frameChild2.pack(side=BOTTOM)


right_frameChild = Frame(right_frame,width = 440, height = 500, bd=8,relief="raise")
right_frameChild.pack(side=TOP)

right_frameChild2 = Frame(right_frame,width = 440, height = 100, bd=8,relief="raise")
right_frameChild2.pack(side=BOTTOM)

#########
left_frame_G_Child = Frame(left_frameChild,width = 440, height = 320, bd=8,relief="raise")
left_frame_G_Child.pack(side=LEFT)

left_frame_G_Child2 = Frame(left_frameChild,width = 440, height = 320, bd=8,relief="raise")
left_frame_G_Child2.pack(side=RIGHT)


left_frame_G_Child3 = Frame(left_frameChild2,width = 440, height = 320, bd=8,relief="raise")
left_frame_G_Child3.pack(side=LEFT)

left_frame_G_Child4 = Frame(left_frameChild2,width = 440, height = 320, bd=8,relief="raise")
left_frame_G_Child4.pack(side=RIGHT)

#=========variables for items==============
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()

coffeeVar1 = StringVar()
coffeeVar2 = StringVar()
coffeeVar3 = StringVar()
coffeeVar4 = StringVar()
coffeeVar5 = StringVar()
coffeeVar6 = StringVar()
coffeeVar7 = StringVar()
coffeeVar8 = StringVar()

foodVar9 = StringVar()
foodVar10 = StringVar()
foodVar11 = StringVar()
foodVar12 = StringVar()
foodVar13 = StringVar()
foodVar14 = StringVar()
foodVar15 = StringVar()
foodVar16 = StringVar()


net_price = IntVar()
paidVat = IntVar()
total = IntVar()
paid =IntVar()
discount = IntVar()
return_taka = IntVar()
txtReceipt = StringVar()
DateofOrder = StringVar()

def exit():
	qExit = messagebox.askyesno("Quit", "Are you sure?")
	if qExit > 0:
		root.destroy()
		return

def reset():
        var1.set("0")
        var2.set("0")
        var3.set("0")
        var4.set("0")
        var5.set("0")
        var6.set("0")
        var7.set("0")
        var8.set("0")
        var9.set("0")
        var10.set("0")
        var11.set("0")
        var12.set("0")
        var13.set("0")
        var14.set("0")
        var15.set("0")
        var16.set("0")

        #var17 = IntVar()
        #var17.set("0")

        #var18 = IntVar()
        #var18.set("0")

        #var19 = IntVar()
        #var19.set("0")

        #var20 = IntVar()
        #var20.set("0")

        coffeeVar1.set("0")
        coffeeVar2.set("0")
        coffeeVar3.set("0")
        coffeeVar4.set("0")
        coffeeVar5.set("0")
        coffeeVar6.set("0")
        coffeeVar7.set("0")
        coffeeVar8.set("0")
        
        foodVar9.set("0")
        foodVar10.set("0")
        foodVar11.set("0")
        foodVar12.set("0")
        foodVar13.set("0")
        foodVar14.set("0")
        foodVar15.set("0")
        foodVar16.set("0")
        
        net_price.set("0")
        paidVat.set("0")
        total.set("0")
        paid.set("0")
        discount.set("0")
        return_taka.set("0")
        #txtReceipt.delete("1.0",END)
        DateofOrder.set(time.strftime("%d-%m-%Y"))

#============Check Button Funtion ==========
def checkButton():
        if (var1.get() == 1 ):
                txtcoffee1.configure(state = NORMAL)
        elif(var1.get() == 0):
                txtcoffee1.configure(state = DISABLED)
                coffeeVar1.set("0")
                
        if (var2.get() == 1 ):
                txtcoffee2.configure(state = NORMAL)
        elif(var2.get() == 0):
                txtcoffee2.configure(state = DISABLED)
                coffeeVar2.set("0")
                
        if (var3.get() == 1 ):
                txtcoffee3.configure(state = NORMAL)
        elif(var3.get() == 0):
                txtcoffee3.configure(state = DISABLED)
                coffeeVar3.set("0")
                
        if (var4.get() == 1 ):
                txtcoffee4.configure(state = NORMAL)
        elif(var4.get() == 0):
                txtcoffee4.configure(state = DISABLED)
                coffeeVar4.set("0")
                
        if (var5.get() == 1 ):
                txtcoffee5.configure(state = NORMAL)
        elif(var5.get() == 0):
                txtcoffee5.configure(state = DISABLED)
                coffeeVar5.set("0")
                
        if (var6.get() == 1 ):
                txtcoffee6.configure(state = NORMAL)
        elif(var6.get() == 0):
                txtcoffee6.configure(state = DISABLED)
                coffeeVar6.set("0")
                
        if (var7.get() == 1 ):
                txtcoffee7.configure(state = NORMAL)
        elif(var7.get() == 0):
                txtcoffee7.configure(state = DISABLED)
                coffeeVar7.set("0")
                
        if (var8.get() == 1 ):
                txtcoffee8.configure(state = NORMAL)
        elif(var8.get() == 0):
                txtcoffee8.configure(state = DISABLED)
                coffeeVar8.set("0")


        if (var9.get() == 1 ):
                txtfood1.configure(state = NORMAL)
        elif(var9.get() == 0):
                txtfood1.configure(state = DISABLED)
                foodVar9.set("0")
                
        if (var10.get() == 1 ):
                txtfood2.configure(state = NORMAL)
        elif(var10.get() == 0):
                txtfood2.configure(state = DISABLED)
                foodVar10.set("0")
                
        if (var11.get() == 1 ):
                txtfood3.configure(state = NORMAL)
        elif(var11.get() == 0):
                txtfood3.configure(state = DISABLED)
                foodVar11.set("0")
                
        if (var12.get() == 1 ):
                txtfood4.configure(state = NORMAL)
        elif(var12.get() == 0):
                txtfood4.configure(state = DISABLED)
                foodVar12.set("0")
                
        if (var13.get() == 1 ):
                txtfood5.configure(state = NORMAL)
        elif(var13.get() == 0):
                txtfood5.configure(state = DISABLED)
                foodVar13.set("0")
                
        if (var14.get() == 1 ):
                txtfood6.configure(state = NORMAL)
        elif(var14.get() == 0):
                txtfood6.configure(state = DISABLED)
                foodVar14.set("0")
                
        if (var15.get() == 1 ):
                txtfood7.configure(state = NORMAL)
        elif(var15.get() == 0):
                txtfood7.configure(state = DISABLED)
                foodVar15.set("0")
                
        if (var16.get() == 1 ):
                txtfood8.configure(state = NORMAL)
        elif(var16.get() == 0):
                txtfood8.configure(state = DISABLED)
                foodVar16.set("0")

def cost():
        item1 = float(coffeeVar1.get())
        item1 = float(coffeeVar2.get())
        item1 = float(coffeeVar3.get())
        item1 = float(coffeeVar4.get())
        item1 = float(coffeeVar5.get())
        item1 = float(coffeeVar6.get())
        item1 = float(coffeeVar7.get())
        item1 = float(coffeeVar8.get())

        item1 = float(foodVar9.get())
        item1 = float(foodVar10.get())
        item1 = float(foodVar11.get())
        item1 = float(foodVar12.get())
        item1 = float(foodVar13.get())
        item1 = float(foodVar14.get())
        item1 = float(foodVar15.get())
        item1 = float(foodVar16.get())

        
        
        
                
#****************************Desert******************
Coffee1 = Checkbutton(left_frame_G_Child, text="Regular Cold Coffee \t\t ", variable = var1,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=0,column=0,sticky = W)
Coffee2 = Checkbutton(left_frame_G_Child, text="Chocolate Cold Coffee  \t\t", variable = var2,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=1,column=0,sticky = W)
Coffee3 = Checkbutton(left_frame_G_Child, text="Cappuccino \t\t", variable = var3,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=2,column=0,sticky = W)
Coffee4 = Checkbutton(left_frame_G_Child, text="Latta \t\t", variable = var4,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=3,column=0,sticky = W)
Coffee5 = Checkbutton(left_frame_G_Child, text="Blizard \t\t", variable = var5,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=4,column=0,sticky = W)
Coffee6 = Checkbutton(left_frame_G_Child, text="Milk Shake \t\t", variable = var6,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=5,column=0,sticky = W)
Coffee7 = Checkbutton(left_frame_G_Child, text="Mango Shake \t\t", variable = var7,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=6,column=0,sticky = W)
Coffee8 = Checkbutton(left_frame_G_Child, text="Stawberry Shake \t\t", variable = var8,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)
#Coffee9 = Checkbutton(left_frame_G_Child, text="Mango Juice \t\t", variable = var17,
 #                   onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)
#Coffee10 = Checkbutton(left_frame_G_Child, text="Orange Juice \t\t", variable = var18,
 #                   onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)


#****************************FOODS******************
food1 = Checkbutton(left_frame_G_Child2, text="Regular Cold Coffee \t\t", variable = var9,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=0,column=0,sticky = W)
food2 = Checkbutton(left_frame_G_Child2, text="Chocolate Cold Coffee \t\t", variable = var10,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=1,column=0,sticky = W)
food3 = Checkbutton(left_frame_G_Child2, text="Cappiccino \t\t", variable = var11,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=2,column=0,sticky = W)
food4 = Checkbutton(left_frame_G_Child2, text="Latta \t\t", variable = var12,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=3,column=0,sticky = W)
food5 = Checkbutton(left_frame_G_Child2, text="Blizard \t\t", variable = var13,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=4,column=0,sticky = W)
food6 = Checkbutton(left_frame_G_Child2, text="Milk Shake \t\t", variable = var14,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=5,column=0,sticky = W)
food7 = Checkbutton(left_frame_G_Child2, text="Mango Shake \t\t", variable = var15,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=6,column=0,sticky = W)
food8 = Checkbutton(left_frame_G_Child2, text="Stawberry Shake \t\t", variable = var16,
                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)
#food9 = Checkbutton(left_frame_G_Child2, text="Stawberry Shake \t\t", variable = var19,
#                   onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)
#food10 = Checkbutton(left_frame_G_Child2, text="Stawberry Shake \t\t", variable = var20,
#                    onvalue=1,offvalue=0,font=('arial',10,'bold')).grid(row=7,column=0,sticky = W)

#====== entry for drinks
txtcoffee1 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar1,justify='left')
txtcoffee1.grid(row =0,column=1)


txtcoffee2 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar2,justify='left')
txtcoffee2.grid(row =1,column=1)


txtcoffee3 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar3,justify='left')
txtcoffee3.grid(row =2,column=1)


txtcoffee4 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar4,justify='left')
txtcoffee4.grid(row =3,column=1)


txtcoffee5 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar5,justify='left')
txtcoffee5.grid(row =4,column=1)


txtcoffee6 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar6,justify='left')
txtcoffee6.grid(row =5,column=1)


txtcoffee7 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar7,justify='left')
txtcoffee7.grid(row =6,column=1)


txtcoffee8 = Entry(left_frame_G_Child,font=('arial',10,'bold'),bd=4,width=6, textvariable = coffeeVar8,justify='left')
txtcoffee8.grid(row =7,column=1)

#======entry for foods
txtfood1 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar9,justify='left')
txtfood1.grid(row =0,column=1)


txtfood2 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar10,justify='left')
txtfood2.grid(row =1,column=1)


txtfood3 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar11,justify='left')
txtfood3.grid(row =2,column=1)


txtfood4 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar12,justify='left')                 
txtfood4.grid(row =3,column=1)


txtfood5 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar13,justify='left')
txtfood5.grid(row =4,column=1)


txtfood6 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar14,justify='left')
txtfood6.grid(row =5,column=1)


txtfood7 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar15,justify='left')
txtfood7.grid(row =6,column=1)


txtfood8 = Entry(left_frame_G_Child2,font=('arial',10,'bold'),bd=4,width=6, textvariable = foodVar16,justify='left')
txtfood8.grid(row =7,column=1)

#=========information
lblReciept = Label(right_frameChild,font=('arial',12,'bold'),text='Cash Memo',bd =2).grid(row=0,column=0,sticky=W)
txtReciept = Text(right_frameChild,font=('arial',8,'bold'),bd=2,width=59)
txtReciept.grid(row =1,column=0)

#=========Payment information

lblCost1 = Label(left_frame_G_Child3,font=('arial',16,'bold'),text='Net Price',bd=4)
lblCost1.grid(row=0,column=0,sticky=W)
txtCost1 = Entry(left_frame_G_Child3,font=('arial',13,'bold'),bd=4,justify='left',textvariable = net_price)
txtCost1.grid(row=0,column=1,sticky=W)

lblCost2 = Label(left_frame_G_Child3,font=('arial',16,'bold'),text='Vat',bd=4)
lblCost2.grid(row=1,column=0,sticky=W)
txtCost2 = Entry(left_frame_G_Child3,font=('arial',13,'bold'),bd=4,textvariable = paidVat,justify='left')
txtCost2.grid(row=1,column=1,sticky=W)

lblCost3 = Label(left_frame_G_Child3,font=('arial',16,'bold'),text='Total Price',bd=4)
lblCost3.grid(row=2,column=0,sticky=W)
txtCost3 = Entry(left_frame_G_Child3,font=('arial',13,'bold'),bd=4,textvariable = total,justify='left')
txtCost3.grid(row=2,column=1,sticky=W)


lblPayment1 = Label(left_frame_G_Child4,font=('arial',16,'bold'),text='Paid',bd=4)
lblPayment1.grid(row=0,column=0,sticky=W)
txtPayment1 = Entry(left_frame_G_Child4,font=('arial',13,'bold'),bd=4,textvariable = paid,justify='left')
txtPayment1.grid(row=0,column=1,sticky=W)

lblPayment2 = Label(left_frame_G_Child4,font=('arial',16,'bold'),text='Discount',bd=4)
lblPayment2.grid(row=1,column=0,sticky=W)
txtPayment2 = Entry(left_frame_G_Child4,font=('arial',13,'bold'),bd=4,textvariable = discount,justify='left')
txtPayment2.grid(row=1,column=1,sticky=W)

lblPayment3 = Label(left_frame_G_Child4,font=('arial',16,'bold'),text='Return',bd=4)
lblPayment3.grid(row=2,column=0,sticky=W)
txtPayment3 = Entry(left_frame_G_Child4,font=('arial',13,'bold'),bd=4,textvariable = return_taka,justify='left')
txtPayment3.grid(row=2,column=1,sticky=W)


#=========Items information



#========button
btnTotal= Button(right_frameChild2,padx=16,pady=1,bd=4,fg='black',
                 font=('arial',11,'bold'),width=5,text="Total").grid(row=0,column=1)

btnReceipt= Button(right_frameChild2,padx=16,pady=1,bd=4,fg='black',
                 font=('arial',11,'bold'),width=5,text="Receipt").grid(row=0,column=2)

btnReset= Button(right_frameChild2,padx=16,pady=1,bd=4,fg='black',
                 font=('arial',11,'bold'),width=5,text="Reset",command =  reset).grid(row=0,column=3)

btnExit= Button(right_frameChild2,padx=16,pady=1,bd=4,fg='black',
                 font=('arial',11,'bold'),width=5,text="Exit",command =  exit).grid(row=0,column=4)






root.mainloop()
