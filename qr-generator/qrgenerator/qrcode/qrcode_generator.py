from copy import Error
from pyqrcode import create
import sys

if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import messagebox
else:
    import Tkinter as tk
    from tkinter import messagebox


def callback(event):
    print('e.get():', data.get())
    # or more universal
    print('event.widget.get():', event.widget.get())
    # select text after 5ms
    root.after(5, select_all, event.widget)


def select_all(widget):
    # select text
    widget.select_range(0, 'end')
    # move cursor to the end
    widget.icursor('end')

# Getting data


root = tk.Tk()
root.title('Qr Code Generator')
data = tk.Entry(root)
data.bind('<Control-a>', callback)


def gen_qr():
    global dta
    dta = data.get()
    if len(dta) != 0 and not dta.isspace():
        print(dta)
        dta = create(dta)
        test = dta.xbm(scale=5)
        global xbm_image
        xbm_image = tk.BitmapImage(
            data=test,
            foreground="black",
            background="white"
        )
        image_view.config(image=xbm_image)
        statement.config(text="QR code for: " + str(data.get()))
    else:
        messagebox.showwarning('warning', 'Fields are Required!')
    try:
        generate_file(dta)
    except Error as e:
        print(e)



def generate_file(dta):
    data = dta
    data.png('qrcode.png', scale=8)


heading = tk.Label(root, text="QR code Generator", font="ubuntu 25")
subtitle = tk.Label(root, text="Enter data", font="ubuntu 20")
make_button = tk.Button(root, text="Make QR", font="ubuntu 20", command=gen_qr)
image_view = tk.Label(root)
statement = tk.Label(root)


# GUI GRID


heading.grid(row=0, column=0, columnspan=2)
subtitle.grid(row=1, column=0)
data.grid(row=1, column=1)
make_button.grid(row=2, column=0, columnspan=2)
image_view.grid(row=3, column=0, columnspan=2)
statement.grid(row=4, column=0, columnspan=2)

root.mainloop()
