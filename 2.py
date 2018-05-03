def creartxt():
    archi=open('2.txt','w')
    archi.close()

def escribirtxt():

    archi = open('2.txt','a')
    mensaje='Bienvenido a python'

    print(mensaje[18]+mensaje[17]+mensaje[16]+mensaje[15]+mensaje[14]+mensaje[13]+mensaje[12]+mensaje[11]+mensaje[10]+mensaje[9]+mensaje[8]+mensaje[7]+mensaje[6]+mensaje[5]+mensaje[4]+mensaje[3]+mensaje[2]+mensaje[1]+mensaje[0] )
    archi.close()
creartxt()
escribirtxt()

