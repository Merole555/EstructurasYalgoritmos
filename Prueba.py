import random
import timeit

random.seed(42)   # misma semilla para todos: los resultados son comparables entre compañeros

# --- Listas de prueba ---------------------------------------------------
PEQUENA        = [5, 1, 4, 2, 8]
ALEATORIA      = [random.randint(0, 1000) for _ in range(300)]

# Lista "casi ordenada": ya viene en orden, salvo 5 elementos fuera de lugar.
# Guarden esta lista, es la protagonista de la Parte 2.
CASI_ORDENADA  = list(range(300))
for _ in range(5):
    i, j = random.randint(0, 299), random.randint(0, 299)
    CASI_ORDENADA[i], CASI_ORDENADA[j] = CASI_ORDENADA[j], CASI_ORDENADA[i]

# Las mismas dos listas, pero grandes (2.000 elementos). Se usan en el experimento de la Parte 2,
# donde hace falta tamaño para que la diferencia se note.
ALEATORIA_G     = [random.randint(0, 10000) for _ in range(2000)]
CASI_ORDENADA_G = list(range(2000))
for _ in range(10):
    i, j = random.randint(0, 1999), random.randint(0, 1999)
    CASI_ORDENADA_G[i], CASI_ORDENADA_G[j] = CASI_ORDENADA_G[j], CASI_ORDENADA_G[i]


def esta_ordenada(lista):
    """Devuelve True si la lista quedó ordenada de menor a mayor."""
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def probar(funcion, nombre):
    """Corre la funcion sobre las listas de prueba y avisa si algo salió mal."""
    for etiqueta, datos in [("pequena", PEQUENA), ("aleatoria", ALEATORIA),
                            ("casi ordenada", CASI_ORDENADA), ("vacia", []),
                            ("un elemento", [7])]:
        resultado = funcion(list(datos))          # list(...) = copia, para no dañar el original
        if not esta_ordenada(resultado):
            print(f"[X] {nombre} FALLA con la lista {etiqueta}: {resultado[:12]}")
            return False
        if sorted(datos) != list(resultado):
            print(f"[X] {nombre} perdió o inventó elementos en la lista {etiqueta}")
            return False
    print(f"[OK] {nombre} ordena bien las 5 listas de prueba")
    return True

def seleccion(lista):
    """
    Ordena la lista de menor a mayor con el método de selección.
    """
    n = len(lista)

    for i in range(n):
        # TODO — te toca a ti.
        # 1. Empieza suponiendo que el mínimo está en la posición i:  pos_min = i
        # 2. Recorre desde i + 1 hasta el final buscando algo más pequeño y actualiza pos_min.
        # 3. Al terminar el recorrido, intercambia lista[i] con lista[pos_min].
        pos_min = i
        for j in range(i + 1, n):
            if lista[j] < lista[pos_min]:
                pos_min = j
        lista[i], lista[pos_min] = lista[pos_min], lista[i]

    return lista

def insercion(lista):
    """
    Ordena la lista de menor a mayor con el método de inserción.
    """
    for i in range(1, len(lista)):
        actual = lista[i]      # la "carta" que estamos ubicando
        j = i - 1              # empezamos a mirar hacia atrás

        # TODO — te toca a ti.
        # Mientras j sea válido (j >= 0) Y lista[j] sea mayor que "actual":
        #     corre lista[j] una posición a la derecha  ->  lista[j + 1] = lista[j]
        #     y retrocede  ->  j -= 1
        #
        # Cuando el while termine, "actual" va en la posición j + 1.
        #
        # Ojo: las DOS condiciones del while van juntas con "and". Si te falta la de j >= 0,
        # el índice se sale por la izquierda y sobreescribes el final de la lista.
        
        while j >= 0 and lista[j] > actual:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = actual

    return lista



probar(insercion, "insercion")
probar(seleccion, "seleccion")

print("Listo. PEQUENA =", PEQUENA)
