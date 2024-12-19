#FUNCIONES DEFINIDAS POR EL USUARIO
#UTILIZACION DE LOS ARGUMENTOS Y PARAMETROS
#PASO DE VARIABLES POR VALOR


#Enrique Martinez Luna

"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.

"""
def main():
    
    area = 0
    print("ingresa la medida de la base en cm")
    base = int ( input() )
    print("ingresa la medida de la altura en cm")
    altura = int ( input() )
    print("ingresa el numbre del poligono las figuras soportadas son : triangulo, cuadrado y rectangulo")
    tipo = str ( input() )
    poligono(tipo,base,altura)

def poligono(tipo,base,altura): 

    if tipo == "triangulo" :
        area = base * altura / 2
        print("el area del triangulo es : ", area)
    
    elif tipo == "cuadrado" :
        area = base * altura
        print("el area del cuadrado es : ", area)

    elif tipo == "rectangulo" :
        area = base * altura
        print("el area del rectangulo es : ", area)
    pass

main()
