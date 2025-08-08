# Programa para evaluar una expresión matemática con paréntesis y una división central
def evaluar_expresion():
	print("Ingrese una expresión matemática usando paréntesis. Ejemplo: (2+3)*(4-1)/5")
	expresion = input("Expresión: ")
	try:
		# Evaluar la expresión de forma segura
		resultado = eval(expresion, {"__builtins__": None}, {})
		print(f"El resultado de la expresión es: {resultado}")
		# División central: divide el resultado entre 2 y muestra ambos lados
		print(f"División central: {resultado} / 2 = {resultado/2}")
	except Exception as e:
		print(f"Error al evaluar la expresión: {e}")

if __name__ == "__main__":
	evaluar_expresion()
