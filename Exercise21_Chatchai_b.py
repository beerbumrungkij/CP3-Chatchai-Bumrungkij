from tkinter import *
import math

def leftClickButton(event):
    try:
        result = float(textBoxWeight.get())/math.pow(float(textBoxHeigth.get())/100,2)
        if result >= 30:
            labelResult.configure(text="อ้วนมาก")
        elif result >= 25.0:
            labelResult.configure(text="อ้วน")
        elif result >= 23.0:
            labelResult.configure(text="น้ำหนักเกิน")
        elif result >= 18.6:
            labelResult.configure(text="น้ำหนักปกติ เหมาะสม")
        else :
            labelResult.configure(text="ผอมเกินไป")
    except:
        labelResult.configure(text="กรุณาป้อนตัวเลขเท่านั้น")
MainWindow = Tk()
#Heigth
labelHeigth =  Label(MainWindow,text = "ส่วนสูง (cm.)",font=('tahoma',14))
labelHeigth.grid(row =0, column = 0)

textBoxHeigth =Entry(MainWindow)
textBoxHeigth.grid(row =0, column =1)

#Weight
labelWeight = Label(MainWindow,text = "น้ำหนัก (kg.)",font=('tahoma',14))
labelWeight.grid(row =1 , column =0)

textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)

#Result
labelResult = Label(MainWindow,text = "ผลลัพธ์",font=('tahoma',16))
labelResult.grid(row=2,column =1)

#cal
calculateButton = Button(MainWindow,text= "คำนวน",font=('tahoma',14))
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row =2 , column =0)
MainWindow.mainloop()