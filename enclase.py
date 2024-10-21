from collections import deque

# Usamos deque para simular una LinkedList
lista = deque()

# Añadir elementos a la lista
lista.append("Palabra")
lista.append(5)
lista.append(17)
lista.append("Palabra 2")

# Remover el último elemento
lista.pop()

# Imprimir el tamaño de la lista
print(f"El tamaño de la lista es: {len(lista)}")

# Imprimir el último elemento
print(lista[-1])