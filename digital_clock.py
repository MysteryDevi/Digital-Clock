import time
from tkinter import *

def clock():
    tikTok = time.strftime("%Y / %m / %d\n%H : %M : %S")
    label.config(text=str(tikTok))
    label.after(1000, clock) 


window = Tk()

window.title('Clock')
window.geometry("640x400+100+100")

label = Label(window, text=clock)
label.after(1000, clock) 

label.pack()
window.mainloop()
