nome = "Guilherme"
idade = 28
profissao = "Progamador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s Idade: %d" % (nome, idade)) # Com % onde a váriavel vai ser substituida. s para string, d inteiros e f para float

print("Nome: {} Idade: {}".format(nome, idade)) # O format usa o {}, ou entre as {} colocar a posição {3}, ou o **dados

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome)) # OU usar o format de forma nomeada
print("Nome: {nome} Idade: {idade}".format(**dados)) 

print(f"Nome: {nome} Idade: {idade}")  # entre {} passa o nome da variável
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") # número de casas que quero 
