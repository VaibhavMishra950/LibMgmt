#Importing Libraries.
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st
from tkinter import messagebox as mb
from PIL import Image, ImageTk
import mysql.connector as sql

#Difining Functions
#########################################


def update_member():
	if (ent_name_update.get() == "" or ent_class_update.get() == "" or gender_var_update.get() == "" or ent_mobile_update.get() == ""):
		mb.showerror("Library Management", "All Fields Require At Least One Value.")
	else:
		cursor.execute("update members set name = '{}', class = {}, gender = '{}', mobile = {} where rollno = {}".format(ent_name_update.get(), ent_class_update.get(), gender_var_update.get(), ent_mobile_update.get(), ent_rollno_update['text']))
		con.commit()
		mb.showinfo("Library Management", "Member Details Updated Successfully!")
		win_update_member.destroy()

def update_member_win():
	global ent_gender_update_male
	global ent_gender_update_female
	global ent_rollno_update
	global ent_name_update
	global ent_class_update
	global ent_mobile_update
	global gender_var_update
	global win_update_member
	win_update_member = Tk()
	win_update_member.title("Update Member Details")
	
	
	frm_ent_data_update = LabelFrame(win_update_member, text = "Update Details")
	frm_ent_data_update.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	frm_buttons = Frame(win_update_member)
	frm_buttons.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	lbl_rollno_update = Label(frm_ent_data_update, text = "Member\'s Roll No: ")
	lbl_rollno_update.grid(row = 0, column = 0, padx = 10, pady = 10)
	ent_rollno_update = Label(frm_ent_data_update, text = "")
	ent_rollno_update.grid(row = 0, column = 1, padx = 10, pady = 10)
	
	lbl_name_update = Label(frm_ent_data_update, text = "Member\'s Name: ")
	lbl_name_update.grid(row = 1, column = 0, padx = 10, pady = 10)
	ent_name_update = Entry(frm_ent_data_update)
	ent_name_update.grid(row = 1, column = 1, padx = 10, pady = 10)
	
	lbl_class_update = Label(frm_ent_data_update, text = "Member\'s Class: ")
	lbl_class_update.grid(row = 2, column = 0, padx = 10, pady = 10)
	ent_class_update = Entry(frm_ent_data_update)
	ent_class_update.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	gender_var_update = StringVar(frm_ent_data_update)
	
	lbl_gender_update = Label(frm_ent_data_update, text = "Member\'s Gender: ")
	lbl_gender_update.grid(row = 3, column = 0, padx = 10, pady = 10)
	ent_gender_update = Frame(frm_ent_data_update) 
	ent_gender_update.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	ent_gender_update_male = Radiobutton(ent_gender_update, indicatoron = 1, text = "   Male   ", variable = gender_var_update, value = 'M')
	ent_gender_update_male.pack(anchor = W, fill = X)
    
	ent_gender_update_female = Radiobutton(ent_gender_update, indicatoron = 1, text = "   Female   ", variable = gender_var_update, value = 'F')
	ent_gender_update_female.pack(anchor = W ,fill = X)
	
	lbl_mobile_update = Label(frm_ent_data_update, text = "Member\'s Mobile No: ")
	lbl_mobile_update.grid(row = 4, column = 0, padx = 10, pady = 10)
	ent_mobile_update = Entry(frm_ent_data_update)
	ent_mobile_update.grid(row = 4, column = 1, padx = 10, pady = 10)
	
	btn_close_update = Button(frm_buttons,text = "Close", command = win_update_member.destroy, font = ("MiClock ExtraLight", 8, "bold"))
	btn_close_update.grid(row = 0, column = 0, padx = 100, pady = 10)
	
	btn_submit_update = Button(frm_buttons, text = "Update", command = update_member, font = ("MiClock ExtraLight", 8, "bold"))
	btn_submit_update.grid(row = 0, column = 1, padx = 100, pady = 10)
	#Inserting Data
	############
	
	cursor.execute("select * from members where rollno = {}".format(roll_ent_for_update.get()))
	data_to_insert = cursor.fetchall()
	
	ent_rollno_update['text'] = data_to_insert[0][0]
	ent_name_update.insert(0, data_to_insert[0][1])
	ent_class_update.insert(0, data_to_insert[0][2])
	if data_to_insert[0][3] == 'M':
		ent_gender_update_male.select()
	else:
		ent_gender_update_female.select()
	
	ent_mobile_update.insert(0, data_to_insert[0][4])
	
	##########
	
	
	win_update_member.mainloop()

def check_roll_for_update():
	if roll_ent_for_update.get() == "":
		mb.showerror("Library Management", "Please Enter Roll No.")
	else:
		cursor.execute("select rollno from members")
		test_data = cursor.fetchall()
		for x in test_data:
			if x[0] == int(roll_ent_for_update.get()):
				update_member_win()
				break
		else:
			mb.showerror("Library Management", "No member with Roll No {}!".format(roll_ent_for_update.get()))

def update_member_win_root():
	global roll_ent_for_update
	temp_ent_roll_win = Tk()
	temp_ent_roll_win.title("Enter Roll Number")
	f1 = Frame(temp_ent_roll_win)
	f1.pack()
	Label(f1, text = "Enter Roll No: ").grid(row = 0 ,column = 0, padx = 20, pady = 20)
	roll_ent_for_update = Entry(f1)
	roll_ent_for_update.grid(row = 0, column = 1, padx = 20, pady = 20)
	
	Button(temp_ent_roll_win, text = "   Continue   ", command = check_roll_for_update, font = ("MiClock ExtraLight", 8, "bold")).pack(pady = 30)
	
	temp_ent_roll_win.mainloop()

def get_member_details_del():
	member_details_data_area.configure(state ='normal')
	member_details_data_area.delete(1.0, END)
	
	roll_to_delete = int(ent_roll_delete.get())
	list_of_details = []
	query = "select * from members where rollno = {}".format(roll_to_delete)
	cursor.execute(query)
	raw_data = cursor.fetchall()
	try:
		loop_var = raw_data[0]
		for x in loop_var:
			list_of_details.append(x)

	
	
		data = """
***********************************
   M E M B E R     D E T A I L S
***********************************

Roll No   : {} 
Name      : {}
Class     : {}
Gender    : {}
Mobile No : {}

***********************************
		""".format(*list_of_details)
		member_details_data_area.insert(1.0, data)
		member_details_data_area.configure(state ='disabled')
		btn_delete_member['state'] = NORMAL
	except IndexError:
		mb.showerror("Library Management", "No Member With Roll No {} Found!!!".format(ent_roll_delete.get()))
	

def delete_member():
	bool_var = mb.askyesno("Library Management", "Do You Really Wan\'t To Delete Data Of \n Member {}?".format(ent_roll_delete.get()))
	if bool_var:
		cursor.execute("delete from members where rollno = {}".format(ent_roll_delete.get()))
		mb.showinfo("Library Management", "Member {} deleted Successfully!".format(ent_roll_delete.get()))
		win_delete_member.destroy()
	else:
		win_delete_member.destroy()
	

def delete_member_win():
    global btn_delete_member
    global member_details_data_area
    global ent_roll_delete
    global win_delete_member
    win_delete_member = Tk()
    win_delete_member.title("Delete A Member")
    f1 = Frame(win_delete_member)
    f1.pack(padx = 10, ipady = 30)
    
    f2 = Frame(win_delete_member)
    f2.pack(padx = 10, ipady = 30)
    
    f3 = Frame(win_delete_member)
    f3.pack(padx = 10, ipady = 30)
    
    Label(f1, text = "Enter Roll No: ").grid(row = 0, column = 0, padx = 10, pady = 10)
    ent_roll_delete = Entry(f1)
    ent_roll_delete.grid(row = 0, column = 1 ,padx = 10, pady = 10)
    Button(f2, text = "Get Data", command = get_member_details_del, font = ("MiClock ExtraLight", 8, "bold")).pack(padx = 10, pady = 10)
    
    member_details_data_area = st.ScrolledText(f2,
                                width = 35,
                                height = 10,
                                foreground = "blue")
    member_details_data_area.pack(padx = 40, pady = 20)
    member_details_data_area.configure(state ='disabled')
    btn_delete_member = Button(f3, text = "Delete This Member", command = delete_member, font = ("MiClock ExtraLight", 8, "bold"))
    btn_delete_member.pack()
    btn_delete_member['state']= DISABLED
    
    win_delete_member.mainloop()



def show_members():
    cursor.execute('select * from members')
    data = cursor.fetchall()
    count = cursor.rowcount
    
    win_show_members = Tk()
    win_show_members.title("All Members")
        
    cols = ["ROLL NO", "NAME", "CLASS", "GENDER", "MOBILE NO"]
    for c in range(5):
    	Label(win_show_members, text=cols[c], font=("Carrois Gothic SC", 10, "bold")).grid(row=0, column=c, padx=8, pady = 15)
    for x in range(count):
    	for y in range(5):
    		l = Label(win_show_members, text = data[x][y], font = ("MiClock ExtraLight", 8))
    		l.grid(row = x+1, column = y, padx = 8, pady = 7, sticky = W, ipadx = 40)
    
    
    win_show_members.mainloop()


def add_member():
	if (ent_rollno_add.get() == "" or ent_name_add.get() == "" or ent_class_add.get() == "" or gender_var.get() == "" or ent_mobile_add.get() == ""):
		mb.showerror("Library Management", "All Fields Require At Least One Value")
		print(ent_rollno_add.get() == "",  ent_name_add.get() == "", ent_class_add.get() == "", gender_var.get(), ent_mobile_add.get() == "")
	else:
		cursor.execute("select rollno from members")
		raw_data_roll = cursor.fetchall()
		for x in raw_data_roll:
			if x[0] == int(ent_rollno_add.get()):
				mb.showerror("Library Management", "Member {} Already Exists!".format(ent_roll_add.get()))
		else:
			add_member_query = "insert into members values({}, '{}', {}, '{}', {})".format(ent_rollno_add.get(), ent_name_add.get(), ent_class_add.get(), gender_var.get(), ent_mobile_add.get())
			cursor.execute(add_member_query)
			con.commit()
			mb.showinfo("Library Management", "Member Added Successfully!")
			win_add_member.destroy()
	

def clr_member():
	ent_rollno_add.delete(0, END)
	ent_name_add.delete(0, END)
	ent_class_add.delete(0, END)
	ent_gender_add_male.deselect()
	ent_gender_add_female.deselect()
	ent_mobile_add.delete(0, END)

def add_member_win():
	global ent_gender_add_male
	global ent_gender_add_female
	global ent_rollno_add
	global ent_name_add
	global ent_class_add
	global ent_mobile_add
	global gender_var
	global win_add_member
	
	win_add_member = Tk()
	win_add_member.title("Add A Member")
	win_add_member.option_add('*Font','MiClock\ ExtraLight 8')
	
	frm_ent_data = LabelFrame(win_add_member, text = "Enter Details")
	frm_ent_data.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	frm_buttons = Frame(win_add_member)
	frm_buttons.pack(padx = 10, pady = 10, ipadx = 10, ipady = 10)
	
	lbl_rollno_add = Label(frm_ent_data, text = "Enter Roll No: ")
	lbl_rollno_add.grid(row = 0, column = 0, padx = 10, pady = 10)
	ent_rollno_add = Entry(frm_ent_data)
	ent_rollno_add.grid(row = 0, column = 1, padx = 10, pady = 10)
	
	lbl_name_add = Label(frm_ent_data, text = "Enter Name: ")
	lbl_name_add.grid(row = 1, column = 0, padx = 10, pady = 10)
	ent_name_add = Entry(frm_ent_data)
	ent_name_add.grid(row = 1, column = 1, padx = 10, pady = 10)
	
	lbl_class_add = Label(frm_ent_data, text = "Enter Class: ")
	lbl_class_add.grid(row = 2, column = 0, padx = 10, pady = 10)
	ent_class_add = Entry(frm_ent_data)
	ent_class_add.grid(row = 2, column = 1, padx = 10, pady = 10)
	
	gender_var = StringVar(frm_ent_data)
	
	lbl_gender_add = Label(frm_ent_data, text = "Enter Gender: ")
	lbl_gender_add.grid(row = 3, column = 0, padx = 10, pady = 10)
	ent_gender_add = Frame(frm_ent_data) 
	ent_gender_add.grid(row = 3, column = 1, padx = 10, pady = 10)
	
	ent_gender_add_male = Radiobutton(ent_gender_add, text = "Male", variable = gender_var, value = 'M')
	ent_gender_add_male.pack(anchor = W)
    
	ent_gender_add_female = Radiobutton(ent_gender_add, text = "Female", variable = gender_var, value = 'F')
	ent_gender_add_female.pack(anchor = W)
	
	lbl_mobile_add = Label(frm_ent_data, text = "Enter Mobile No: ")
	lbl_mobile_add.grid(row = 4, column = 0, padx = 10, pady = 10)
	ent_mobile_add = Entry(frm_ent_data)
	ent_mobile_add.grid(row = 4, column = 1, padx = 10, pady = 10)
	
	btn_clear_add = Button(frm_buttons,text = "Clear", command = clr_member, font = ("MiClock ExtraLight", 8, "bold"))
	btn_clear_add.grid(row = 0, column = 0, padx = 100, pady = 10)
	
	btn_submit_add = Button(frm_buttons, text = "Submit", command = add_member, font = ("MiClock ExtraLight", 8, "bold"))
	btn_submit_add.grid(row = 0, column = 1, padx = 100, pady = 10)
	
	win_add_member.mainloop()

##########################################

con = sql.connect(host = "localhost",
			      user = "",
			      passwd = "",
			      database = "test")

cursor = con.cursor()

#print(con.is_connected())

root = Tk()
root.geometry('3000x1500')
root.title("Library Management System - JNV Bhopal")

################################
#Title

Label(root,
         text = "J. N. V. Ratibad, Bhopal (M. P.)",
         font = ("Carrois Gothic SC", 30, "bold"),
         foreground = "royalblue").pack()

Label(root, text = "Computer Science Project - Library Management System",font = ("Source Sans Pro", 15, "bold"), fg = "#ff6a00").pack(pady = 40)
#Label(root, text = "Submitted By: Masoom Baccha  	 Guided By: Masoom Teacher",font = ("Source Sans Pro", 12), fg = "#ff6a00").pack()

nvsLogo = Image.open("logo.png")
renderNvsLogo = ImageTk.PhotoImage(nvsLogo)
img = Label(root, image=renderNvsLogo)
img.image = renderNvsLogo
img.pack()

#Main Window Frame
#########################################

frm_main = LabelFrame(root, text = "MAIN MENU", font = ("Source Sans Pro", 8))
frm_main.place(x= 1500, y = 1100, anchor = CENTER)

frm_member = LabelFrame(frm_main, text = "Members", font = ("Cutive Mono", 8))
frm_member.grid(row = 0, column = 0, padx = 20, pady = 20, ipadx = 20, ipady = 20)

frm_books = LabelFrame(frm_main, text = "Books", font = ("Cutive Mono", 8))
frm_books.grid(row = 0, column = 1, padx = 20, pady = 20, ipadx = 20, ipady = 20)

#########################################

#Contents Of Member Frame
#########################################

btn_add_member = Button(frm_member, text = "Add New Member", width = 17, bd = 3, command = add_member_win, font = ("MiClock ExtraLight", 8, "bold"))
btn_add_member.grid(row = 0, column = 0 ,padx = 10, pady = 10)

btn_show_member = Button(frm_member, text = "Show All Members", width = 17, bd = 3, command = show_members, font = ("MiClock ExtraLight", 8, "bold"))
btn_show_member.grid(row = 0, column = 1 ,padx = 10, pady = 10)

btn_update_member = Button(frm_member, text = "Update Member Details", width = 17, bd = 3, command = update_member_win_root, font = ("MiClock ExtraLight", 8, "bold"))
btn_update_member.grid(row = 1, column = 0 ,padx = 10, pady = 10)

btn_delete_member = Button(frm_member, text = "Delete A Member", width = 17, bd = 3, command = delete_member_win, font = ("MiClock ExtraLight", 8, "bold"))
btn_delete_member.grid(row = 1, column = 1 ,padx = 10, pady = 10)


######################################

#Contents Of Books Frame
#########################################

btn_add_book = Button(frm_books, text = "Add New Book", width = 17, bd = 3, font = ("MiClock ExtraLight", 8, "bold"))
btn_add_book.grid(row = 0, column = 0 ,padx = 10, pady = 10)

btn_show_book = Button(frm_books, text = "Show All Books", width = 17, bd = 3, font = ("MiClock ExtraLight", 8, "bold"))
btn_show_book.grid(row = 0, column = 1 ,padx = 10, pady = 10)

btn_update_book = Button(frm_books, text = "Update Book Details", width = 17, bd = 3, font = ("MiClock ExtraLight", 8, "bold"))
btn_update_book.grid(row = 1, column = 0 ,padx = 10, pady = 10)

btn_delete_book = Button(frm_books, text = "Delete A Book", width = 17, bd = 3, font = ("MiClock ExtraLight", 8, "bold"))
btn_delete_book.grid(row = 1, column = 1 ,padx = 10, pady = 10)


######################################


root.mainloop()
