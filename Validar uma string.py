def validar_string(pergunta,min,max):
    x = input('Digite uma frase:')
    tam = len(x)
    while tam < min or tam > max:
        x = input('Digite uma frase:')
        break # Usei esse break para nao ter um loop infinito na string
    return x

#Programa Principal
x = validar_string('Digite uma frase',0,9) # Aqui se o tamanho min e o max da string
print('Voce digitou ---> {}'.format(x))
