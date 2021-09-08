import os
from textwrap import indent
from PyInquirer import prompt, Separator
import keyboard
from datetime import datetime
import json

from prompt_toolkit.shortcuts import clear
def clearsc():
    os.system('cls' if os.name == 'nt' else 'clear')
#-------------------------------Main Menu-------------------------------#
def main_menu():
    clearsc()
    print("-"*15,"Que desea hacer?","-"*15)
    questions = [
                    {
                    "type" : "list",
                    "qmark" : "=",
                    "name" : "opcion",
                    "message" : "(Use las flechas del teclado)",
                    "choices" : ["Ingresar pedido", "Ver registro de pedidos", "Salir"]
                    }    
                ]
    awnsers = prompt(questions)
    print(awnsers)
    if awnsers["opcion"] == "Salir":
        confirm_ex()
    elif awnsers["opcion"] == "Ver registro de pedidos":
        registro_de_pedidos()
    else:
        ingresar_pedido()
#-------------------------------Confirmar Salida-------------------------------#
def confirm_ex():
    clearsc()
    questions = [
                    {
                    "type" : "confirm",
                    "name" : "YorN",
                    "message" : "Esta seguro que desea salir?",
                    }    
                ]
    awnsers = prompt(questions)
    if awnsers["YorN"] == True:
        clearsc()
        os._exit(0)
    else:
        main_menu()
#-------------------------------Registro de Pedidos-------------------------------#
def registro_de_pedidos():
    clearsc()
    print("Funcion aun no implementada, presione <q> para volver.")
    while True:
            if keyboard.read_key() == "q":
                main_menu()
                break
#-------------------------------Ingresar Pedidos-------------------------------#
def ingresar_pedido():
    clearsc()
    while True:
        awnser = None
        questions = [
            {
                'type': 'checkbox',
                'qmark': '+',
                'message': '(<arriba>, <abajo> para mover la flecha, <espacio> para seleccionar, <a> para seleccionar todos, <i> para invertir la seleccion)',
                'name': 'productos',
                'choices': [ 
                    Separator('===Notebooks==='),
                    {
                        'name': '<01> NOTEBOOK BANGHO MAX L5                          $72990'
                    },
                    {
                        'name': '<02> NOTEBOOK ASUS ZENBOOK 14                        $159990'
                    },
                    {
                        'name': '<03> NOTEBOOK ASUS TUF GAMING F17                    $194990'
                    },
                    Separator('===Teclados==='),
                    {
                        'name': '<11> TECLADO GENIUS RS2 KB-118 SP BLACK              $949'
                    },
                    {
                        'name': '<12> TECLADO HYPERX ALLOY CORE RGB                   $4389'
                    },
                    {
                        'name': '<13> TECLADO CORSAIR RAPIDFIRE RGB MECANICO          $19890'
                    },
                    Separator('===Mouses==='),
                    {
                        'name': '<21> MOUSE INALAMBRICO TRUST YVI NEGRO               $790'
                    },
                    {
                        'name': '<22> MOUSE REDRAGON COBRA FPS M711 RGB               $3990'
                    },
                    {
                        'name': '<23> MOUSE GAMER HYPERX PULSEFIRE SURGE RGB          $4899'
                    },
                    Separator('===Auriculares==='),
                    {
                        'name': '<31> AURICULARES GENIUS HS-04SU C/MICROFONO          $1799'
                    },
                    {
                        'name': '<32> AURICULAR LOGITECH G332 G LEATHERETTE           $5485'
                    },
                    {
                        'name': '<33> AURICULAR HYPERX CLOUD ALPHA S 7.1 BLACK        $13799'
                    },
                    Separator('===Otros==='),
                    {
                        'name': '<41> MICROFONO LOGITECH BLUE SNOWBALL WHITE          $7999'
                    },
                    {
                        'name': '<42> WEBCAM LOOSAFE 1080P 1/2 CMOS USB C/TRIPODE     $4999'
                    },
                    {
                        'name': '<43> IMPRESORA LASER NEGRO HP M107A LASERJET         $17999'
                    },
                ],
            }
        ]
        awnser = prompt(questions)
        if awnser["productos"] == []:
            clearsc()
            print("Usted debe seleccionar al menos un producto, presione <q> para continuar.")
            while True:
                if keyboard.read_key() == "q":
                    main_menu()
                    break
        else:
            clearsc()
            break
    orden = [],[] #Filtrar codigos de productos
    cant_p = len(awnser["productos"])
    for x in range(cant_p):
        cdp = awnser["productos"][x][1:3]
        orden[0].append(cdp)
    suma = 0
    for i in range(cant_p): #Añadir precios al arreglo 
        x = int(orden[0][i])
        if x == 1:
            suma = suma+72990
            orden[1].append(72990)
        elif x == 2:
            suma = suma+159990
            orden[1].append(159990)
        elif x == 3:
            suma = suma+194990
            orden[1].append(194990)
        elif x == 11:
            suma = suma+949
            orden[1].append(949)
        elif x == 12:
            suma = suma+4389
            orden[1].append(4389)
        elif x == 13:
            suma = suma+19890
            orden[1].append(19890)
        elif x == 21:
            suma = suma+790
            orden[1].append(790)
        elif x == 22:
            suma = suma+3990
            orden[1].append(3990)
        elif x == 23:
            suma = suma+4899
            orden[1].append(4899)
        elif x == 31:
            suma = suma+1799
            orden[1].append(1799)
        elif x == 32:
            suma = suma+5485
            orden[1].append(5485)
        elif x == 33:
            suma = suma+13799
            orden[1].append(13799)
        elif x == 41:
            suma = suma+7999
            orden[1].append(7999)
        elif x == 42:
            suma = suma+4999
            orden[1].append(4999)
        elif x == 43:
            suma = suma+17999
            orden[1].append(17999)
    for i in range(cant_p): # Añadir productos al arreglo
        x = int(orden[0][i])
        if x == 1:
            orden[0].append("NOTEBOOK BANGHO MAX L5")
        elif x == 2:
            orden[0].append("NOTEBOOK ASUS ZENBOOK 14")
        elif x == 3:
            orden[0].append("NOTEBOOK ASUS TUF GAMING F17")
        elif x == 11:
            orden[0].append("TECLADO GENIUS RS2 KB-118 SP BLACK")
        elif x == 12:
            orden[0].append("TECLADO HYPERX ALLOY CORE RGB")
        elif x == 13:
            orden[0].append("TECLADO CORSAIR RAPIDFIRE RGB MECANICO")
        elif x == 21:
            orden[0].append("MOUSE INALAMBRICO TRUST YVI NEGRO")
        elif x == 22:
            orden[0].append("MOUSE REDRAGON COBRA FPS M711 RGB")
        elif x == 23:
            orden[0].append("MOUSE GAMER HYPERX PULSEFIRE SURGE RGB")
        elif x == 31:
            orden[0].append("AURICULARES GENIUS HS-04SU C/MICROFONO")
        elif x == 32:
            orden[0].append("AURICULAR LOGITECH G332 G LEATHERETTE")
        elif x == 33:
            orden[0].append("AURICULAR HYPERX CLOUD ALPHA S 7.1 BLACK")
        elif x == 41:
            orden[0].append("MICROFONO LOGITECH BLUE SNOWBALL WHITE")
        elif x == 42:
            orden[0].append("WEBCAM LOOSAFE 1080P 1/2 CMOS USB C/TRIPODE")
        elif x == 43:
            orden[0].append("IMPRESORA LASER NEGRO HP M107A LASERJET")
    for x in range(cant_p):
        orden[0].pop(0)
    fecha = pedir_fecha()
    clearsc()
    print("="*85)
    print("Orden Final:")
    print("="*85)
    for x in range(cant_p):
        print(orden[0][x]," "*(70-len(orden[0][x])),"$",orden[1][x])
    print("-"*85)
    print("Suma total:"," "*59,"$",suma)
    print("Fecha de entrega:"," "*53, fecha[0],"/",fecha[1],"/",fecha[2])
    print("="*85)
    questions = [
                    {
                    "type" : "confirm",
                    "name" : "YorN",
                    "message" : "Desea continuar?",
                    }    
                ]
    awnsers = prompt(questions)
    clearsc()
    if awnsers["YorN"] == True: # Transfromar pedido a diccionario
        ordenes = []
        orden_actual = {
            "productos" : orden[0],
            "precios" : orden[1],
            "precio_total" : suma,
            "fecha_de_entrega" : fecha[0]+"/"+fecha[1]+"/"+fecha[2]
        }
       # with open("pedidos.json", "a") as f:
        print("Pedido almacenado, presione <q> para contiunar")
        while True:
            if keyboard.read_key() == "q":
                main_menu()
                break
    else:
        main_menu()
#-------------------------------Pedir Fecha de Entrega-------------------------------#
def pedir_fecha():
    year = datetime.now().year
    while True:
        try:
            aux = input("Ingrese la fecha de entrega del pedido: <dd/mm/yyyy o dd-mm-yyyy>")
            fecha = aux.split("-")
            int(fecha[0])
        except ValueError:
            try:
                fecha = aux.split("/")
                int(fecha[0])
            except ValueError:
                print("Fecha o formato invalido.")
            else:
                try:
                    for x in range(3):
                        a = fecha[x]
                except IndexError:
                    print("Fecha o formato invalido.")
                else:
                    if int(fecha[0]) > 31:
                        print("Fecha o formato invalido.")
                    elif int(fecha[1]) > 12 or fecha[1] == None:
                        print("Fecha o formato invalido.")
                    elif int(fecha[2]) < year or fecha[2] == None:
                        print("Fecha o formato invalido.")
                    else:
                        break
        else:
            try:
                for x in range(3):
                    a = fecha[x]
            except IndexError:
                print("Fecha o formato invalido.")
            else:
                if int(fecha[0]) > 31:
                    print("Fecha o formato invalido.")
                elif int(fecha[1]) > 12 or fecha[1] == None:
                    print("Fecha o formato invalido.")
                elif int(fecha[2]) < year or fecha[2] == None:
                    print("Fecha o formato invalido.")
                else:
                    break
    return fecha
