#pedir numero al usuairo e indicar si es positivo, negativo o cero
for x in range (3):
    numero=int (input ("pedir numero"))
    if numero <0 :
        print ("negativo")
    elif numero == 0 :
        print ("cero")
    else :
         print ("positivo")