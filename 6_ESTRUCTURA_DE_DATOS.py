#PILAS
#LISTAS
#ARBOLES

#Enrique Martinez Luna


class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def esta_vacia(self):
        return len(self.items) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

    def __str__(self):
        return str(self.items)


class ListaEnlazada:
    class Nodo:
        def __init__(self, dato):
            self.dato = dato
            self.siguiente = None

    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = self.Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos


class NodoArbol:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = NodoArbol(dato)
        else:
            self._insertar_recursivo(self.raiz, dato)

    def _insertar_recursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierdo is None:
                nodo.izquierdo = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.izquierdo, dato)
        else:
            if nodo.derecho is None:
                nodo.derecho = NodoArbol(dato)
            else:
                self._insertar_recursivo(nodo.derecho, dato)

    def recorrido_inorden(self):
        return self._recorrido_inorden_recursivo(self.raiz, [])

    def _recorrido_inorden_recursivo(self, nodo, recorrido):
        if nodo:
            self._recorrido_inorden_recursivo(nodo.izquierdo, recorrido)
            recorrido.append(nodo.dato)
            self._recorrido_inorden_recursivo(nodo.derecho, recorrido)
        return recorrido


def main():
    print("===== PILA =====")
    pila = Pila()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    print("Contenido de la pila:", pila)
    print("Desapilando:", pila.desapilar())
    print("Contenido de la pila después de desapilar:", pila)
    print("Elemento en el tope:", pila.ver_tope())

    print("\n===== LISTA ENLAZADA =====")
    lista = ListaEnlazada()
    lista.agregar(5)
    lista.agregar(15)
    lista.agregar(25)
    print("Contenido de la lista enlazada:", lista.mostrar())

    print("\n===== ÁRBOL BINARIO =====")
    arbol = ArbolBinario()
    elementos = [50, 30, 70, 20, 40, 60, 80]
    for elemento in elementos:
        arbol.insertar(elemento)
    print("Recorrido inorden del árbol binario:", arbol.recorrido_inorden())


if __name__ == "__main__":
    main()
