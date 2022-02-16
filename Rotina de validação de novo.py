def valida_inteiro(pergunta, min,max):
    x = int(input(pergunta))
    while x < min or x > max:
        x = int(input(pergunta))
    return x

#Programa Principal
x = valida_inteiro('Digite um valor inteiro:',0, 100)
print('Voce digitou {} Encerrando o programa'.format(x))

