# Constantes para los tipos de temperatura
celsius = "Celsius"
fahrenheit = "Fahrenheit"

# Funciones recursivas para convertir temperaturas
def convertir(valor,tipo):
 if tipo== celsius:
  return (9/5) * valor + 32
else: return (5/9) * (valor - 32)


"""def fahrenheit_a_celsius(fahrenheit):
return (5/9) * (fahrenheit - 32)"""

# Función recursiva para manejar la conversión de temperatura
def convertir_temperatura():
# Solicitar input del usuario
opcion = input("Elija la conversión (1 para Celsius a Fahrenheit, 2 para Fahrenheit a Celsius): ")

if opcion == "1":
temp_celsius = float(input("Ingrese la temperatura en Celsius: "))
resultado = convertir(temp_celsius,celsius)
print(f"Resultado: {resultado} °F")
elif opcion == "2":
temp_fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
resultado = convertir(temp_fahrenheit,fahrenheit.setdefault())
print(f"Resultado:1 {resultado} °C")
else:
print("Opción no válida.")

# Preguntar si desea realizar otra conversión
otra_conversion = input("¿Desea realizar otra conversión? (s/n): ")
if otra_conversion.lower() == 's':
convertir_temperatura()

# Iniciar la conversión de temperatura
convertir_temperatura()