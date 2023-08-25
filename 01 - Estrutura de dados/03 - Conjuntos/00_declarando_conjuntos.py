# O conjunto ou set, não possui objetos repetidos. Ele elimina os valores duplicados do iterável 
# Não garante a ordem que foi escrita
# Pode usar () ou {}
# Não suportam index ou fatiamento, para fazer tem que converter o set em lista


numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)  # {1, 2, 3, 4}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}
