from tkinter import *
class MyFullName:
    def __init__(self, win):

        self.lbl0 = Label(win, text="My Full Name")
        self.lbl0.place(x=175, y=10)

        self.lbl1 = Label(win, text="Enter First name:")
        self.lbl1.place(x=100, y=50)
        self.__txt1 = Entry(win, bd=1)
        self.__txt1.place(x=220, y=50)

        self.lbl2 = Label(win, text="Enter Middle name:")
        self.lbl2.place(x=100, y=100)
        self.__txt2 = Entry(win, bd=2)
        self.__txt2.place(x=220, y=100)

        self.lbl3 = Label(win, text="Enter Last name:")
        self.lbl3.place(x=100, y=150)
        self.__txt3 = Entry(win, bd=3)
        self.__txt3.place(x=220, y=150)

        self.lbl4 = Label(win, text="Your Full name is:")
        self.lbl4.place(x=100, y=200)
        self.__txt4 = Entry(win, bd=4)
        self.__txt4.place(x=220, y=200)

        self.btnfull = Button(win, text="Show Full name", fg="Black")
        self.btnfull.place(x=175, y=250)
        self.btnfull.bind('<Button-1>', self.FullName)

    def FullName(self, Full):
        LastName = str(self.__txt3.get())

        Firstname = str(self.__txt1.get())

        MiddleName = str(self.__txt2.get())

        FullName = Firstname + " " + MiddleName + " " + LastName
        self.__txt4.insert(END, str(FullName),)

FullName = Tk()
mywin = MyFullName(FullName)
FullName.geometry("600x400+10+10")
FullName.title("Midterm Exam Problem 2")
FullName.mainloop()
