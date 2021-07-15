
listadepuracion=[[10.103,-74.902],
                 [10.115,-75.085],
                 [10.108,-74.801]]

def ImprimirCoordenads(listaoriginal):
    
    listaduplicada=list(listaoriginal)
    print("Las coordenadas guardadas actualmente son: ")
    #creamos un for que pasará imprimiendo la sublista X ambas posiciones
    for x in range(0,len(listaduplicada)):
        print(f"{x+1}. Coordenada Latitud:'{[listaduplicada[x][0]]}' Longitud: '{[listaduplicada[x][1]]}'")

ImprimirCoordenads(listadepuracion)