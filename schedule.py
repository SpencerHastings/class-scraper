from tkinter import *
import sqlite3
import string
from byu.newcourses import grab_courses, grab_courses_dept

courses = grab_courses()
##########
##Frames##
##########
top = Tk()
top.geometry("800x500")
dept_frame = Frame(top, bg="red")
courses_frame = Frame(top, bg="blue")
selected_frame = Frame(top, bg="green")

########
##Dept##
########
dept_scroll = Scrollbar(dept_frame)
dept_list = Listbox(dept_frame, yscrollcommand = dept_scroll.set)
for dept in courses:
    dept_f = ''.join(c for c in str(dept) if c not in '}{\')(,')
    dept_list.insert(END, dept_f)
dept_scroll.config(command = dept_list.yview)

###########
##Courses##
###########
courses_scroll = Scrollbar(courses_frame)
courses_list = Listbox(courses_frame, yscrollcommand = courses_scroll.set)
courses_scroll.config(command = courses_list.yview)

############
##Selected##
############ 

selected_scroll = Scrollbar(selected_frame)
selected_list = Listbox(selected_frame, yscrollcommand = selected_scroll.set)
selected_scroll.config(command = selected_list.yview)

###########
##Buttons##
###########
def deptbutton():
    courses_list.delete(0, courses_list.size())
    department = dept_list.get(dept_list.curselection()[0])
    rows = grab_courses_dept(department)
    for row in rows:
        #row_f = ''.join(c for c in str(row) if c not in '}{\')(,')
        courses_list.insert(END, row)

def coursesbutton():
    item = courses_list.get(courses_list.curselection()[0])
    current = selected_list.get(0, END)
    if item not in current:
        selected_list.insert(END, item)

def selectedbutton():
    selected_list.delete(selected_list.curselection()[0])

def calculatecourses():
    return None

dept_button = Button(dept_frame, text = "Select Dept.", command = deptbutton)
courses_button = Button(courses_frame, text = "Add Course", command = coursesbutton)
selected_button = Button(selected_frame, text = "Remove Course", command = selectedbutton)
calculate_button = Button(top, text = "Calculate Courses", command = calculatecourses)

###########
##Packing##
###########

calculate_button.pack(side=BOTTOM, fill=X)

dept_frame.pack(side = LEFT, fill = BOTH)
dept_button.pack(side = TOP, fill = X)
dept_list.pack(side = LEFT, fill = BOTH, expand = 1)
dept_scroll.pack(side = RIGHT, fill = Y)

courses_frame.pack(side = LEFT, fill = BOTH, expand = 1)
courses_button.pack(side = TOP, fill = X)
courses_list.pack(side = LEFT, fill = BOTH, expand = 1)
courses_scroll.pack(side = RIGHT, fill = Y)

selected_frame.pack(side = LEFT, fill = BOTH)
selected_button.pack(side = TOP, fill = X)
selected_list.pack(side = LEFT, fill = BOTH, expand = 1)
selected_scroll.pack(side = RIGHT, fill = Y)

top.mainloop()