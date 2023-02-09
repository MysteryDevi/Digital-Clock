import time
from tkinter import *

def clock():
    tikTok = time.strftime("%H:%M:%S %p")     # %p는 AM PM 표시
    label.config(text=str(tikTok))
    label.after(1000, clock) 
    

window = Tk()

window.title('Clock')

label = Label(window, text=clock, font=('Arial',100), bg='skyblue')
label.after(1000, clock) 

clock()
label.pack()
window.mainloop()

