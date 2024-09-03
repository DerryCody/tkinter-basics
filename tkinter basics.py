import tkinter

screen=tkinter.Tk()
screen.geometry("900x900")

screen.title("Basics")
screen.configure(background="pink")

label=tkinter.Label(screen,background="brown",text="Login",font=("times new roman",35))
label.pack()

label=tkinter.Label(screen,background="white",text="Username",fg="black",font=("times new roman",35))
label.place(x=100,y=300)

label=tkinter.Label(screen,background="white",text="Password",fg="black",font=("times new roman",35))
label.place(x=100,y=550)

entry=tkinter.Entry(screen,font=("comic sans",35))
entry.place(x=350,y=300)

entry=tkinter.Entry(screen,font=("comic sans",35))
entry.place(x=350,y=550)

button=tkinter.Button(screen,fg="green",text="Submit",font=("times new roman",20))
button.place(x=100,y=625)



screen.mainloop()