# Conjunto não ordenardo pares, chave e valor, separadas por ,.
# usa-se {} ou dict
# Chave é imutável, valor pode ser mutavél e imutável

pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# Quando já tem o dicionário e vai acrescentar mais um valor
pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
