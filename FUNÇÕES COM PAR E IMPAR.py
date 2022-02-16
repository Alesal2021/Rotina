'''
Aqui o codigo sem a função com def
x = int(input('Digite um valor'))
if x % 2 == 0:
    print('PAR')
else:
    print('IMPAR')

'''
def par_impar(x):
   if x % 2 == 0:
    return '----->par<-----'
   else:
    return '----->impar<-----'
#Programa Principal
print(par_impar(int(input('Digite um valor:'))))

