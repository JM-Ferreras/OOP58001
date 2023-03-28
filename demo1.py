from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("my first GUI")

btn1=Button(window, text = "Click me", fg= "Yellow", bg="Black")
btn1.place(x=215,y=200)
txtfld = Entry(window,border=2.5)
txtfld.place(x=180,y=150)

lbl=Label(window,text="My First Demo", font="Verdana")
lbl.place(x=180, y=50)


window.mainloop()