def creartxt():
    archi=open('3.txt','w')
    archi.close()

def escribir():
    archi = open('3.txt', 'a')
    lista = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']]
    print("0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22")
    print("T R W A G M Y F P D X  B  N  J  Z  S  Q  V  H  L  C  K  E")
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        print(lista[1][0])
    elif numero == 1:
        print('El valor en letra del numero ingresado es:',lista[1][1])
    elif numero == 2:
        print('El valor en letra del numero ingresado es:',lista[1][2])
    elif numero == 3:
        print('El valor en letra del numero ingresado es:',lista[1][3])
    elif numero == 4:
        print('El valor en letra del numero ingresado es:',lista[1][4])
    elif numero == 5:
        print('El valor en letra del numero ingresado es:',lista[1][5])
    elif numero == 6:
        print('El valor en letra del numero ingresado es:',lista[1][6])
    elif numero == 7:
        print('El valor en letra del numero ingresado es:',lista[1][7])
    elif numero == 8:
        print('El valor en letra del numero ingresado es:',lista[1][8])
    elif numero == 9:
        print('El valor en letra del numero ingresado es:',lista[1][9])
    elif numero == 10:
        print('El valor en letra del numero ingresado es:',lista[1][10])
    elif numero == 11:
        print('El valor en letra del numero ingresado es:',lista[1][11])
    elif numero == 12:
        print('El valor en letra del numero ingresado es:',lista[1][12])
    elif numero == 13:
        print('El valor en letra del numero ingresado es:',lista[1][13])
    elif numero == 14:
        print('El valor en letra del numero ingresado es:',lista[1][14])
    elif numero == 15:
        print('El valor en letra del numero ingresado es:',lista[1][15])
    elif numero == 16:
        print('El valor en letra del numero ingresado es:',lista[1][16])
    elif numero == 17:
        print('El valor en letra del numero ingresado es:',lista[1][17])
    elif numero == 18:
        print('El valor en letra del numero ingresado es:',lista[1][18])
    elif numero == 19:
        print('El valor en letra del numero ingresado es:',lista[1][19])
    elif numero == 20:
        print('El valor en letra del numero ingresado es:',lista[1][20])
    elif numero == 21:
        print('El valor en letra del numero ingresado es:',lista[1][21])
    elif numero == 22:
        print('El valor en letra del numero ingresado es:',lista[1][22])

    else:
        print("Ese numero no existe en la lista de listas")



creartxt()
escribir()

