class Fun_modulomatematicas:
    def __init__(self,listanum):
        self.lista=listanum

    def verificaprimo(self):
        for i in self.lista:
            if self.__verificarprimo(i):
                print('El elemento',i,'Si es un nro primo')
            else:
                print('El elemento',i,'No es un nro primo')
    
    def conviertegrados(self,origen,destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son',self.__conviertegrados(i, origen, destino),'grados',destino)

    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))
    
    def __verificarprimo(self,nro):
        es_primo = True  
        for i in range(2, nro):  
            if nro % i == 0:  
                es_primo = False  
                break  
        return es_primo
    
    def valor_modal(self,menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if menor:
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)

        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo
    
    def __conviertegrados(self,valor,origen,destino):
    
        resultado=0

        if origen=='Celsius':
            if destino=='Farenheit':
                resultado=(valor*9/5)+32
            
            elif destino=='Celsius':
                 resultado=valor
             
            else:
                 resultado=(valor+273.15)
             
        elif origen=='Farenheit':
            if destino=='Kelvin':
                resultado=(5/9*(valor-32)+273.15)
            
            elif destino=='Celsius':
                resultado=(valor-32)*5/9
            
            else:
                resultado=valor
        else:
            if destino=='Celsius':
                resultado=(valor-273.15)
            
            elif destino=='Farenheit':
                resultado=(1.8*(valor-273.15)+32)
            else:
                resultado=valor
                     
        return resultado
    
    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero