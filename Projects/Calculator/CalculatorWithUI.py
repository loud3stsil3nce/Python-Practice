from tkinter import *
import CLICalculator
add = CLICalculator.add
subtract = CLICalculator.subtract
multiply = CLICalculator.multiply
divide = CLICalculator.divide
power = CLICalculator.power
squareRoot = CLICalculator.squareRoot


def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals():
    try:
        global equation_text
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except ZeroDivisionError:
        equation_label.set("arithmetic error")
        equation_text = ""
    except SyntaxError:
        equation_label.set("syntax error")
        equation_text = ""
def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""


window = Tk()
window.geometry("600x603")
window.title("Calculator App")
icon = PhotoImage(file='Games\Calculator\download.png')
window.iconphoto(True, icon)
window.config(background="teal")

equation_text= ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg='white', width=40, height=2)
label.pack()

frame = Frame(window)
frame.pack()


button1 = Button(frame, text=1, height=4, width=9, font=35,
                 command=lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame, text=2, height=4, width=9, font=35,
                 command=lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame, text=3, height=4, width=9, font=35,
                 command=lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame, text=4, height=4, width=9, font=35,
                 command=lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame, text=5, height=4, width=9, font=35,
                 command=lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame, text=6, height=4, width=9, font=35,
                 command=lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame, text=7, height=4, width=9, font=35,
                 command=lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame, text=8, height=4, width=9, font=35,
                 command=lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame, text=9, height=4, width=9, font=35,
                 command=lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame, text=0, height=4, width=9, font=35,
                 command=lambda: button_press(0))
button0.grid(row=3,column=0)


plus = Button(frame, text="+", height=4, width=9, font=35,
              command=lambda: button_press("+"))
plus.grid(row=0, column=3)

minus = Button(frame, text="-", height=4, width=9, font=35,
              command=lambda: button_press("-"))
minus.grid(row=1, column=3)

times = Button(frame, text="x", height=4, width=9, font=35,
              command=lambda: button_press("*"))
times.grid(row=2, column=3)

divide = Button(frame, text="/", height=4, width=9, font=35,
              command=lambda: button_press("/"))
divide.grid(row=3, column=3)


power = Button(frame, text="^", height=4, width=9, font=35,
              command=lambda: button_press("**"))
power.grid(row=3, column=2)

decimal = Button(frame, text=".", height=4, width=9, font=35,
              command=lambda: button_press("."))
decimal.grid(row=3, column=1)



subframe = Frame(window)
subframe.pack()

clear = Button(subframe, text="clear", height=4, width=9, font=35,
              command=clear)
clear.grid(row=0, column=1)

equal = Button(subframe, text="=", height=4, width=9, font=35,
              command=equals)
equal.grid(row=0, column=2)

labelleft = Label(subframe, text="", height=4, width=9, font=35,
                  )
labelleft.grid(row=0, column=0)
labelright = Label(subframe, text="", height=4, width=9, font=35,
                  )
labelright.grid(row=0, column=3)

window.mainloop()
