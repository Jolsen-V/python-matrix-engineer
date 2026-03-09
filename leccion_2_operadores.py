
#======================================
#  MÓDULO 01 · LECCIÓN 2: operadores
#======================================

number1 = 96
number2 = 6

#-----------------------------------------
# operadores aritméticos
print()
print("===== ALL BASIC MATHEMATICAL OPERATIONS =====")

print(f"The sum is: {number1+number2}") # suma
print(f"The subtraction is: {number1 - number2}") # esta
print(f"The multiplication is: {number1 * number2}") # multiplicación 
print(f"The division is: {number1 / number2}") # división
print(f"The entire division is: {number1 // number2}") # división entera
print(f"The module is : {number1 % number2}") # módulo (resto)
print(f"The power is: {number1 ** number2}") # potencia

#operadores de comparación
print()
print("-----COMPARASION OPERATORS-------")

print(f"96 will be greater than 6?: {number1 > number2}")
print(f"96 will be less than 6?: {number1 < number2}")
print(f"96 is equal to 6? : {number1 == number2}")
print(f"96 is different from 6?: {number1 != number2}")
print(f"96 is greater than or equal to 6?: {number1 >= number2} ")
print(f"96 is less than or equal to 6?: {number1 <= number2}")

# Operadores lógicos 
print()
print("****** LOGICAL OPERATORS *******")

has_money = True
has_time = False
is_adult = True
has_car = True
has_plane = False

print(f"has time AND is adult: {has_time and is_adult}")
print(f"has plane OR has money:{has_plane or has_money}")
print(f"has money AND has car: {has_money and has_car}")
print(f"NOT has money: {not has_money}")
print(f"NOT has plane: {not has_plane}")
print(f"has time OR has plane: {has_time or has_plane}")