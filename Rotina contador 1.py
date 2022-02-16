def comida():
    ovos = 'variavel local de comida'
    print(ovos)
def bacon():
    ovos = 'variavel local de bacon'
    print(ovos)
    bacon()
    print(ovos)
#Programa principal
ovos = 'variavel global'
comida()
print(ovos)




