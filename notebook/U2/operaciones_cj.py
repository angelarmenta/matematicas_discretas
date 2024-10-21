#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

# Función para la Unión de dos conjuntos
def union(conjunto1, conjunto2):
    return conjunto1.union(conjunto2)

# Función para la Intersección de dos conjuntos
def interseccion(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)

# Función para la Diferencia de dos conjuntos
def diferencia(conjunto1, conjunto2):
    return conjunto1.difference(conjunto2)

# Función para la Diferencia Simétrica de dos conjuntos
def diferencia_simetrica(conjunto1, conjunto2):
    return conjunto1.symmetric_difference(conjunto2)

# Ejemplos de conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Pruebas de las funciones
print(f"Conjunto 1: {conjunto1}")
print(f"Conjunto 2: {conjunto2}\n")

print(f"Unión: {union(conjunto1, conjunto2)}")
print(f"Intersección: {interseccion(conjunto1, conjunto2)}")
print(f"Diferencia (Conjunto 1 - Conjunto 2): {diferencia(conjunto1, conjunto2)}")
print(f"Diferencia Simétrica: {diferencia_simetrica(conjunto1, conjunto2)}")
