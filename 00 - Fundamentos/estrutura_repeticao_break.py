while True:  # Laço infinito, loop
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
        continue

    print(numero)


# for numero in range(100):

#     if numero % 2 == 0:
#         continue   #Condição aqui para pular a execução, nesse caso aparecer só números impars

#     print(numero, end=" ")
