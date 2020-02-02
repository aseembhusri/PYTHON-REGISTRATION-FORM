from tkinter import *
import sqlite3


def save_info():
    firstname_info = firstname.get()
    lastname_info = lastname.get()
    age_info = age.get()
    age_info = str(age_info)
    rollno_info=rollno.get()
    rollno_info=str(rollno_info)
    print(firstname_info,lastname_info,age_info,rollno_info,)
    conn=sqlite3.connect('Form.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS student(Firstname TEXT,Lastname TEXT,Age integer(20),Roll integer(20))')
        cursor.execute('INSERT INTO student(Firstname,Lastname,Age,Roll) Values(?,?,?,?)',(firstname_info,lastname_info,age_info,rollno_info,))
        conn.commit()

    

    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    age_entry.delete(0, END)
    rollno_entry.delete(0,END)
    




screen=Tk()
screen.geometry("500x500")
screen.title("Python Form")
heading = Label(text = "Python Form", bg="red",width="500",height="2")
heading.pack()

firstname_text = Label(text = "Firstname * ",)
lastname_text = Label(text = "Lastname * ",)
age_text = Label(text = "Age * ",)
rollno_text=Label(text="Roll * ",)


firstname_text.place(x= 15, y=70)
lastname_text.place(x= 15, y=140)
age_text.place(x= 15, y=210)
rollno_text.place(x=15,y=280)


firstname= StringVar()
lastname= StringVar()
age= IntVar()
rollno=IntVar()


firstname_entry = Entry (textvariable = firstname, width ="30")
lastname_entry = Entry (textvariable = lastname, width ="30")
age_entry = Entry (textvariable = age, width ="30")
rollno_entry =Entry(textvariable=rollno,width="30")


firstname_entry.pack()
lastname_entry.pack()
age_entry.pack()
rollno_entry.pack()

firstname_entry.place(x=15, y=100)
lastname_entry.place(x=15,y=180)
age_entry.place(x=15, y=240)
rollno_entry.place(x=15,y=300)

register =Button(text= "Register",width="40",height="2",command = save_info, bg="grey")
register.place(x=0,y=350)






