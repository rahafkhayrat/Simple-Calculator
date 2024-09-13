from tkinter import *

expression= ''

def press(userInput):
    global expression
    expression=expression + str(userInput) 
    equation.set(expression)

def equal_press():
    
    try:

        global expression
        result= str(eval(expression)) 
        equation.set(result)
        expression=" "
    except:
        
        equation.set("Error")

def clear():
    global expression
    expression=''
    equation.set(" ")        
       
    
gui = Tk()
gui.title("Simple Calculator")
gui.geometry("280x250")  

titlelabel = Label(gui, text="Simple Calculator", fg="black" , font=("century 20 bold"))

titlelabel.grid(columnspan=4 , pady=20)  

equation=StringVar()

expressionField= Entry(gui , textvariable=equation)

expressionField.grid(columnspan=4,padx=5,pady=10 , ipadx=70)

Button1=Button(gui , text="1", command=lambda:press(1),height=1 , width=7)
Button1.grid(row=2 , column=0)
Button2=Button(gui , text="2",command=lambda:press(2),height=1 , width=7)
Button2.grid(row=2 , column=1)
Button3=Button(gui , text="3",command=lambda:press(3),height=1 , width=7)
Button3.grid(row=2 , column=2)
Button4=Button(gui , text="4",command=lambda:press(4),height=1 , width=7)
Button4.grid(row=3 , column=0)
Button5=Button(gui , text="5",command=lambda:press(5),height=1 , width=7)
Button5.grid(row=3 , column=1)
Button6=Button(gui , text="6",command=lambda:press(6),height=1 , width=7)
Button6.grid(row=3 , column=2)
Button7=Button(gui , text="7",command=lambda:press(7),height=1 , width=7)
Button7.grid(row=4 , column=0)
Button8=Button(gui , text="8",command=lambda:press(8),height=1 , width=8)
Button8.grid(row=4 , column=1)
Button9=Button(gui , text="9",command=lambda:press(9),height=1 , width=8)
Button9.grid(row=4 , column=2)
Button0=Button(gui , text="0",command=lambda:press(0),height=1 , width=8)
Button0.grid(row=5 , column=0)
Button_dot=Button(gui , text=".",command=lambda:press("."),height=1 , width=8)
Button_dot.grid(row=5 , column=1)
Button_equal=Button(gui , text="=",command=equal_press,height=1 , width=8 , bg="red" ,fg="black" )
Button_equal.grid(row=5 , column=2)
Button_plus=Button(gui , text="+",command=lambda:press("+"),height=1 , width=8)
Button_plus.grid(row=2 , column=3)
Button_minus=Button(gui , text="-",command=lambda:press("-"),height=1 , width=8)
Button_minus.grid(row=3 , column=3)
Button_multi=Button(gui , text="*",command=lambda:press("*"),height=1 , width=8)
Button_multi.grid(row=4 , column=3)
Button_div=Button(gui , text="/",command=lambda:press("/"),height=1 , width=8)
Button_div.grid(row=5 , column=3)
Button_clear=Button(gui , text="Clear",command=clear,height=1 , width=8)
Button_clear.grid(row=6 , column=0)

gui.mainloop()
