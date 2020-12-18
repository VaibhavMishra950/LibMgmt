from tkinter import *
from tkinter import messagebox as mb
import mysql.connector as s
con = s.connect(host="localhost", user = "", passwd="", database = "test")
cursor = con.cursor()

def show_books():
    cursor.execute('select * from books')
    data = cursor.fetchall()
    count = cursor.rowcount
    
    win_show_books = Tk()
        
    cols = ["BOOK ID", "TITLE", "AUTHOR", "PAGES", "PRICE"]
    for c in range(5):
    	Label(win_show_books, text=cols[c], font=("Helvetica", 8, "bold")).grid(row=0, column=c, padx=8, pady = 15)
    for x in range(count):
    	for y in range(5):
    		l = Label(win_show_books, text = data[x][y])
    		l.grid(row = x+1, column = y, padx = 8, pady = 7, sticky = W, ipadx = 40)
    
    
    win_show_books.mainloop()

show_books()