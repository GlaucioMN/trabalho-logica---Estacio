entrada_idade = ""  # Inicializa a variável como uma string vazia

while entrada_idade != "0":  # Continua enquanto o usuário não digitar 0
    entrada_idade = input("Digite um número qualquer ou 0 para sair: ")
    if entrada_idade != "0":  # Verifica novamente para evitar imprimir 0
        print("Número digitado:", entrada_idade)