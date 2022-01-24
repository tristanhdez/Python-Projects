import sys


if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk

root = tk.Tk()
root.title('Select One')
data = tk.Entry(root)


def open_normal():
    root.destroy()
    import qrcode.qrcode_generator


def open_animate():
    root.destroy()
    import animateqrcode.qrcode_animate_generator


heading = tk.Label(root, text="Choose One", font="ubuntu 30")
button_normal = tk.Button(root, text="Make Normal QR", font="ubuntu 20", command=lambda: [open_normal()])
button_animate = tk.Button(root, text="Make Animate QR", font="ubuntu 20", command=lambda: [open_animate()])

# GUI


heading.grid(row=0, column=0, columnspan=5)
button_normal.grid(row=1, column=1, columnspan=1)
button_animate.grid(row=1, column=2, columnspan=2)


root.resizable(False, False)
root.mainloop()
