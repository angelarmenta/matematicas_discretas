#developed by Roberto Ángel Meléndez-Armenta
#https://www.youtube.com/@educar-ia

# Función para convertir de decimal a binario
def decimal_a_binario(decimal):
    return bin(decimal)[2:]

# Función para convertir de decimal a octal
def decimal_a_octal(decimal):
    return oct(decimal)[2:]

# Función para convertir de decimal a hexadecimal
def decimal_a_hexadecimal(decimal):
    return hex(decimal)[2:]

# Función para convertir de binario a decimal
def binario_a_decimal(binario):
    return int(binario, 2)

# Función para convertir de octal a decimal
def octal_a_decimal(octal):
    return int(octal, 8)

# Función para convertir de hexadecimal a decimal
def hexadecimal_a_decimal(hexadecimal):
    return int(hexadecimal, 16)

# Prueba de las funciones
decimal = 10
binario = '1010'
octal = '123'
hexadecimal = '2F4'

print(f"El número decimal {decimal} en binario es: {decimal_a_binario(decimal)}")
print(f"El número decimal {decimal} en octal es: {decimal_a_octal(decimal)}")
print(f"El número decimal {decimal} en hexadecimal es: {decimal_a_hexadecimal(decimal)}")
print(f"El número binario {binario} en decimal es: {binario_a_decimal(binario)}")
print(f"El número octal {octal} en decimal es: {octal_a_decimal(octal)}")
print(f"El número hexadecimal {hexadecimal} en decimal es: {hexadecimal_a_decimal(hexadecimal)}")
