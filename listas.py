from typing import List

class Lista:
    """
    Clase para representar listas recursivas.
    """
    def __init__(self,elementos=None):
        """
        Constructor de la clase. Si elementos es None, construye una Lista
        vacía, en otro caso, asigna el primer elemento como la cabeza de la
        Lista y llama recursivamente el constructor para construir la cola de
        la lista utilizando el resto de elementos.
        """
        if elementos != None:
            if not isinstance(elementos,List):
                raise TypeError("Debe recibir una lista de elementos")
            elif len(elementos) == 1:
                self.cabeza = elementos[0]
                self.cola = Lista()
            else:
                self.cabeza = elementos[0]
                self.cola = Lista(elementos[1:])
        else:
            self.cabeza = None
            self.cola = None

    def __repr__(self):
        """
        Representación en cadena, legible para humanos, de
        las listas.
        """
        

    def agrega_principio(self, elemento):
        """
        Agrega un elemento al principio de la lista.
        """

    def agrega_final(self,elemento):
        """
        Agrega un elemento al final de la lista.
        """
        pass

    def longitud(self):
        """
        Devuelve el número de elementos en la lista.
        """
        return 0

    def contiene(self,elemento):
        """
        Devuelve si el elemento se encuentra en la lista.
        """
        return False

    def copia(self):
        """
        Crea una nueva lista idéntica a esta.
        """
        return Lista()

    def concatena(self, lista):
        """
        Concatena la lista actual con la lista recibida como argumento.
        """
        return Lista()


    def reversa(self):
        """
        Regresa una lista con los elementos en orden invertido a la original.
        """
        return Lista()


    def mapea(self,f):
        """
        Devuelve la lista resultante de aplicar una función f sobre los elementos
        de la lista.
        """
        return Lista()

    def filtra(self,f):
        """
        Devuelve la lista resultante de seleccionar los elementos que cumplan
        con la condición f.
        """
        return Lista()

    def __eq__(self, lista):
        """
        Compara dos listas y devuelve si son iguales.
        """
        if not isinstance(lista,Lista):
            return False
        if self.longitud() != lista.longitud():
            return False
        elif self.cabeza == lista.cabeza:
            return self.cola == lista.cola
        else:
            return False
