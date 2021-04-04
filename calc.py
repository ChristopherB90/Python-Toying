# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:54:52 2021

@author: Chris
"""


from tkinter import *
from decimal import *

def calcButton(a,b,d):
    button = Button(a,text=str(b),width = 10, height = 4, relief = RAISED, command = lambda: onClick(str(d)) )
    return button

def zeroButton(a,b,c,d):
    button = Button(a,text=str(b),width = 21, height = 4, relief = RAISED, command = lambda: onClick(str(d)) )
    return button

root = Tk()
baseFrame = Frame(root)
baseFrame.pack()

shapeFrame1 = Frame(baseFrame, relief = RIDGE )
shapeFrame1.pack(side=TOP)

shapeFrame2 = Frame(baseFrame, relief = RIDGE )
shapeFrame2.pack(side=TOP)

calcScreen = Label(shapeFrame1, text = "",font=("Helvetica", 18))
calcScreen.pack(side = TOP)

calcInput = Label(shapeFrame1, text = "")
calcInput.pack(side = TOP)

Shape2SubFrame1 = Frame(shapeFrame2 )
Shape2SubFrame1.pack(side=LEFT)

Shape2SubFrame2 = Frame(shapeFrame2)
Shape2SubFrame2.pack(side=RIGHT)

memFrame = Frame(Shape2SubFrame1, relief = RIDGE)
memFrame.pack(side=TOP)

buttonFrame1 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame1.pack()

buttonFrame2 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame2.pack()

buttonFrame3 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame3.pack()

buttonFrame4 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame4.pack()

equalsFrame = Frame(Shape2SubFrame1, relief = RIDGE )
equalsFrame.pack()

selectedValue = ""
screenValue = ""
memoryValue = ""
answer = ""
subScreen = ""
FixedAnswer = ""

def onClick(a):
    global selectedValue
    global subScreen
    subScreen += a
    selectedValue = subScreen.replace("*", "x") 
    calcInput.configure(text="%s"% selectedValue)

def clearAll():
    global memoryValue
    global selectedValue
    global screenValue
    global subScreen
    #subscreen is the hidden calculation line, with * instead of x to be evaluated.
    memoryValue =""
    selectedValue=""
    screenValue=""
    subScreen=""
    calcInput.configure(text="")
    calcScreen.configure(text="")
    
    
def clearScreen():
    calcScreen.configure(text="")

def clearInput():
    calcInput.configure(text="")
    
def memAdd():
    global memoryValue
    global selectedValue 
    memoryValue = calcScreen.cget("text")
    #print("memory:"+memoryValue)

def memShow():
    global selectedValue
    global memoryValue
    clearScreen()
    clearInput()
    print(selectedValue)
    selectedValue = memoryValue
    print(selectedValue)
    calcInput.configure(text="%s"% selectedValue)

def memClear():
    global memoryValue
    memoryValue = ""

def equalsClick():
    global selectedValue
    global answer
    global subScreen
    
    #removed excess decimal 0s
    answer = (str(eval(subScreen))).strip("0")
    print(answer)
    print(len(answer))
    print(len(answer[:-1]))
    
    if answer[-1] ==".":
        print(answer)
        answer = answer[:-1]
        print(answer)

        
    calcScreen.configure(text="%s"% answer)
    #selectedValue = str(answer)hhhhhh)

allClearButton = Button(memFrame,text=str("CE"),width = 10, height = 4, relief = RAISED, command = lambda: clearAll() )
allClearButton.pack(side=LEFT)

memShowButton = Button(memFrame,text=str("Mem"),width = 10, height = 4, relief = RAISED, command = lambda: memShow() )
memShowButton.pack(side=LEFT)

memAddButton = Button(memFrame,text=str("M+"),width = 10, height = 4, relief = RAISED, command = lambda: memAdd() )
memAddButton.pack(side=LEFT)
    
memClearButton = Button(Shape2SubFrame2,text=str("M-"),width = 10, height = 4, relief = RAISED, command = lambda: memClear() )
memClearButton.pack(side=TOP)
    
button1 = calcButton(buttonFrame1, 1, 1)
button1.pack(side = LEFT)

button2 = calcButton(buttonFrame1, 2, 2)
button2.pack(side = LEFT)

button3 = calcButton(buttonFrame1,3, 3)
button3.pack(side = LEFT)

button4 = calcButton(buttonFrame2,4, 4)
button4.pack(side = LEFT)

button5 = calcButton(buttonFrame2,5, 5)
button5.pack(side = LEFT)

button6 = calcButton(buttonFrame2,6, 6)
button6.pack(side = LEFT)

button7 = calcButton(buttonFrame3,7, 7)
button7.pack(side = LEFT)

button8 = calcButton(buttonFrame3,8, 8)
button8.pack(side = LEFT)

button9 = calcButton(buttonFrame3,9, 9)
button9.pack(side = LEFT)

button0 = zeroButton(buttonFrame4, 0, 4, 0)
button0.pack(side = LEFT)

buttonDecimal = calcButton(buttonFrame4, ".",".")
buttonDecimal.pack(side = LEFT)

buttonPlus = calcButton(Shape2SubFrame2,"+","+")
buttonPlus.pack(side = TOP)

buttonMinus = calcButton(Shape2SubFrame2,"-","-")
buttonMinus.pack(side = TOP)

buttonMultiply= calcButton(Shape2SubFrame2,"x","*")
buttonMultiply.pack(side = TOP)

buttonDivide = calcButton(Shape2SubFrame2,"/","/")
buttonDivide.pack(side = TOP)

equalsButton = Button(baseFrame,text=str("="),width = 43, height = 4, relief = RAISED, command = lambda: equalsClick() )
equalsButton.pack(side=BOTTOM)

root.mainloop()


# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:54:52 2021

@author: Chris
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
from tkinter import *


def calcButton(a,b,d):
    button = Button(a,text=str(b),width = 10, height = 4, relief = RAISED, command = onClick(str(d)) )
    return button

def zeroButton(a,b,c,d):
    button = Button(a,text=str(b),width = 21, height = 4, relief = RAISED, command = onClick(str(d)) )
    return button

root = Tk()
baseFrame = Frame(root)
baseFrame.pack()

shapeFrame1 = Frame(baseFrame, relief = RIDGE )
shapeFrame1.pack(side=TOP)

shapeFrame2 = Frame(baseFrame, relief = RIDGE )
shapeFrame2.pack(side=BOTTOM)

greet = Label(shapeFrame1, text = "")
greet.pack(side = TOP)


Shape2SubFrame1 = Frame(shapeFrame2)
Shape2SubFrame1.pack(side=LEFT)

Shape2SubFrame2 = Frame(shapeFrame2)
Shape2SubFrame2.pack(side=RIGHT)

buttonFrame1 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame1.pack()

buttonFrame2 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame2.pack()

buttonFrame3 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame3.pack()

buttonFrame4 = Frame(Shape2SubFrame1, relief = RIDGE )
buttonFrame4.pack()

selectedValue = ""
screenValue = ""

def onClick(a):
    global selectedValue
    selectedValue += a
    greet.configure(text="%s"% selectedValue)
 
  

button1 = Button(buttonFrame1,text=str(1),width = 10, height = 4, relief = RAISED, command = onClick("1") )
button1.pack(side = LEFT)

button2 = Button(buttonFrame1,text=str(2),width = 10, height = 4, relief = RAISED )
button2.pack(side = LEFT)

button3 = Button(buttonFrame1,text=str(3),width = 10, height = 4, relief = RAISED )
button3.pack(side = LEFT)

button4 = Button(buttonFrame2,text=str(4),width = 10, height = 4, relief = RAISED )
button4.pack(side = LEFT)

button5 = Button(buttonFrame2,text=str(5),width = 10, height = 4, relief = RAISED )
button5.pack(side = LEFT)

button6 = Button(buttonFrame2,text=str(6),width = 10, height = 4, relief = RAISED )
button6.pack(side = LEFT)

button7 = Button(buttonFrame3,text=str(7),width = 10, height = 4, relief = RAISED )
button7.pack(side = LEFT)

button8 = Button(buttonFrame3,text=str(8),width = 10, height = 4, relief = RAISED )
button8.pack(side = LEFT)

button9 = Button(buttonFrame3,text=str(9),width = 10, height = 4, relief = RAISED )
button9.pack(side = LEFT)

button0 = Button(buttonFrame4,text=str(0),width = 21, height = 4, relief = RAISED )
button0.pack(side = LEFT)


buttonDecimal = Button(buttonFrame4,text=str("."),width = 10, height = 4, relief = RAISED )
buttonDecimal.pack(side = TOP)

buttonPlus = Button(Shape2SubFrame2,text=str("+"),width = 10, height = 4, relief = RAISED )
buttonPlus.pack(side = TOP)

buttonMinus = Button(Shape2SubFrame2,text=str("-"),width = 10, height = 4, relief = RAISED )
buttonMinus.pack(side = TOP)

buttonMultiply = Button(Shape2SubFrame2,text=str("x"),width = 10, height = 4, relief = RAISED )
buttonMultiply.pack(side = TOP)

buttonDivide = Button(Shape2SubFrame2,text=str("/"),width = 10, height = 4, relief = RAISED )
buttonDivide.pack(side = TOP)




root.mainloop()

"""








