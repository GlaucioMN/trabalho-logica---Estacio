50# Essa atividade  aborda todos os conceitos aprendidos  até agora para verficar 
# o entendimento e aplicação na linguagem Python.
# mostra um pequeno codigo para utilização de uma calculadora simples com condiçoes,
# paramentros, argumentos e funções aprendidas ate agora, implementando o codigo anterior V1.


def adicao(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não é possível dividir por zero."
    else:
        return num1 / num2

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisao':
        resultado = divisao(num1, num2)
    else:
        return "Operação inválida."
    return resultado

saida = ''

while saida.lower() != 'n':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calculadora(num1, num2, operacao)
    print(f"Resultado da operação: {resultado}")

    saida = input("Deseja continuar? (S/N): ")