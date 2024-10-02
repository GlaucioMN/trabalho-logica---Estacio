# O uso de while True cria um loop que continua indefinidamente até que seja explicitamente interrompido.
# A condição if entrada_idade == '0' verifica diretamente se o usuário digitou 0 para sair do loop.
# O bloco try-except tenta converter a entrada para um número inteiro. Se ocorrer algum erro de entrada de dados
# a exceção ValueError é capturada e uma mensagem de erro personalizada é exibida.





# Inicializa a variável como uma string vazia
# Continua enquanto o usuário não digitar 0
# Verifica novamente para evitar imprimir 0

while True:
    entrada_idade = input("Digite um número inteiro positivo ou 0 para sair: ")

    if entrada_idade == "0":
        break

    try:
        numero = int(entrada_idade)
        if numero >= 0:
            print("Número digitado:", numero)
        else:
            print("Por favor, digite um número inteiro positivo.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")