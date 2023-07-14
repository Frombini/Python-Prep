import sys
if len(sys.argv)==2:
    import datetime
    import os
    marca_de_timepo = datetime.datetime.now()
    marca_de_timepo =int(datetime.datetime.timestamp(marca_de_timepo))

    lluvia=sys.argv[1]
    temperatura= input('ingrese la temperatura en grados centigrados')
    humedad= input('ingrese el porcentaje de humedad')
    linea=str(marca_de_timepo)+','+temperatura+','+humedad+','+lluvia

    logs_lluvia=open('clase09_ej2.csv','a')
    logs_lluvia.write(linea+'\n')
    logs_lluvia.close


else:
    print('ERROR: introdujo una cantidad de argumentos distinta de tres(3)')
    print('Ejemplo: clase09_ej2.py <temperatura> <humedad> <True o Flase>')