def creartxt ():
    archi=open('1.txt','w')
    archi.close()

def escribirtxt():
    b=0

    archi=open('1.txt','a')
    a = int(input("Ingrese el numero binario :"))

    for i in a:
        multi= a.find(len(a))*2
        multi+=b
        final= multi+i
        print()


creartxt()
escribirtxt()





