from MyQR import myqr
import os
import sys


if sys.version_info[0] == 3:
    import tkinter as tk
    from tkinter import messagebox, filedialog as fd
else:
    import Tkinter as tk
    from Tkinter import messagebox, filedialog as fd


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
root.title('Qr Code Animate Generator')
data = tk.Entry(root)
data.bind('<Control-a>', callback)

def generate_qr():
    dta = data.get()
    if len(dta) != 0 and not dta.isspace() and len(filepath) != 0:
        version, level, qr_name = myqr.run(
        # Add string or a URL (add http(s):// before it)
        words=dta,     

        # Set the highest fault tolerance rate
        version=1,               

        # Control the error correction level,
        # the range is L, M, Q, H, increasing from left to right
        level='H',               

        #Add file name eg. your_image.gif/jpg/png/bmp
        picture = filepath, 

        # Color QR code
        colorized=True,

        # Set contrast of the image,
        # 1.0 - original picture / default,
        # small value - low contrast,
        # large value - high contrast.
        contrast=1.0,

        # Set brightness of the image,
        # adjustment values ​​same as above
        brightness=1.0,

        # Save the file name, the format can be jpg, png, bmp, gif
        save_name="qrcodeanimate.gif",

        #Control location
        save_dir=os.getcwd()
        )
        tk.Label(root, text='QR Code Created, Please, check in your directory!', foreground='green').grid(row=6, columnspan=2, pady=10)
        statement.config(text="QR code for: " + str(data.get()))
        print("Done")
    else:
        messagebox.showwarning('warning', 'Fields are Required!')

def open_file():
    file = fd.askopenfile(mode = 'r', filetypes = [('Image Files', '*.gif')])
    if file:
        global filepath
        filepath = os.path.abspath(file.name)
        print(filepath)
        tk.Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=6, columnspan=2, pady=10)
    else:
        tk.Label(root, text='Please, Upload a File', foreground='red').grid(row=6, columnspan=2, pady=10)
    

heading = tk.Label(root, text="QR code Generator", font="ubuntu 20")
subtitle = tk.Label(root, text="Add message or an URL (add http(s):// before it)", font="ubuntu 15")
make_button = tk.Button(root, text="Make QR", font="ubuntu 15", command=lambda: [generate_qr()])
image_view = tk.Label(root)
statement = tk.Label(root)
upload_button = tk.Button(root, text="Upload Image (Only gif)", font="ubuntu 15", command=lambda: [open_file()])


heading.grid(row=0, column=0, columnspan=2)
subtitle.grid(row=1, column=0)
data.grid(row=2, column=0, columnspan=2)
make_button.grid(row=4, column=0, columnspan=2)
upload_button.grid(row=3, column=0, columnspan=2)
statement.grid(row=5, column=0, columnspan=2)

root.mainloop()
