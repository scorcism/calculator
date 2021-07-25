from tkinter import *


def click(events):
    global scvalue  
    text = events.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                # ek value return kar dega means 2+4 raha toh 6 return kar dega
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "error"

        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()  


if __name__ == '__main__':
    root = Tk()
    root.geometry("500x600")

    root.title("Calculator with Abhishek")
    scvalue = StringVar()
    scvalue.set("")

    screen = Entry(root, textvar=scvalue, font="lucida 30 bold")
    screen.pack(fill=X, ipadx=8, pady=10, padx=10)


    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="9", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="8", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="7", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)


    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="6", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="5", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="4", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)


    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="3", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="2", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="1", font="lucida 20 bold", padx=15, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)


    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="0", font="lucida 20 bold", padx=17, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="-", font="lucida 20 bold", padx=17, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="*", font="lucida 20 bold", padx=17, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)


    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="/", font="lucida 20 bold", padx=15, pady=22)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="%", font="lucida 20 bold", padx=15, pady=22)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="=", font="lucida 20 bold", padx=15, pady=22)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    f1 = Frame(root, bg="grey")
    f1.pack()

    b = Button(f1, text="C", font="lucida 20 bold", padx=16, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text="+", font="lucida 20 bold", padx=16, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)

    b = Button(f1, text=".", font="lucida 20 bold", padx=16, pady=12)
    b.bind("<Button-1>", click)
    b.pack(side="left", padx=18, pady=4)


    root.mainloop()
