#!/usr/bin/env python
#-*- coding: utf-8 -*-
from Tkinter import *
from gettext import gettext
import datetime
from ttk import Combobox

def procesar():
    totalPans = PrecioPans * PansCan.get()
    print totalPans
    totalPlayDep = PrecioPlayDep * PlayCan.get()
    print totalPlayDep
    totalPlayDia = PrecioPlayDia * PlayDCan.get()
    print totalPlayDia
    totalChaleco = PrecioChaleco * ChalCan.get()
    print totalChaleco
    total = totalPans+totalPlayDep+totalPlayDia+totalChaleco
    print total
    
ventana = Tk()

Fecha = datetime.datetime.now()
Nombre = StringVar()
PrecioPans = 230
PrecioPlayDep= 110
PrecioPlayDia = 110
PrecioChaleco =150
PansCan = IntVar()
PlayCan = IntVar()
PlayDCan = IntVar()
ChalCan = IntVar()
totalPans= IntVar()
totalPlayDep=IntVar()
totalPlayDia = IntVar()
totalChaleco =IntVar()
total = IntVar()
var = IntVar()

ventana.title=('Nuevo Apartado')

fecha = Label(ventana, text=Fecha)
fecha.grid(row=1, column=1)

nombre = Label(ventana, text='Nombre')
Nombre=Entry(ventana,textvariable=Nombre)
nombre.grid(row=2,column=1)
Nombre.grid(row=3,column=1)

escuela = Label(ventana, text='Selecciona la escuela')
Escuela = Combobox(ventana)
escuela.grid(row=4, column=1)
Escuela.grid(row=5,column=1)
Escuela ["values"] = ["5 de Febrero Mat", "5 de Febrero Vesp", "Francisco Lozornio", "Ma. Elena Zapata"]

Pedido = Label(ventana, text='Pedido')
Pedido.grid(row=7, column=1)
Precio = Label(ventana, text='Precio')
Precio.grid(row=7, column=2)
Talla = Label(ventana, text='Talla')
Talla.grid(row=7, column=3)
Cantidad = Label(ventana, text='Cantidad')
Cantidad.grid(row=7, column=4)
Estatus = Label(ventana, text='Estatus')
Estatus.grid(row=7, column=5)
Total = Label(ventana, text='Total')
Total.grid(row=7, column=7)

pans = Label(ventana,text='Pans')
PansP = Label(ventana, text=PrecioPans)
PansT = Combobox(ventana)
PansCant = Entry(ventana, textvariable=PansCan)
PansOk = Radiobutton(ventana, text='ok')
PansNo = Radiobutton(ventana, text='no')
PansTotal = Label(ventana, textvariable=totalPans)
pans.grid(row=8, column=1)
PansP.grid(row=8, column=2)
PansT.grid(row=8, column=3)
PansT ["values"] = ["3", "4", "6", "8","10","12","14"]
PansCant.grid(row=8, column=4)    
#PansCant ["values"] = ["1","2","3","4","5","6","7","8","9","10"]
PansOk.grid(row=8,column=5)
PansNo.grid(row=8,column=6)
PansTotal.grid(row=8,column=7)    

playeraDep = Label(ventana,text='Playera Deportiva')
PlayeraP = Label(ventana, text=PrecioPlayDep)
PlayeraT = Combobox(ventana)
PlayeraCant = Entry(ventana, textvariable=PlayCan)
PlayeraOk = Radiobutton(ventana, text='ok')
PlayeraNo = Radiobutton(ventana, text='no')
PlayeraTotal = Label(ventana, textvariable=totalPlayDep)
playeraDep.grid(row=9, column=1)
PlayeraP.grid(row=9, column=2)
PlayeraT.grid(row=9, column=3)
PlayeraT ["values"] = ["3", "4", "6", "8","10","12","14"]
PlayeraCant.grid(row=9, column=4)
#PlayeraCant ["values"] = ["1","2","3","4","5","6","7","8","9","10"]
PlayeraOk.grid(row=9,column=5)
PlayeraNo.grid(row=9,column=6)
PlayeraTotal.grid(row=9,column=7)

playeraDia = Label(ventana,text='Playera Diario')
PlayP = Label(ventana, text='$110')
PlayT = Combobox(ventana)
PlayCant = Entry(ventana, textvariable=PlayDCan)
PlayOk = Radiobutton(ventana, text='ok')
PlayNo = Radiobutton(ventana, text='no')
PlayTotal = Label(ventana, textvariable=totalPlayDia)
playeraDia.grid(row=10, column=1)
PlayP.grid(row=10, column=2)
PlayT.grid(row=10, column=3)
PlayT ["values"] = ["3", "4", "6", "8","10","12","14"]
PlayCant.grid(row=10, column=4)
#PlayCant ["values"] = ["1","2","3","4","5","6","7","8","9","10"]
PlayOk.grid(row=10,column=5)
PlayNo.grid(row=10,column=6)
PlayTotal.grid(row=10,column=7)


chaleco = Label(ventana,text='Chaleco')
ChalecoP = Label(ventana, text='$130')
ChalecoT = Combobox(ventana)
ChalecoCant = Entry(ventana, textvariable=ChalCan)
ChalecoOk = Radiobutton(ventana, text='ok')
ChalecoNo = Radiobutton(ventana, text='no')
ChalecoTotal = Label(ventana, textvariable=totalChaleco)
chaleco.grid(row=11, column=1)
ChalecoP.grid(row=11, column=2)
ChalecoT.grid(row=11, column=3)
ChalecoT ["values"] = ["3", "4", "6", "8","10","12","14"]
ChalecoCant.grid(row=11, column=4)
#ChalecoCant ["values"] = ["1","2","3","4","5","6","7","8","9","10"]
ChalecoOk.grid(row=11,column=5)
ChalecoNo.grid(row=11,column=6)
ChalecoTotal.grid(row=11,column=7)

'''estatus_med = Label(ventana, text='Selecciona el estatus del producto')
entryEstatus_med1= Radiobutton(ventana, text="Option 1", variable=var, value=1,
                  command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(ventana, text="Option 2", variable=var, value=2,
                  command=sel)
R2.pack( anchor = W )

R3 = Radiobutton(ventana, text="Option 3", variable=var, value=3,
                  command=sel)
R3.pack( anchor = W)'''

Imprimir=Button(ventana,text='Imprimir', background="pink")
Imprimir.grid(row=12,column=6)

Guardar=Button(ventana,text='Guardar', command=procesar, background="pink")
Guardar.grid(row=12,column=7)

ventana.mainloop()
