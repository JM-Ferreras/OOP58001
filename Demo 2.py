from tkinter import*
win=Tk()

win.geometry("400x200+10+10")
win.title("Grid Manager")

#put your widget here

txt1=Entry(win, bd=2, justify="center")
txt1.grid(row=0, column=0)
txt1.insert(0, "row 0" + " "+"column 0")

txt2=Entry(win, bd=2, justify="center")
txt2.grid(row=0, column=1)
txt2.insert(0, "row 0" + " "+"column 1")

txt3=Entry(win, bd=2, justify="center")
txt3.grid(row=0, column=2)
txt3.insert(0, "row 0" + " "+"column 2")

txt4=Entry(win, bd=2, justify="center")
txt4.grid(row=1, column=0)
txt4.insert(0, "row 1" + " "+"column 0")

txt5=Entry(win, bd=2, justify="center")
txt5.grid(row=1, column=1)
txt5.insert(0, "row 1" + " "+"column 1")

txt6=Entry(win, bd=2, justify="center")
txt6.grid(row=1, column=2)
txt6.insert(0, "row 1" + " "+"column 2")

win.mainloop()
