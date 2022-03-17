from tkinter import messagebox
from tkinter import *
from tkinter.ttk import Combobox
import random, string, pyperclip

win = Tk()
win.config(bg="#000000")
win.title('Password Generator')
rdbt = IntVar()
check = IntVar()
check2 = False
rsl = ""


def checked():
    global check2
    if check2:
        check2 = False
        btn3.config(fg="#ffffff")
        txt.config(show="*")
    elif not check2:
        check2 = True
        btn3.config(fg="#0fff0f")
        txt.config(show="")


def med():
    rdb2.config(fg="#ffffff")
    rdb.config(fg="#0fff0f")
    rdb3.config(fg="#0fff0f")


def hrd():
    rdb3.config(fg="#ffffff")
    rdb.config(fg="#0fff0f")
    rdb2.config(fg="#0fff0f")


def ez():
    rdb.config(fg="#ffffff")
    rdb2.config(fg="#0fff0f")
    rdb3.config(fg="#0fff0f")


def generate():
    global rsl
    if rdbt.get() == 1:
        try:
            int(cmb.get())
            rsl = ''.join(random.choice(string.ascii_letters) for i in range(int(cmb.get())))
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")
        except:
            rsl = ''.join(random.choice(string.ascii_letters) for i in range(128))
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")
    elif rdbt.get() == 0:
        try:
            int(cmb.get())
            rsl = ''.join(
                random.choice(string.ascii_letters) + random.choice(string.digits) for i in range(int(cmb.get())))[
                  0:int(cmb.get())]
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")
        except:
            rsl = ''.join(random.choice(string.ascii_letters) + random.choice(string.digits) for i in range(64))
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")
    else:
        try:
            int(cmb.get())
            rsl = ''.join(random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(
                ['!', '#', '$', '%', '&', '(', ')', '+', '-', '=', '?', '@', '_']) for i in range(int(cmb.get())))[
                  0:int(cmb.get())]
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")
        except:
            rsl = ''.join(random.choice(string.ascii_letters) + random.choice(string.digits) + random.choice(
                ['!', '#', '$', '%', '&', '(', ')', '+', '-', '=', '?', '@', '_']) for i in range(43))
            txt.config(state='normal')
            txt.delete(0, END)
            txt.insert(INSERT, rsl)
            txt.config(state="readonly")


def copy():
    global rsl
    if not rsl == "":
        pyperclip.copy(rsl)
        messagebox.showinfo(title='Success!', message='Password copied to clipboard')
    else:
        messagebox.showwarning(title='Operation failed successfully', message="Password wasn't copied to clipboard.\nGenerate a password first!")


def encrypt(event):
    global rsl
    text = rsl
    s = 2
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif (char.islower()):
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += chr((ord(char)))
    print(result)
    return result

win.bind('<Return>', encrypt)

keno = Label(win, text="  ", bg="#000000")
lbl = Label(win, text="Length", bg="#000000", fg="#0fff0f", font=("Bahnschrift SemiLight", 12))
cmb = Combobox(win)
cmb["values"] = ("8", "9", "10", "16", "poly")
cmb.set('8')
rdb = Radiobutton(win, text="Easy", variable=rdbt, value=1, bg="#000000", fg="#0fff0f", font=("Bahnschrift SemiLight", 12), command=ez)
rdb2 = Radiobutton(win, text="Medium", variable=rdbt, value=0, bg="#000000", fg="#ffffff", font=("Bahnschrift SemiLight", 12),
                   command=med)
rdb3 = Radiobutton(win, text="Hard", variable=rdbt, value=2, bg="#000000", fg="#0fff0f", font=("Bahnschrift SemiLight", 12),
                   command=hrd)
lbl2 = Label(win, text="   Password   ", bg="#000000", fg="#0fff0f", font=("Bahnschrift SemiLight", 12))
txt = Entry(win, width=20, font=('Calibri', 10), show="*")
btn = Button(win, text="Generate", font=("Bahnschrift SemiLight", 12), bg="#000000", fg="#0fff0f", command=generate)
btn2 = Button(win, text="Copy", font=("Bahnschrift SemiLight", 12), bg="#000000", fg="#0fff0f", command=copy)
btn3 = Checkbutton(win, text="Hide", font=("Bahnschrift SemiLight", 12), bg="#000000", fg="#ffffff", variable=check, offvalue=1,
                   onvalue=0, command=checked)
txt.config(state="readonly")
cmb.config(state="readonly")

lbl.grid(column=0, row=0)
cmb.grid(column=1, row=0)
keno.grid(column=2, row=0)
rdb.grid(column=3, row=0)
rdb2.grid(column=4, row=0)
rdb3.grid(column=5, row=0)
lbl2.grid(column=0, row=1)
txt.grid(column=1, row=1)
keno.grid(column=2, row=1)
btn.grid(column=3, row=1)
btn2.grid(column=4, row=1)
btn3.grid(column=5, row=1)

win.mainloop()
