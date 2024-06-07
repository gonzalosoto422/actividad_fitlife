import os 
import msvcrt
import csv

#funcion para crear titulos
def titulo(texto):
    print(f"\033[33m{texto.upper()}]0\33[0m")

def error(texto : str):
      print(f"\033[31m{texto.upper()}]0\33[0m")

#tuplas - clases
clases = [
    ("pesas","LUN-MIE 8:30-10:00 a.m",10),
    ("zumba","MAR-JUE 3:30-5.40 p.m",20),
    ("nutrucion","VIE 6:00-7:30 a.m",2),
    ("crossfit","SAB 11:30-12:50 p.m",10)
]
#diccionario -usuario
usuarios = {}
#lista-reserva
reserva = []
#comenzamos el sistema
while True:
    print("<<press any key>>")
    msvcrt.getch()
    os.system("cls")
    print("""\033[32
    sistema de gestion fitlife
    ************************\033m[0m
    1) registro usuario
    2) reservar clase
    3) consultar clases disponibles
    4) consultar clases de usuario
    5) consultar usuarios
    0) salir
    \033[32m============================\033[0m""")
    opcion = input("seleccione :")
    if opcion=="0":
        titulo("adios")
        nombre = input("ingrese nombre de usurio :").title()
        #validar que nombre de usuario no se repita
        if nombre not in usuario.value():
            usuarios[numero_usuario] = nombre
            numero_usuario+100
            exito("usuario registrado")
        else: 
            error("usuario ya registrado")
    elif opcion=="1":
        titulo("registrar usuario")
    elif opcion=="2":
        titulo("reservar clases")
        codigo = int(input("ingrese codigo de usuario"))
        if codigo in usuarios:
            curso = input("ingrese curso para inscribir :").capitalize()
            centinelacurso = False
            for c in clases:
                if c[0].capitalize() == curso:
                    centinelacurso = True
                    if c[2]>0: #verificamos si hay cupos
                        centinelacupos = True
                        #realizar la reserva
                        reserva.append(codigo,usuario[codigo],c[0],c[1])
                        exito("Reserva realizada")
                        #descontar cupo
                        actualizacioncupo = (c[0],c[1],c[2]-1)
                        clases.remove(c)
                        clases.append(actualizacioncupo)
    elif opcion=="3":
        titulo("consultar clases diponibles")
    elif opcion=="4":
        titulo("consultar reseva de usuario")
    elif opcion=="5":
        titulo("")
