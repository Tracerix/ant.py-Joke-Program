import math
import time
from math import pi, sin, cos
from random import randint, choice
from win32api import *
from win32con import *
from win32gui import *
import tkinter as tk
import sys, site

desk = GetDC(0)
x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()


def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()



def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()

def rainbow_effect():
    for i in range(0, 100):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        color = RGB(r, g, b)

        brush = CreateSolidBrush(color)
        SelectObject(desk, brush)
        PatBlt(desk, 0, 0, x, y, PATINVERT)
        Sleep(10)

        DeleteObject(brush)



def shake_effect():
    shake_range = 20
    for _ in range(100):
        x_offset = randint(-shake_range, shake_range)
        y_offset = randint(-shake_range, shake_range)

        BitBlt(desk, x_offset, y_offset, x, y, desk, 0, 0, SRCCOPY)
        Sleep(10)
shake_effect()
rainbow_effect()
def close_window():
    root.destroy()

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, text="IM AN ANT, KILL ME IF YOU CAN", fg="white", bg="black", font=("Helvetica", 24))
label.pack(expand=True)

root.after(200, close_window)  # Close the window after 0.2 seconds (200 milliseconds)

root.mainloop()

if sys.version_info[0] ==3 and sys.version_info[1]>=5:
    pass
else:
    raise Exception("Must be using Python 3.5 or newer, but not python 4")

import tkinter as tk
import random
import pip

try:
    from PIL import ImageTk, Image
except ImportError:
    if hasattr(pip, 'main'):
        pip.main(['install', '--user', 'pillow'])
    else:
        import pip._internal
        pip._internal.main(['install', '--user', 'pillow'])
        
    from importlib import reload
    reload(site)
    from PIL import ImageTk, Image

from io import BytesIO
import urllib.request as request
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
root = tk.Tk()

URL="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR4M7-AC3MZeRoSbwHda789UMKnqbyDLV_RQ&usqp=CAUhttps://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTR4M7-AC3MZeRoSbwHda789UMKnqbyDLV_RQ&usqp=CAU"
response = request.urlopen(URL, context=ctx)
img_data = response.read()
h=BytesIO(img_data)
open_i=Image.open(h)
imagen = open_i.resize((400, 400), Image.ANTIALIAS)
image = ImageTk.PhotoImage(imagen)

def startInfiniteLoop():
    i = 0
    otherFrame = []
    while True:
        tkl=tk.Toplevel()
        if tkl.winfo_screenwidth() > 1800:
            x = random.randint(-650, 1400)
        elif tkl.winfo_screenwidth() > 1500:
            x = random.randint(-600, 1200)
        elif tkl.winfo_screenwidth() > 1250:
            x = random.randint(-600, 900)
        else:
            x = random.randint(-500, 800)
        y =  random.randint(-550, 550)
        tkl.geometry("+%d+%d" % (x + 400, y + 400))
        tkl.title("IM AN ANT!")
        label = tk.Label(tkl, image=image)
        label.pack(fill="both")
        otherFrame.append(tkl)
        i += 1
        tkl.update()
        if i%500 == 0:
            root.update()
            
def IDIOT():
    print("ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT! ANT!")

label = tk.Label(root, image=image)
label.pack(fill='both')
IDIOT()
startInfiniteLoop()
root.mainloop()

