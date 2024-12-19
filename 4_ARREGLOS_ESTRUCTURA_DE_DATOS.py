#ARREGLOS UNIDIMENCIONALES
#ARREGLOS DE MAS DE UNA DIMENSION
#ARREGLOS  Y FUNCIONES
#ARREGLOS DE CARACTERES

#Enrique Martinez Luna

#/*
# * Escribe un programa que imprima los 50 primeros números de la sucesión
# * de Fibonacci empezando en 0.
# * - La serie Fibonacci se compone por una sucesión de números en
# *   la que el siguiente siempre es la suma de los dos anteriores.
# *   0, 1, 1, 2, 3, 5, 8, 13...
# */

fib = [0,1]

i = 0

a = 0

print (fib [-2])
print (fib [-1])

while i < 48 :

    aux = fib [a] + fib [a+1] 

    print(aux)

    fib.append(aux)

    i += 1

    a += 1




