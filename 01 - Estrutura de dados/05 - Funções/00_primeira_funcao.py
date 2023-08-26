# Bloco de código identificado por um nome que pode receber parametros, para dizer qual seria a entrada da função
# Pode retornar vários valores
# 

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Aqui é opicional passar o nome durante a execução, ao contrário de cima.
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

# Como chamar a função para ser executada:
exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_2("Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
