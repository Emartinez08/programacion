#DECLARACION DE APUNTADORES
#UTILIZACION DE APUNTADORES
#APUNTADORES Y ARREGLOS
#VALORES POR REFERENCIA DE FUNCIONES


#Enrique Martinez Luna

# Declaración y utilización de "apuntadores" (referencias)
def declaracion_y_utilizacion():
    x = 10
    y = x  # y "apunta" a x (referencia)
    
    print("Declaración y Utilización de Referencias:")
    print(f"Valor de x: {x}")
    print(f"Valor de y (refiere a x): {y}")
    
    y = 20  # Esto no afecta a x, ya que se crea una nueva referencia
    print(f"Nuevo valor de y: {y}")
    print(f"Valor de x permanece igual: {x}\n")

# Apuntadores y arreglos (listas en Python)
def apuntadores_y_arreglos():
    lista = [1, 2, 3, 4]
    referencia_lista = lista  # referencia_lista "apunta" a la misma lista que lista

    print("Apuntadores y Arreglos (Listas):")
    print(f"Lista original: {lista}")
    
    referencia_lista[0] = 99  # Cambiar el valor a través de la referencia afecta la lista original
    print(f"Lista después del cambio usando referencia: {lista}\n")

# Paso de valores por referencia en funciones
def modificar_lista_por_referencia(lista):
    lista.append(5)  # La lista original será modificada
    print("Modificando lista dentro de la función:", lista)

def paso_por_referencia():
    mi_lista = [1, 2, 3]
    print("Paso por Referencia de Funciones:")
    print("Lista antes de la función:", mi_lista)
    
    modificar_lista_por_referencia(mi_lista)
    print("Lista después de la función:", mi_lista, "\n")

# Función principal
if __name__ == "__main__":
    declaracion_y_utilizacion()
    apuntadores_y_arreglos()
    paso_por_referencia()
