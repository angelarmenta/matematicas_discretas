#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

# Operaciones básicas para números binarios
def suma_binaria(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def resta_binaria(bin1, bin2):
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def multiplicacion_binaria(bin1, bin2):
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def division_binaria(bin1, bin2):
    return bin(int(bin1, 2) // int(bin2, 2))[2:]

# Operaciones básicas para números octales
def suma_octal(oct1, oct2):
    return oct(int(oct1, 8) + int(oct2, 8))[2:]

def resta_octal(oct1, oct2):
    return oct(int(oct1, 8) - int(oct2, 8))[2:]

def multiplicacion_octal(oct1, oct2):
    return oct(int(oct1, 8) * int(oct2, 8))[2:]

def division_octal(oct1, oct2):
    return oct(int(oct1, 8) // int(oct2, 8))[2:]

# Operaciones básicas para números hexadecimales
def suma_hexadecimal(hex1, hex2):
    return hex(int(hex1, 16) + int(hex2, 16))[2:]

def resta_hexadecimal(hex1, hex2):
    return hex(int(hex1, 16) - int(hex2, 16))[2:]

def multiplicacion_hexadecimal(hex1, hex2):
    return hex(int(hex1, 16) * int(hex2, 16))[2:]

def division_hexadecimal(hex1, hex2):
    return hex(int(hex1, 16) // int(hex2, 16))[2:]

# Prueba de las funciones
bin1, bin2 = '1010', '1101'  # Ejemplos en binario
oct1, oct2 = '12', '7'       # Ejemplos en octal
hex1, hex2 = 'a', 'f'        # Ejemplos en hexadecimal

print("Operaciones con números binarios:")
print(f"Suma: {bin1} + {bin2} = {suma_binaria(bin1, bin2)}")
print(f"Resta: {bin1} - {bin2} = {resta_binaria(bin1, bin2)}")
print(f"Multiplicación: {bin1} * {bin2} = {multiplicacion_binaria(bin1, bin2)}")
print(f"División: {bin1} / {bin2} = {division_binaria(bin1, bin2)}")

print("\nOperaciones con números octales:")
print(f"Suma: {oct1} + {oct2} = {suma_octal(oct1, oct2)}")
print(f"Resta: {oct1} - {oct2} = {resta_octal(oct1, oct2)}")
print(f"Multiplicación: {oct1} * {oct2} = {multiplicacion_octal(oct1, oct2)}")
print(f"División: {oct1} / {oct2} = {division_octal(oct1, oct2)}")

print("\nOperaciones con números hexadecimales:")
print(f"Suma: {hex1} + {hex2} = {suma_hexadecimal(hex1, hex2)}")
print(f"Resta: {hex1} - {hex2} = {resta_hexadecimal(hex1, hex2)}")
print(f"Multiplicación: {hex1} * {hex2} = {multiplicacion_hexadecimal(hex1, hex2)}")
print(f"División: {hex1} / {hex2} = {division_hexadecimal(hex1, hex2)}")
