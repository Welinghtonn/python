def calculadora():
  print("CALCULADORA")
  
  n1 = int(input("DIGITE O 1º NUMERO: "))
  n2 = int(input("DIGITE O 2º NUMERO: "))
  operador = input("OPERADOR: ")

  if operador == "+":
    print("RESULTADO =",n1 + n2)
  elif operador == "-":
    print("RESULTADO =",n1 - n2)
  elif operador == "*":
    print("RESULTADO =",n1 * n2)
  elif operador == "/":
    print("RESULTADO =",n1 / n2)
  elif operador != "+" or operador != "-" or operador != "*" or operador != "/":
    print("OPERADOR INVÁLIDO")

if __name__ == "__main__":
  calculadora()