import pyperclip

text = pyperclip.paste()
if int(len(text)) < 20:
    nbm = text
else:
    nbm = 'Window'

pyperclip.copy('''\rimport tkinter as tk\nwindow = tk.Tk()\nwindow.title("''' + nbm + '''")\nwindow.geometry("400x300")\nwindow.mainloop()''')