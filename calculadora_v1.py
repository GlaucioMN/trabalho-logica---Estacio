# Essa atividade  aborda conceitos básicos para codar uma calculadora básica em Python que realize as quatro operações aritméticas: adição, subtração, multiplicação e divisão.

def calcular(num1, num2, operacao):
    """Realiza uma operação matemática entre dois números.

    Argumentos:
        num1: O primeiro número.
        num2: O segundo número.
        operacao: A operação a ser realizada (+, -, *, /).

    Resultados esperados:
        O resultado da operação ou uma mensagem de erro caso a divisão por zero seja tentada.
    """

    if operacao == "+":
        return num1 + num2
    elif operacao == "-":
        return num1 - num2
    elif operacao == "*":
        return num1 * num2
    elif operacao == "/":
        if num2 == 0:
            return "Divisão por zero não é permitida"
        else:
            return num1 / num2
    else:
        return "Operação inválida"

while True:
    try:
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        resultado = calcular(num1, num2, operacao)
        print("Resultado:", resultado)
    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's':
        break