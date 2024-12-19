#INSTRUCCIONES TIPO IF,ELSE,IF-ELSEIF-ELSE,SELECT-CASE
#CICLOS TIPO FOR, WHILE, DO WHILE
#CICLOS ANIDADOS

#Enrique Martinez Luna

# Escribe un programa que muestre por consola (con un print) los
 #números de 1 a 100 (ambos incluidos y con un salto de línea entre
 #cada impresión), sustituyendo los siguientes:
 #- Múltiplos de 3 por la palabra "fizz".
 #- Múltiplos de 5 por la palabra "buzz".
 #- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"." "

X = 1

while X < 101 :
    
    if X%3 == 0 and X%5 == 0 :

        print ("fizzbuzz")
        X += 1

    else :

        if X%3 == 0 :
            print("fizz")
            X += 1

        elif X%5 == 0 :
            print ("buzz")
            X += 1   
        
        else :
            print (X)
            X += 1

