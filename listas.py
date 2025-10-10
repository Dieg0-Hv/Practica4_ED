 #Universidad Nacional Autónoma de México
 #Facultad de Ciencias
 #Licenciatura en Ciencias de la Computación
 #Estructuras Discretas 
 #Practica4
 #Escrito por: Hernandez Vazquez Diego y Bruno Bernardo Soto Lugo
 
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
        if self.cabeza is None:
            return "()"
        # repr(self.cabeza) para que las cadenas salgan con comillas y repr(self.cola) llama recursivamente a __repr__ en la cola
        return f"({repr(self.cabeza)} {repr(self.cola)})"

    def agrega_principio(self, elemento):
        """
        Agrega un elemento al principio de la lista.
        """
        if self.cabeza is None:
            self.cabeza = elemento
            self.cola = Lista()
            return

        # caso recursivo: desplazamos la cabeza actual hacia adelante
        antiguo = self.cabeza
        # ponemos el nuevo elemento como cabeza
        self.cabeza = elemento
        # asi aseguramos que haya un objeto Lista en la cola
        if self.cola is None:
            self.cola = Lista()
        # llamamos recursivamente para insertar el antiguo valor
        self.cola.agrega_principio(antiguo)

    def agrega_final(self,elemento):
        """
        Agrega un elemento al final de la lista.
        """
        if self.cabeza is None:
            self.cabeza = elemento
            self.cola = Lista()
            return

        # Si la cola es None inicializamos como lista vacía
        if self.cola is None:
            self.cola = Lista()

        # Si la cola es la lista vacía le colocamos el elemento ahí
        if self.cola.cabeza is None:
            self.cola.cabeza = elemento
            self.cola.cola = Lista()
            return
        self.cola.agrega_final(elemento)

    def longitud(self):
        """
        Devuelve el número de elementos en la lista.
        """
        return 0

    def contiene(self,elemento):
        """
        Devuelve si el elemento se encuentra en la lista.
        """
        if self.cabeza is None:
            return False

        # Si la cabeza actual es el elemento buscado
        if self.cabeza == elemento:
            return True

        # Buscamos en la cola
        return self.cola.contiene(elemento)

    def copia(self):
        """
        Crea una nueva lista idéntica a esta.
        """
        if self.cabeza is None:
            return Lista()

        # Crear nueva lista con la misma cabeza y la copia recursiva de la cola
        nueva_lista = Lista()
        nueva_lista.cabeza = self.cabeza
        nueva_lista.cola = self.cola.copia()
        return nueva_lista

    def concatena(self, lista):
        """
        Concatena la lista actual con la lista recibida como argumento.
        """
        # Si la lista original está vacía, devolver copia de la otra
        if self.cabeza is None:
            return lista.copia()

        # Crear otra lista con misma cabeza
        nueva_lista = Lista()
        nueva_lista.cabeza = self.cabeza
        nueva_lista.cola = self.cola.concatena(lista)
        return nueva_lista


    def reversa(self):
        """
        Regresa una lista con los elementos en orden invertido a la original.
        """
        # Lista vacía → devolver lista vacía
        if self.cabeza is None:
            return Lista()

        # Invertir la cola y luego agregar la cabeza al final
        lista_invertida = self.cola.reversa()
        lista_invertida.agrega_final(self.cabeza)
        return lista_invertida


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
