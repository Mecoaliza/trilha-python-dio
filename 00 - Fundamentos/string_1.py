## METÓDOS

# Padronizar os textos

nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

# Remover espaços em branco

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")  # remover espaços da direira e esquerda
print(texto.rstrip() + ".") # remover espaços da esquerda
print(texto.lstrip() + ".") # remover espaços da direira 

# Junções e Centralização
menu = "Python"

print("####" + menu + "####")
print(menu.center(14)) # Centralizar o nome
print(menu.center(14, "#"))
print("-".join(menu))  # Juntar algo com a String, "-"
