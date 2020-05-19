from tkinter import *

text_pay = "ค่างวดต่อเดือน (บาท) :"
text_month = "จำนวนงวด (เดือน) :"
text_loan = "ยอดจัดไฟแนนซ์ (บาท) :"
text_down = "เปอร์เซ็นเงินดาวน์ (%) :"
text_msg = "กรุณาป้อนตัวเลข"
f = ('tahoma', 11)


def setDefault():
    labelLoan.configure(text="")
    labelLoan_result.configure(text="")
    labelPay.configure(text="")
    labelPay_result.configure(text="")
    labelPDown.configure(text="")
    labelMonth.configure(text="")
    labelMonth_result.configure(text="")

def leftClickButton(event):
    try:
        car_price = float(textBoxCarPrice.get())
        down = float(textBoxDown.get())
        interest = float(textBoxInterest.get())
        period = int(textBoxPeriod.get())

        result = car_price - down
        down_result = down / car_price * 100
        month = period * 12
        result_int = ((result * (interest / 100) * period) + result) / month

        if down > car_price:
            labelPDown_result.configure(text="เงินดาวน์มากกว่าราคารถ", foreground="red")
            setDefault()

        elif interest > 100:
            labelPDown_result.configure(text="ใส่จำนวนดอกเบี้ยสูงผิดปกติ", foreground="red")
            setDefault()

        elif period > 9:
            labelPDown_result.configure(text="ใส่จำนวนปีมากกว่า 9 ปี", foreground="red")
            setDefault()

        else:
            labelLoan.configure(text=text_loan)
            labelLoan_result.configure(text='{:,.2f}'.format(result), foreground="green")

            labelPay.configure(text=text_pay)
            labelPay_result.configure(text='{:,.2f}'.format(result_int), foreground="green")

            labelPDown.configure(text=text_down)
            labelPDown_result.configure(text='{:,.2f}'.format(down_result), foreground="green")

            labelMonth.configure(text=text_month)
            labelMonth_result.configure(text='{:,.0f}'.format(month), foreground="green")

    except:
        labelPDown_result.configure(text="กรุณาป้อนตัวเลข", foreground="red")
        setDefault()


MainWindow = Tk()
MainWindow.title("โปรแกรมคำนวณเงินค่างวดรถต่อเดือน")

# title
labelTitle = Label(MainWindow, text="โปรแกรมคำนวณเงินค่างวดรถต่อเดือน", font=('tahoma', 14), width=30, height=2,
                   foreground="blue")
labelTitle.grid(row=0, column=0, columnspan=3)

# Dev
labelName = Label(MainWindow, text="ผู้พัฒนา : ฉัตรชัย บำรุงกิจ", font=('tahoma', 10))
labelName.grid(row=0, column=3, columnspan=3)

# car price
labelCarPrice = Label(MainWindow, text="ราคารถ (บาท) :", font=f)
labelCarPrice.grid(row=1, column=0, ipadx=3, sticky='e')

textBoxCarPrice = Entry(MainWindow)
textBoxCarPrice.grid(row=1, column=1, ipadx=5, ipady=5, pady=10)

# down
labelDown = Label(MainWindow, text="จำนวนเงินดาวน์ (บาท) :", font=f)
labelDown.grid(row=2, column=0, ipadx=3, sticky='e')

textBoxDown = Entry(MainWindow)
textBoxDown.grid(row=2, column=1, ipadx=5, ipady=5, pady=10)

# period
labelPeriod = Label(MainWindow, text="เวลาผ่อนชำระ 1-9 (ปี)  :", font=f)
labelPeriod.grid(row=3, column=0, ipadx=3, sticky='e')

textBoxPeriod = Entry(MainWindow)
textBoxPeriod.grid(row=3, column=1, ipadx=5, ipady=5, pady=10)

# interest
labelInterest = Label(MainWindow, text="ดอกเบี้ยต่อปี (%) :", font=f)
labelInterest.grid(row=4, column=0, ipadx=3, sticky='e')

textBoxInterest = Entry(MainWindow)
textBoxInterest.grid(row=4, column=1, ipadx=5, ipady=5, pady=10)

# calculate
calculateButton = Button(MainWindow, text=" คำนวน ", font=f)
calculateButton.bind('<Button-1>', leftClickButton)
calculateButton.grid(row=4, column=2, padx=5, pady=10, sticky='w')

# percent_down
labelPDown = Label(MainWindow, text="", font=f)
labelPDown.grid(row=5, column=0, ipadx=3, sticky='e')

labelPDown_result = Label(MainWindow, text="", font=f)
labelPDown_result.grid(row=5, column=1, ipadx=3, sticky='e')

# loan
labelLoan = Label(MainWindow, text="", font=f)
labelLoan.grid(row=6, column=0, ipadx=3, sticky='e')

labelLoan_result = Label(MainWindow, text="", font=f)
labelLoan_result.grid(row=6, column=1, ipadx=3, sticky='e')

# pay
labelPay = Label(MainWindow, text="", font=f)
labelPay.grid(row=7, column=0, ipadx=3, sticky='e')

labelPay_result = Label(MainWindow, text="", font=f)
labelPay_result.grid(row=7, column=1, ipadx=3, sticky='e')

# pay
labelMonth = Label(MainWindow, text="", font=f)
labelMonth.grid(row=8, column=0, ipadx=3, sticky='e')

labelMonth_result = Label(MainWindow, text="", font=f)
labelMonth_result.grid(row=8, column=1, ipadx=3, sticky='e')

MainWindow.mainloop()
