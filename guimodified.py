import tkinter as tk
import os
import smtplib
from csv import DictWriter
from tkinter import ttk
win=tk.Tk()
win.title('Gui application with python')
name_label=ttk.Label(win,text='Enter your name')
name_label.grid(row=0,column=0,sticky=tk.W)

email_label=ttk.Label(win,text="Enter your email ID")
email_label.grid(row=1,column=0,sticky=tk.W)

age_label=ttk.Label(win,text="Enter your age")
age_label.grid(row=2,column=0,sticky=tk.W)

gender_label=ttk.Label(win,text="Select your gender")
gender_label.grid(row=3,column=0,sticky=tk.W)
                  
user_label=ttk.Label(win,text="Select your Profession")
user_label.grid(row=4,column=0,sticky=tk.W)

button=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=button,state='readonly')
gender_combobox['values']=('Male','Female','Other')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)

name=tk.StringVar()
name_box=ttk.Entry(win,width=16,textvariable=name)
name_box.grid(row=0,column=1)
name_box.focus()

email=tk.StringVar()
email_box=ttk.Entry(win,width=16,textvariable=email)
email_box.grid(row=1,column=1)

age=tk.StringVar()
age_box=ttk.Entry(win,width=16,textvariable=age)
age_box.grid(row=2,column=1)

radio=tk.StringVar()
radio_btn1=ttk.Radiobutton(win,text='Student',value='Student',variable=radio)
radio_btn1.grid(row=4,column=1)
radio_btn2=ttk.Radiobutton(win,text='Teacher',value='Teacher',variable=radio)
radio_btn2.grid(row=4,column=2)

check=tk.IntVar()
check_box=ttk.Checkbutton(win,text="Have You liked the application? ",variable=check)
check_box.grid(row=5,columnspan=3)

def action():
    uname=name.get()
    uemail=email.get()
    uage=age.get()
    ubutton=button.get()
    uradio=radio.get()
    if check.get()==0:
        subscribed='No'
    else:
        subscribed='Yes'
    with open('gui.csv','a',newline='') as f:
        reader=DictWriter(f,fieldnames=['Name','Email','Age','Gender','Profession','Subscription'])
        if os.stat('gui.csv').st_size==0:
            reader.writeheader()
        
        reader.writerow({
            'Name':uname,
            'Email':uemail,
            'Age':uage,
            'Gender':ubutton,
            'Profession':uradio,
            'Subscription':subscribed
            })
    name_box.delete(0,tk.END)
    age_box.delete(0,tk.END)
    email_box.delete(0,tk.END)
    message=f"Your name is {uname}\nYour age is {uage}\nYour gender is {ubutton}\nYou are a {uradio}\n Thankyou for giving feedback!!!"
    connection=smtplib.SMTP('smtp.gmail.com',587)
    connection.ehlo()
    connection.starttls()
    connection.login('sagarguptasargam123@gmail.com',"srg@2909")
    connection.sendmail('sagarguptasargam123@gmail.com',uemail,message)
   
submit_button=ttk.Button(win,width=16,text='Submit',command=action)
submit_button.grid(row=6,column=0)

submit_button.grid(row=6,column=0)

win.mainloop()
