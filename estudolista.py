#ESTUDANDO LISTAS
#OS INDICES DA LISTA COMEÇAM EM 0!
lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

#TUPLA(NÃO PODE SER ALTERADA)
tupla = (1, 10, 12, 14) #A TUPLA É USADA ENTRE PARENTESES 
print(tupla)
print(len(tupla)) #A FUNÇÃO LEN REVELA A QUANTIDADE DE ELEMENTOS NA LISTA OU NA TUPLA
print(len(lista_animal))

#CONVERTENDO UMA LISTA PARA TUPLA 
tupla_animal = tuple(lista_animal)
print(tupla_animal)

#CONVERTENDO A TUPLA EM LISTA 
lista_num = list(tupla) #APOS CONVERTER A TUPLA PARA LISTA, PODE SER FEITO ALTERAÇÕES 
lista_num[0] = 100
print(lista_num)

#ALTERANDO NOMES NA LISTA
lista_animal[0] = 'macaco'
print(lista_animal)

#PERCORRENDO A LISTA COM LAÇO DE REPETIÇÃO
for x in lista_animal:
    print(x)
soma = 0
for x in lista:
    print(x)
    #soma += x

#SOMA DOS VALORES DA LISTA
print('Soma dos valores da lista é: {}'.format(sum(lista)))

#MAIOR E MENOR VALOR DA LISTA
print('Maior valor da lista é: {}'.format(max(lista)))
print('Menor valor da lista é: {}'.format(min(lista)))

#ORDENANDO OS VALORES
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

#REVERTENDO AS LISTAS
lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)

#VERIFICANDO SE JA EXISTE UM NOME NA LISTA_ANIMAL
a = input('Qual nome deseja verificar: ')
if a in lista_animal:
    print('O nome {} já está na lista.'.format(a))
else:
    print('O nome {} não existe na lista.'.format(a))
    #INCLUINDO NOVOS REGISTROS A LISTA
    b = input('Deseja incluir o nome {} a lista? '.format(a))
    if b == 'sim':
        lista_animal.append(a)
        print(lista_animal)
    else: 
        print('Ok, obrigado')

#RETIRANDO REGISTROS DA LISTA
c = input('Deseja retirar algum nome da lista? ')
if c == 'sim':
    d = int(input('Qual o indice do nome que será removido? '))
    lista_animal.pop(d)
    print(lista_animal)

#print(lista_animal[1])
#print(type(lista_animal))
