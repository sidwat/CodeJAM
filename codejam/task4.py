from tkinter import *
import csv
from smtplib import *

def action_of_button():
    global email
    global password
    global blood_group
    email=e.get()
    password=e2.get()
    blood_group=clicked.get()
    recipient=search(blood_group)
    send_mail(recipient,email,password)
    label=Label(root,text="message sent to all").grid(row=7,column=0)
    return
def search(bg):
    path=r'C:\Users\sidha\Desktop\democsvfile.csv'
    file=open(path)
    reader=csv.reader(file)
    header=next(reader)
    data=[row for row in reader]
    recipient=[]
    for i in data:
        if i[1]==bg:
            recipient.append(i[2])
    print(recipient)
    return recipient
def send_mail(recipient,email,password):
    message= "Dear sir, you are kindly requested to donate your blood for the sake of the life od Mohan, one of the suttabaaz"
    server=SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    for i in recipient:
        server.sendmail(email,recipient,message)
    server.quit()
    return 

root = Tk()
root.title("Task4")
root.geometry("400x400")
label1=Label(root,text="Welcome to this amazing app").grid(row=0,column=0)
label2=Label(root,text="""Just enter your credentials of your email
and the blood group you desire and I will mail the corresponding students
about the blood donation""").grid(row=1,column=0)
e=Entry(root,width=35,borderwidth=5)
e.insert(0,"Enter your email")
e.grid(row=3,padx=40,pady=20)
e2=Entry(root,width=35,borderwidth=5)
e2.insert(0,"Enter your password")
e2.grid(row=4,padx=40,pady=20)
clicked=StringVar()
clicked.set("Select the blood group")
dropdown=OptionMenu(root,clicked,"A+","A-","B+","B-","AB+","AB-","O+","O-")
dropdown.grid(row=5,padx=40,pady=20)
button=Button(root, text="Send emails",padx=10,pady=10,command=action_of_button).grid(row=6)

root.mainloop()
