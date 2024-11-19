# Essa atividade  aborda conceitos básicos utilização da estrutura de repetição for em Python,
# como iteração sobre strings e intervalos numéricos,
#além de demonstrar a importância da concatenação de strings.

# Iteração sobre listas : Lista de nomes, personalizando as mensagens de saída.
# Ninhos de laços que abordam o FOR.
# detalha melhor a compreensão de listas para criar listas a partir de iterações.

# Iterando sobre uma string
texto = "Olá, laço for."
for item in texto:
    print("Caractere:", item)

# Iterando sobre um intervalo numérico
for numero in range(1, 11):
    print("Número do intervalo:", numero)

# Iterando sobre uma lista
nomes = ["Carlos", "Fernanda", "Jaqueline"]
for nome in nomes:
    print(f"Olá, {nome}!")

# Criando uma tabela usando laços aninhados e utilziação do range.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Compreensão de listas para criar uma lista de quadrados
quadrados = [x**2 for x in range(1, 6)]
print(quadrados)