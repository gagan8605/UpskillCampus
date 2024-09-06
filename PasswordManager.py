import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os
from tkinter import messagebox

window=Tk()
window.geometry("500x400")
window.resizable('false','false')
window.configure(bg="Darkcyan")

def decrypt(data):
    pas=[]
    data=data.strip("[")
    data=data.strip("]")
    data=data.split(",")
    for i in data:
        pas.append(int(int(i)/83))
    fpas=''.join(map(chr,pas))
    inputtxt3.insert(1.0,fpas)

    
def encrypt(text):
    ascii_values = []
    for character in text:
        ascii_values.append(83*ord(character))
    return ascii_values

def clear():
    inputtxt1.delete(1.0,'end')
    inputtxt2.delete(1.0,'end')
    inputtxt3.delete(1.0,'end')

    
def savepass():
    web=inputtxt1.get(1.0,"end-1c")
    email=inputtxt2.get(1.0,"end-1c")
    pasw=inputtxt3.get(1.0,"end-1c")
    pas=(encrypt(pasw))
    print(pas)
    resr=[]
    with open("SavedPassword.txt","r") as file:
        res=file.readlines()
        file.close
    for i in res:
        i=i.split("\n")
        resr.append(i[0])
    i=0    
    stat=0
    leng=len(res)
    while(i<leng):
        if(web==resr[i] and email==resr[i+1]):
            a_file=open("SavedPassword.txt","r")
            listofline=a_file.readlines()
            listofline[i+2]=str(pas)+"\n"
            a_file=open("SavedPassword.txt","w")
            a_file.writelines(listofline)
            a_file.close()
            stat=1
            messagebox.showinfo("Alert","New Password Updated")    
            break
        i+=3
    if(stat==0):
        with open("SavedPassword.txt","a") as file:
            file.write(f"{web}\n{email}\n{pas}\n")
            file.close 
            messagebox.showinfo("Success","New Password Saved")    
    inputtxt1.delete(1.0,'end')
    inputtxt2.delete(1.0,'end')
    inputtxt3.delete(1.0,'end')


    

def openpass():
    web=inputtxt1.get(1.0,"end-1c")
    email=inputtxt2.get(1.0,"end-1c")
    resr=[]
    with open("SavedPassword.txt","r") as file:
        res=file.readlines()
        file.close
    for i in res:
        i=i.split("\n")
        resr.append(i[0])
    i=0    
    stat=0
    leng=len(res)
    while(i<leng):
        if(web==resr[i] and email==resr[i+1]):
            inputtxt3.delete(1.0,'end')
            ##inputtxt3.insert(1.0,resr[i+2])
            decrypt(resr[i+2])
            stat=1
            break
        i+=3
    if(stat==0):
        inputtxt3.delete(1.0,'end')
        inputtxt3.insert(1.0,'No record')





b_savepass=Button(window,text="Save Password",height=2,width=20,bg="Brown",fg="white",command=savepass)
b_savepass.place(relx=0.5,rely=0.65,anchor=CENTER)

####################################COMPLETE###################################################################

b_openpass=Button(window,text="Open Saved Password",height=2,width=20,bg="brown",fg="white",command=openpass)
b_openpass.place(relx=0.5,rely=0.8,anchor=CENTER)

####################################COMPLETE###################################################################

b_clear=Button(window,text="Clear All",height=2,width=10,bg="brown",fg="white",command=clear)
b_clear.place(relx=0.9,rely=0.4,anchor=E)

####################################COMPLETE###################################################################

l1=Label(window,text="Developed By\nShreya Patil",font=("arial",10,"bold"))
l1.config(bg="Darkcyan")
l1.place(relx=0.9,rely=0.95,anchor=CENTER)

l2=Label(window,text="Password Manager",font=("arial",20,"bold"))
l2.config(bg="Darkcyan")
l2.place(relx=0.5,rely=0.1,anchor=CENTER)

#########################################################

inputtxt1 = tk.Text(window,height=1,width=20)
inputtxt1.place(relx=0.7,rely=0.3,anchor=E)

lbl1=tk.Label(window,text="Website",bg="Darkcyan",font=("arial",10,"bold"))
lbl1.place(relx=0.1,rely=0.3,anchor=W)

##########################################################

inputtxt2 = tk.Text(window,height=1,width=20)
inputtxt2.place(relx=0.7,rely=0.4,anchor=E)

lbl2=tk.Label(window,text="E-Mail",bg="Darkcyan",font=("arial",10,"bold"))
lbl2.place(relx=0.1,rely=0.4,anchor=W)

##########################################################

inputtxt3 = tk.Text(window,height=1,width=20)
inputtxt3.place(relx=0.7,rely=0.5,anchor=E)

lbl3=tk.Label(window,text="Password",bg="Darkcyan",font=("arial",10,"bold"))
lbl3.place(relx=0.1,rely=0.5,anchor=W)


window.mainloop()
