#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"


def ej1():
  print('Ejercicios de práctica con números')

  '''
  Realice un programa que solicite por consola 2 números
  Calcule la diferencia entre ellos e informe por pantalla
  si el resultado es positivo, negativo o cero.
  '''
  print("Ingrese dos numeros:")
  numero_1 = float(input())
  numero_2 = float(input())
  diferencia = numero_1 - numero_2

  if diferencia > 0:
    print("La diferencia entre {} y {} es un numero positivo".format(numero_1,numero_2))
  elif diferencia < 0:
    print("La diferencia entre {} y {} es un numero negativo".format(numero_1,numero_2))
  else:
    print("La diferencia entre {} y {} es cero".format(numero_1,numero_2))


def ej2():
    print('Ejercicios de práctica con números')

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
  '''
  print("Ingrese 3 numeros enteros:")

  num_int_1 = int(input())
  num_int_2 = int(input())
  num_int_3 = int(input())

  if num_int_1 % 2:
    print("{} es par".format(num_int_1))
  else:
    print("{} es impar".format(num_int_1))
  
  if num_int_2 % 2:
    print("{} es par".format(num_int_2))
  else:
    print("{} es impar".format(num_int_2))
  
  if num_int_3 % 2:
    print("{} es par".format(num_int_3))
  else:
    print("{} es impar".format(num_int_3))



def ej3():
    print('Ejercicios de práctica con números')

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
  print("Ingrese dos numeros:")

  calc_1 = float(input())
  calc_2 = float(input())

  print("Ingrese el simbolo de la operacion que quiere realizar con estos dos numeros:")

  operacion = str(float())

  if operacion == + :
    print("El resultado de sumar {} con {} es {}".format(calc_1,calc_2, calc_1 + calc_2))
 



def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
  '''


def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    ej2()
    #ej3()
    #ej4()
    #ej5()
