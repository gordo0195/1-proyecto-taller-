#juego 2048 por marco picado m.
about_1 ="""
___________________________________________
+    Instituto Tecnologico de Costa Rica   +      
+         Computer Engineering             +
+         Taller de programación           +
+    Primer Proyecto Programado 1s 2019    +      
+                                          + 
+          Prof. Msc Pedro Gutierrez       +             
+         Taller de Programación           +           
+            Juego de 2048                 +              
+                                          +
+         Marco Picado Monestel            +
+           Carnet:2018310184              +
+   Fecha de emision: 02/04/2019           +
+    Ultima modificación: 30/04/2019       +
+            Version: 0.0.1                +              
____________________________________________
"""
#########################BIBLIOTECAS##########################
from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import random

lista=[]

def guardar():
    name = id_gamer.get()
    lista.append(name + '\'t' +"Score")
    escribir_jugador()
    messagebox.showinfo("Guardado", "Jugador añadido a tabla de scores")
    id_gamer.set("")
    consultar()

    

#############################Cargar imagenes###################
def cargarImg(nombre):
    """recibe una imagen que carga desde la ruta especificada
       entradas: Nombre de la imagen que se quiera cargar
       salidas: imagen que se cargó
       restricciones: solo recibe un nombre dado desde otra función.
       """
       
    ruta=os.path.join('imag',nombre)
    imagen=PhotoImage(file=ruta)
    return imagen



def algo():
    print (id_gamer.get())

def seleccionar_operacion():
    def operacion():
            if opcion.get()==1:
                return seleccion_base()
            elif opcion.get()==2:
                return seleccion_base()
            else:
                messagebox.showerror("Error", "Se debe seleccionar una operacion. Intentalo de nuevo")
    if id_gamer.get()=="":
        messagebox.showerror("Error", "Se debe ingresar al menos un caracter para logear")
    else:
        ventana_seleccion1 = Toplevel()
        ventana_seleccion1.title("Selección de operación.")
        ventana_seleccion1.minsize(300,300)
        ventana_seleccion1.resizable(width=NO, height=NO)
        ventana_seleccion1.config(bg="light blue")

        label1 = Label(ventana_seleccion1, text="Selecciona una operación:", fg="white", bg="light blue", font=("console",16)).place(x=10, y=30)
        multi = Radiobutton(ventana_seleccion1, text="Multiplicación",value=1, variable=opcion, bg="light blue").place(x=20, y=100)
        suma = Radiobutton(ventana_seleccion1, text="Suma",value=2, variable=opcion, bg="light blue").place(x=20, y=150)
        continuar = Button(ventana_seleccion1, text="Continuar", command=operacion, bg="blue", activebackground="yellow")
        continuar.place(x=210, y=240)
        atras = Button(ventana_seleccion1, text="Atras", command=ventana_seleccion1.destroy,bg='blue', activebackground="yellow").place(x=10, y=240)

        
        
            


def seleccion_base():
    def Base():
        if (opcion1.get()==7) or (opcion1.get()==8) or(opcion1.get()==9) or (opcion1.get()==10):
            return ventana_juego()
        else:
            messagebox.showerror("Error!!!", "Debes seleccionar una base")
    ventana_base = Toplevel()
    ventana_base.title("Seleccion de Base Numerica")
    ventana_base.minsize(300,300)
    ventana_base.resizable(width=NO, height=NO)
    ventana_base.config(bg="light blue")

    etiquetaT = Label(ventana_base, text="Selecciona una \n Base Numerica:", fg="white", bg="light blue", font=("console",16)).place(x=10, y=10)
    binaria = Radiobutton(ventana_base, text="Binaria",value=7, variable=opcion1, bg="light blue").place(x=30, y=150)
    octal = Radiobutton(ventana_base, text="Octal",value=8, variable=opcion1, bg="light blue").place(x=30, y=200)
    decimal = Radiobutton(ventana_base, text="Decimal",value=9, variable=opcion1, bg="light blue").place(x=150, y=150)
    hexa = Radiobutton(ventana_base, text="Hexadecimal",value=10, variable=opcion1, bg="light blue").place(x=150, y=200)
    conti= Button(ventana_base, text="Continuar", command=Base, bg="blue", activebackground="yellow").place(x=200, y=250)
    iatras = Button(ventana_base, text="Atras", command=ventana_base.destroy,bg='blue', activebackground="yellow").place(x=10, y=250)


    
def ventana_about():
    """Función que crea la ventana de about
    entradas: no tiene argumentos pero recibe la orden desde el botón de pantalla principal
    salidas: ventana de about
    restricciones: solo ejecuta la ventana about
    """
    ventana2=Toplevel()
    ventana2.title("Acerca de este sotfware:")
    ventana2.minsize(800,500)
    ventana2.resizable(width=NO, height=NO)
    c_ventana2 = Canvas(ventana2, width=800, height=500, bg="light green").place(x=0, y=0)
    e_ventana2 = Label(ventana2, text=about_1, font=("Agency FB", 20)).place(x=115, y=30)

    foto=cargarImg('mi_foto.gif')
    F_about=Label(ventana2, image=foto,bg='light blue')
    F_about.photo=foto
    F_about.place(x=0,y=0)

    btn_atras=Button(ventana2, text="ATRAS", command=ventana2.destroy,bg='blue', activebackground="yellow")
    btn_atras.place(x=10,y=450)
    
def ventana_juego():
    """
    inicializa la ventana de juego
    entradas: llamada desde la función "empezar_juego"
    salidas: ventana de juego y todas sus dependencias
    restricciones: solo inicia desde la ventana inicial
    """
    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    b="0"
    def cuadrícula(b):
        return cuadriAux(matriz, 0, 0, b) 

    def cuadriAux(matriz, n, y, b):
        if n == 0:
            if y <= len(matriz[n])-1:
                matriz[n][y] = Label(frame1, text=b, bg="black", fg="white", font=("Gothic", 66), borderwidth="10", relief="groove").grid(row=n, column=y)
                return cuadriAux(matriz, n, y+1, b)
            else:
                return cuadriAux(matriz, n+1, 0, b)
            
        elif n <= 3:
            if y <= len(matriz[n])-1:
                matriz[n][y] = Label(frame1, text=b, bg="black", fg="white", font=("Gothic", 66), borderwidth="10", relief="groove").grid(row=n, column=y)
                return cuadriAux(matriz, n, y+1, b)
            else:
                return cuadriAux(matriz, n+1, 0, b)
        else:
            print("buuuuuuuuug")


    def movimientos(a):
        if a.bind("<Up>"):
            print("arriba")

        elif a.blind("<Down>"):
            print("Abajo")
            
        elif a.blind("<Left>"):
            print("izquierda")

        elif a.blind("<Right>"):
            print("Derecha")
        else:
            return movimientos(a)
        
            #master.bind("<Up>", self.arriba)
            #master.blind("<Down>", self.abajo)
            #master.blind("<Left>", self.izquierda)
            #master.blind("<Right>", self.derecha)
            
        
        

    """def asigna(matriz, b):
        i=random.randint(0, 3)
        j=ramdom.randint(0, 3)
        if matriz[i][j] == b:
            matriz[i][j] = Label(frame1, text=b, bg="black", fg="white", font=("Gothic", 66), borderwidth="10", relief="groove").grid(row=n, column=y)
            if matriz[i][j]==0:
                matriz[i][j] = 2 
            elif matriz[i][j]==1:
                matriz[j][j] = 4
            
            else:
                return asigno(matriz)
        else:
            return asigno(matriz)"""

    
    ventana = Toplevel()
    ventana.title("2048 :)")
    ventana.geometry("800x500")
    ventana.resizable(width=NO, height=NO)

    #c_juego = Canvas(ventana, width=800, height=500, bg="white").place(x=0, y=0)
    frame1 = Frame(ventana, width=600, height=400)
    frame1.config(cursor="pirate")             
    frame1.config(bg="lightblue")
    frame1.pack(anchor = NW)
    frame1.config(relief = "sunken", bd = "15")

    cuadrícula(b)
    #movimientos(cuadricula(b))
    etiq=Label(ventana, text= "Juego de: ", bg="black", fg="white", font=("Gothic", 20)).place(x=500, y=20)
    etiq1=Label(ventana, text= id_gamer.get(), bg="black", fg="white", font=("Gothic", 20)).place(x=620, y=20)


    
root = Tk()
#VARIABLES GLOBALES:
id_gamer = StringVar()
opcion=IntVar()
opcion1=IntVar()
num=IntVar()
#Configuración de ventana principal:
root.title("2048 por Marco Picado M.")
root.geometry("800x500")
root.minsize(800,500)
root.resizable(width=NO, height=NO)
#Canva de la ventana principal:
C_root=Canvas(root, width=800, height=500, bg="white").place(x=0, y=0)
carg = cargarImg("principal.gif")#extraida de: https://www.ticbeat.com/tecnologias/5-graficos-de-statista-que-explican-el-boom-del-big-data/
imag_prin=Label(root,bg='white')
imag_prin.place(x=0,y=0)
imag_prin.config(image=carg)
##Widgets ventana principal
etiquetaTitulo = Label(root,text="2048",bg="blue",fg="white",font=("Console",56)).place(x=310,y=10)
puntajes = Label(root, text="Puntajes Altos", bg="blue", fg="white", font=("Console", 16)).place(x=10, y=20)
Caja_nombre = Entry(root, textvariable=id_gamer).place(x=620, y=20)
boton_nombre = Button(root, command=algo,text="Registrarme", background="blue", activebackground="yellow").place(x=685, y=50)
boton_acerca = Button(root, command= ventana_about, text="Acerca de:", background="blue", activebackground="yellow").place(x=100, y=450)
boton_juego = Button(root, command=seleccionar_operacion, text ="Iniciar Partida", background="blue", activebackground="yellow").place(x=550, y=450)

root.mainloop()
