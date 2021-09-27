import random 
def loadFromFile(name):
    ''' 
        Recibe el nombre de un archivo (str)
        Retorna una lista de floats con cada uno 
        de los números extraídos del archivo name
    '''
    pass

def sortBurbuja(L):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de burbuja
        para ordenar la lista L
    '''
    flag = False 
    while flag == False:
        flag = True 
        for i in range(len(L)-1): 
            if L[i] > L[i +1]:
                aux = L[i]
                L[i] = L[i+1]
                L[i+1]= aux
                flag = False 
    return 


def sortSeleccion(L):
    ''' 
        Recibe una lista de floats
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de selección
        para ordenar la lista L
    '''
    lenght  = len  (L)
    for i in range(lenght-1):
        less= i
        for j in range(i+1,lenght):
            if L[j] < L[less]:
                less = j
                
        aux = L[less]
        L[less] = L[i]
        L[i] = aux

    return 




def createRandomList(size, minimo, maximo):
    '''
    Retorna un lista de size números aleatorios. Cada elemento de la lista debe 
    estar en el rango [minimo, maximo]
    
    Parámetros
        n: cantidad de elementos a poner en la lista
        minimo: número mínimo que puede haber en la lista
        maximo: número máximo que puede haber en la lista
    '''
    random.randint(minimo,maximo)
    



