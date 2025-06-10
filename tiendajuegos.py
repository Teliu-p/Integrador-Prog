# -*- coding: utf-8 -*-
"""
TRABAJO INTEGRADOR - PROGRAMACIÓN I
Caso Práctico: Organización del Catálogo de "GameHub"
"""

# Base de datos de videojuegos (nombre, precio, unidades_vendidas)
videojuegos = [
    {"nombre": "The Legend of Zelda", "precio": 59.99, "unidades": 150},
    {"nombre": "Minecraft", "precio": 29.99, "unidades": 500},
    {"nombre": "Cyberpunk 2077", "precio": 39.99, "unidades": 200},
    {"nombre": "Animal Crossing", "precio": 49.99, "unidades": 350},
    {"nombre": "FIFA 23", "precio": 59.99, "unidades": 300}
]

# Algoritmos de ordenamiento (Bubble Sort y Selection Sort adaptados)
def bubble_sort(lista, clave):
    """Ordena una lista de juegos usando Bubble Sort"""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j][clave] > lista[j+1][clave]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def selection_sort(lista, clave):
    """Ordena una lista de juegos usando Selection Sort"""
    for i in range(len(lista)):
        min_idx = i
        for j in range(i+1, len(lista)):
            if lista[j][clave] < lista[min_idx][clave]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Algoritmos de búsqueda
def busqueda_lineal(lista, nombre):
    """Busca un juego por nombre usando búsqueda lineal"""
    for juego in lista:
        if juego["nombre"].lower() == nombre.lower():
            return juego
    return None

def busqueda_binaria(lista, nombre):
    """Busca un juego por nombre usando búsqueda binaria (requiere lista ordenada)"""
    low = 0
    high = len(lista) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if lista[mid]["nombre"].lower() == nombre.lower():
            return lista[mid]
        elif lista[mid]["nombre"].lower() < nombre.lower():
            low = mid + 1
        else:
            high = mid - 1
    return None

# Funciones para mostrar resultados
def mostrar_catalogo(catalogo, titulo):
    """Muestra el catálogo de juegos formateado"""
    print(f"\n🔮 {titulo}:")
    print("-" * 50)
    for juego in catalogo:
        print(f"🎮 {juego['nombre']:20} - ${juego['precio']:5} (Vendidos: {juego['unidades']})")
    print("-" * 50)

def mostrar_juego(juego, titulo):
    """Muestra la información de un juego"""
    if juego:
        print(f"\n🔍 {titulo}:")
        print("-" * 50)
        print(f"🎮 {juego['nombre']:20} - ${juego['precio']:5} (Vendidos: {juego['unidades']})")
        print("-" * 50)
    else:
        print("\n❌ Juego no encontrado")

# Sistema interactivo de menú
def menu_principal():
    """Muestra el menú interactivo y gestiona las opciones"""
    catalogo = videojuegos.copy()
    
    while True:
        print("\n" + "═" * 50)
        print("🕹️  MENÚ PRINCIPAL - GAMEHUB CATÁLOGO")
        print("═" * 50)
        print("1. Ordenar por Precio (Bubble Sort)")
        print("2. Ordenar por Ventas (Selection Sort)")
        print("3. Orden Alfabético (Python sorted)")
        print("4. Búsqueda Lineal (por nombre)")
        print("5. Búsqueda Binaria (por nombre)")
        print("6. Mostrar catálogo original")
        print("0. Salir")
        print("═" * 50)
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            catalogo_ordenado = bubble_sort(catalogo.copy(), "precio")
            mostrar_catalogo(catalogo_ordenado, "CATÁLOGO ORDENADO POR PRECIO")
            
        elif opcion == "2":
            catalogo_ordenado = selection_sort(catalogo.copy(), "unidades")
            mostrar_catalogo(catalogo_ordenado, "CATÁLOGO ORDENADO POR VENTAS")
            
        elif opcion == "3":
            catalogo_ordenado = sorted(catalogo.copy(), key=lambda x: x["nombre"])
            mostrar_catalogo(catalogo_ordenado, "CATÁLOGO ORDENADO ALFABÉTICAMENTE")
            
        elif opcion == "4":
            nombre = input("🔍 Ingrese nombre del juego a buscar: ")
            resultado = busqueda_lineal(catalogo, nombre)
            mostrar_juego(resultado, "RESULTADO BÚSQUEDA LINEAL")
            
        elif opcion == "5":
            nombre = input("🔍 Ingrese nombre del juego a buscar: ")
            catalogo_ordenado = sorted(catalogo.copy(), key=lambda x: x["nombre"])
            resultado = busqueda_binaria(catalogo_ordenado, nombre)
            mostrar_juego(resultado, "RESULTADO BÚSQUEDA BINARIA")
            
        elif opcion == "6":
            mostrar_catalogo(catalogo, "CATÁLOGO ORIGINAL")
            
        elif opcion == "0":
            print("¡Gracias por usar GameHub! 👋")
            break
            
        else:
            print("❌ Opción inválida. Intente nuevamente.")

# Ejecutar el sistema interactivo
if __name__ == "__main__":
    menu_principal()