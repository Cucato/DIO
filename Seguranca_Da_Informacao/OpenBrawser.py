import webbrowser
from tkinter import *

root = Tk()
#quando tem espaço nos parenteses, significa que noa tem nome
root.title('Abrir o Browser')
root.geometry('300x200')

def google():
    webbrowser.open('www.google.com')

mygoogle = Button(root, text='Abrir o google', command=google).pack(pady=30)
root.mainloop()
