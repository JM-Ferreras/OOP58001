from tkinter import *
class DistanceConversion:
    def __init__(self, win):

        self.lbl1 = Label(win, text="Enter Meter Length:")
        self.lbl1.place(x=100, y=50)
        self.lbl12 = Label(win, text="meters")
        self.lbl12.place(x=350, y=50)
        self.__txt1 = Entry(win, bd=1)
        self.__txt1.place(x=220, y=50)

        self.lbl2 = Label(win, text="Meters to Centimeters:")
        self.lbl2.place(x=100, y=200)
        self.lbl12 = Label(win, text="centimeters")
        self.lbl12.place(x=360, y=200)
        self.__txt2 = Entry(win, bd=2)
        self.__txt2.place(x=230, y=200)

        self.lbl3 = Label(win, text="Meters to Kilometers:")
        self.lbl3.place(x=100, y=230)
        self.lbl12 = Label(win, text="kilometers")
        self.lbl12.place(x=360, y=230)
        self.__txt3 = Entry(win, bd=3)
        self.__txt3.place(x=230, y=230)

        self.lbl4 = Label(win, text="Meters to inches:")
        self.lbl4.place(x=100, y=260)
        self.lbl12 = Label(win, text="inches")
        self.lbl12.place(x=360, y=260)
        self.__txt4 = Entry(win, bd=4)
        self.__txt4.place(x=230, y=260)

        self.btnconv = Button(win, text="Convert", fg="Black")
        self.btnconv.place(x=250, y=90)
        self.btnconv.bind('<Button-1>', self.conv)

    def conv(self, conv):
        self.__txt2.delete(0, 'end')
        mcm = float(self.__txt1.get())
        ans1 = mcm*100
        self.__txt2.insert(END, float(ans1))

        self.__txt3.delete(0, 'end')
        mkm = float(self.__txt1.get())
        ans2 = mkm / 1000
        self.__txt3.insert(END, float(ans2))

        self.__txt4.delete(0, 'end')
        min = float(self.__txt1.get())
        ans3 = min * 39.37
        self.__txt4.insert(END, float(ans3))

DisCon = Tk()
mywin = DistanceConversion(DisCon)
DisCon.geometry("600x400+10+10")
DisCon.title("Conversion Methods")
DisCon.mainloop()