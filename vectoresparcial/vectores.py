
from  array  import  array
from cProfile import label 
from  cgitb  import  text

from tkinter import * 
import  tkinter
from tkinter import messagebox as MessageBox 
from  webbrowser  import  get



array1=[2,3,6,8,9]
array2=[4,5.9,9,0]

def ingresarvectores():
    

    primero=int(vectora.get()) 
    segundo=int(vectorb.get()) 
    array1.append(primero) 
    array2.append(segundo) 
    print(array1,"ingreso") 
    print(array2,"ingreso")


def Sumarvectores(): 
    a=[]
    for  i  in  range(len(a)): 
    a.append(array1[i]+array2[i]) 
    print(a)


def  mostrarvectores(array1,array2): 
    print(array1)
    print(array2)

array1=[] 
array2=[]

root=Tk()

menubar=Menu(root) 
root.config(menu=menubar)


root.title('Vectores') 
root.geometry('650x450')

#Frames
frame1  =  LabelFrame(  text=  "Ingreso",  font=("calibri",  14)) 
frame3  =  LabelFrame(  text=  "Salida",  font=("calibri",  14))\

frame1.pack(fill="both",  expand="yes",  padx=10,  pady=10) 
frame3.pack(fill="both",  expand="yes",  padx=5,  pady=10)


# Etiquetas
label1  =  Label(root,  text='Ingrese  el  vector  a') 
label1.place(x=210,  y=30)
label2  =  Label(root,  text='Ingrese  el  vector  b') 
label2.place(x=210,  y=50)
label1  =  Label(root,  text='VECTORES',fg="white",bg="black",font=("Arial",25)).place(x=25,  y=150)

#vector 1 
name_var=StringVar
vectora  =  Entry(root,  textvariable=name_var) 
vectora.place(x=60,y=30)

#vector 2 
vectorb=StringVar
vectorb  =  Entry(root,  textvariable=name_var) 
vectorb.place(x=60,y=50)

frame3.config(cursor="pirate")

img  =tkinter.PhotoImage(file="vector1.png") 
fondo=Label(root,image=img).place(x=380,y=10)

#Botones
button_insert  =  Button(root,  text="  Ingresar  Vector  ",activebackground="black",activeforeground="red",bg="white",height=1, 
width=23,command=ingresarvectores).place(x=250,  y=375)
button_insert  =  Button(root,  text="  Sumar  Vectores  ",activebackground="black",activeforeground="red",bg="white",height=1, 
width=23,command=Sumarvectores).place(x=10,  y=375)
button_insert  =  Button(root,  text="  Borrar  Producto  ",activebackground="black",activeforeground="red",bg="white",height=1, 
width=23,command=mostrarvectores).place(x=470,  y=375)


filemenu=Menu(menubar) 
helpmenu=Menu(menubar)


menubar.add_cascade(label="Salida",menu=filemenu) 
menubar.add_cascade(label="Ayuda",menu=helpmenu)


filemenu.add_command(label="Salir",  command="salir") 
helpmenu.add_separator()

root.mainloop()

