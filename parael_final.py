"""
#ejercicio 2
#. Dene una función que convierta grados centígrados en grados Farenheit
def faren(cen):
    far=9/5*cen+32
    return (far)
#ejercicio 3
#Define una función llamada areaCirculo que,a partir del radio de
#uncírculo, devuelva el valor de su área. Utiliza el valor 3.1416

#como aproximación de π o importa el valor del módulo math
from math import pi
def areacirculo(radio):
    return (pi*radio**2)
#ejercicio 4
#crear una funcion para saber si un alumno está desaprobado.
def estaaprob(nota):
    if nota>10.5:
        resultado=True
    else:
        resultado=False

#5. Dseñar una función que nos diga si un número dado es o no es perfecto.
#Se dice que un número es perfecto si es igual a la suma de todos sus
#divisores excluído él mismo. Por ejemplo, 28 es un número perfecto, pues
#sus divisores (excepto él mismo) son 1, 2, 4, 7 y 14, que suman 28.
    
def es_perfecto(numero):
    suma=0
    for i in range(1,numero):
        if numero%i==0:
            suma+=i
            resultado=True
    return("la suma es: ",suma,"y el numero es: ",resultado)

def es_perfecto(numero):
    suma = 0
    for i in range(1,numero):
        if numero % i ==0:
            suma = suma+i
    return suma==numero

#crear una funcion que sume los elementos de una lista.
def suml(lista):
    suma=0
    for i in lista:
        suma+=i
    return(suma)
#Diseñe una función que recibe una lista de números y devuelve el valor de su mayor elemento.
def mayornum(lista):
    mayor=0
    for elem in lista:
        if elem>mayor:
            mayor=elem
    return mayor

#9. Diseña una función que reciba una lista de números y devuelva la media
#de dichos números. ¿qué pasa si el usuario ingresa una lista vacía?    
def calmedia(lista):
    suma=0
    cont=0
    for i in lista:
        if len(lista)==0:
            print(None)
        if len(lista)>0:
            suma+=i
            cont+=1
    return(suma/cont)
       
#10. Diseña una función que calcule el producto de todos los números que componen una lista.
def producto(lista):
    prod=1
    for elem in lista:
        prod*=elem
    return(prod)

#17. Diseña una función que reciba una lista de enteros y devuelva los números mínimo y máximo de la lista simultáneamente.

def mayor_menor(lista):
    mayor=0
    minimo=lista[0]
    for elem in lista:
        if elem>mayor:
            mayor=elem
        if elem<minimo:
            minimo=elem
    return (mayor,minimo)
"""
def heapsort(lista,tam):
    for k in range(tam-1,-1,-1):
        for i in range(0,k):
            item=lista[i]
            j=(i+1)/2
            while j>=0 and lista[j]<item:
                lista[i]=lista[j]
                i=j
                j=j/2
            lista[i]=item
        temp=lista[0];
    lista[0]=lista[k];
    lista[k]=temp;
 
def imprimeLista(lista,tam):
    for i in range(0,tam):
        print (lista[i])
 
def leeLista():
    lista=[]
    cn=int(input("Cantidad de numeros a ingresar: "))
 
    for i in range(0,cn):
        lista.append(int(input("Ingrese numero %d : " % i)))
    return lista
 
A=leeLista()
heapsort(A,len(A))
imprimeLista(A,len(A))













































































































































































