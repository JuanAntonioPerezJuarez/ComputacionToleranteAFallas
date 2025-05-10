def divide_num():
    try:
        #Solicitar al usuario que ingrese dos numeros
        num1 = float(input("Ingresa el primer numero: "))
        num2 = float(input("Ingresa el segundo numero: "))
        
        #dividir los números
        result = num1 / num2
        
    except ValueError:
        # Maneja el error si el usuario ingresa algo que no es un numero
        print("Error: Por favor ingresa un numero valido.")
        
    except ZeroDivisionError:
        #intenta dividir entre cero
        print("Error: No se puede dividir entre cero.")
        
    else:
        # Si no hubo errores, mostrar el resultado
        print(f"El resultado de {num1} / {num2} es: {result}")
    
    finally:
        # Este bloque se ejecuta siempre, haya o no un error
        print("Operación de división finalizada.")

# Llamar a la función para realizar la operación
divide_num()
