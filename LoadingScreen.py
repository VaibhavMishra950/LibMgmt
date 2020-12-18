from tkinter import *
from tkinter import ttk
import time

def load_pb():
	pb['value'] += 1
	load_sc.update_idletasks()
	time.sleep(0.015)
	if pb['value'] == 100:
		load_sc.destroy()
	else:
		load_pb()

def load_fn():
	global load_sc
	global pb
	load_sc = Tk()
	
	Label(load_sc, text = "Loading Database", font = "MiClock\ ExtraLight 10").pack(padx = 20, pady = 30)
	pb = ttk.Progressbar(load_sc, orient = HORIZONTAL, length = 600, max = 100, value = 0, mode = 'determinate')
	pb.pack(padx = 20, pady = 40)
	
	load_pb()
	load_sc.mainloop()
	

root = Tk()

btn_load = Button(root, text = "Load Database", font = "MiClock\ ExtraLight 9", command = load_fn)
btn_load.pack(padx = 40, pady = 40)

root.mainloop()