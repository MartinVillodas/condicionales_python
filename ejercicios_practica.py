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
		print("{} es impar".format(num_int_1))
	else:
		print("{} es par".format(num_int_1))
	
	if num_int_2 % 2:
		print("{} es impar".format(num_int_2))
	else:
		print("{} es par".format(num_int_2))
	
	if num_int_3 % 2:
		print("{} es impar".format(num_int_3))
	else:
		print("{} es par".format(num_int_3))



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

	operacion = str(input())

	if operacion == "+":
		print("El resultado de sumar {} con {} es {}".format(calc_1,calc_2, calc_1 + calc_2))
	elif operacion == "-":
		print("El resultado de restar {} con {} es {}".format(calc_1,calc_2, calc_1 - calc_2))
	elif operacion == "*":
		print("El resultado de multiplicar {} con {} es {}".format(calc_1,calc_2, calc_1 * calc_2))
	elif operacion == "/":
		print("El resultado de dividir {} con {} es {}".format(calc_1,calc_2, calc_1 / calc_2))
	elif operacion == "**":
		print("{} elevado a la potencia {} es {}".format(calc_1,calc_2, calc_1 ** calc_2))
	else:
		print("El simbolo ingresado no corresponde a una operacion matematica")
 



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
	
	print("Porfavor ingrese 3 palabras que usted desee:")
	palabra_1 = str(input())
	palabra_2 = str(input())
	palabra_3 = str(input())

	print("Indique como desea ordenar las palabras que usted ingreso:")
	print("Si desea ordenarlas en orden alfabetico ingrese 1")
	print("Si desea ordenarlas por cantidad de letras ingrese 2")

	ordenar = str(input())

	if ordenar == "1":
		if palabra_1 > palabra_2 and palabra_2 > palabra_3:
			print(palabra_1, palabra_2, palabra_3)
		elif palabra_1 > palabra_3 and palabra_3 > palabra_2:
			print(palabra_1, palabra_3, palabra_2)
		elif palabra_2 > palabra_1 and palabra_1 > palabra_3:
			print(palabra_2, palabra_1, palabra_3)
		elif palabra_2 > palabra_3 and palabra_3 > palabra_1:
			print(palabra_2, palabra_3, palabra_1)
		elif palabra_3 > palabra_1 and palabra_1 > palabra_2:
			print(palabra_3, palabra_1, palabra_2)
		elif palabra_3 > palabra_2 and palabra_2 > palabra_1:
			print(palabra_3, palabra_2, palabra_1)
	elif ordenar == "2":
		if len(palabra_1) > len(palabra_2) and len(palabra_2) > len(palabra_3):
			print(palabra_1, palabra_2, palabra_3)
		elif len(palabra_1) > len(palabra_3) and len(palabra_3) > len(palabra_2):
			print(palabra_1, palabra_3, palabra_2)
		elif len(palabra_2) > len(palabra_1) and len(palabra_1) > len(palabra_3):
			print(palabra_2, palabra_1, palabra_3)
		elif len(palabra_2) > len(palabra_3) and len(palabra_3) > len(palabra_1):
			print(palabra_2, palabra_3, palabra_1)
		elif len(palabra_3) > len(palabra_1) and len(palabra_1) > len(palabra_2):
			print(palabra_3, palabra_1, palabra_2)
		elif len(palabra_3) > len(palabra_2) and len(palabra_2) > len(palabra_1):
			print(palabra_3, palabra_2, palabra_1)
	else:
		print("El numero ingresado no es valido.")

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
		print("Ingrese 3 valores correspondientes a temperaturas:")

		temperatura_1 = float(input())
		temperatura_2 = float(input())
		temperatura_3 = float(input())

		if temperatura_1 >= temperatura_2 and temperatura_1 >= temperatura_3:
			print("{} es la mayor temperatura".format(temperatura_1))
		elif temperatura_2 >= temperatura_1 and temperatura_2 >= temperatura_3:
			print("{} es la mayor temperatura".format(temperatura_2))
		elif temperatura_3 >= temperatura_1 and temperatura_3 >= temperatura_1:
			print("{} es la mayor temperatura".format(temperatura_3))
		
		#Temperatura minima

		if temperatura_1 <= temperatura_2 and temperatura_1 <= temperatura_3:
			print("{} es la menor temperatura".format(temperatura_1))
		elif temperatura_2 <= temperatura_1 and temperatura_2 <= temperatura_3:
			print("{} es la menor temperatura".format(temperatura_2))
		elif temperatura_3 <= temperatura_1 and temperatura_3 <= temperatura_1:
			print("{} es la menor temperatura".format(temperatura_3))

		#Promedio

		promedio = ( temperatura_1 + temperatura_2 + temperatura_3 ) / 3

		print("La temperatura promedio es {}".format(promedio))


if __name__ == '__main__':
		print("Ejercicios de práctica")
		ej1()
		ej2()
		ej3()
		ej4()
		ej5()
