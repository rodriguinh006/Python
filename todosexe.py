## EXE002


''' nome = str(input('Digite seu nome: '))

print(f'Olá {nome}, Bem vindo')

'''

#exe003
'''

numero1 = int(input('Primeiro Número:'))

numero2 = int(input('Segundo número: '))

soma = numero1 + numero2

print(f'a soma de {numero1} + {numero2} é igual {soma} !') 
'''

#exe004
'''

elemento = input('Digite qualquer coisa: ')

print(f'O tipo primitivo de {elemento} é {type(elemento)}')

print(f'Espaços', elemento.isspace())

print(f'Númerico ?', elemento.isnumeric())

print(f'Alfabetico ?', elemento.isalpha())

print(f'Alfanumerico?', elemento.isalnum())

print('Maiusculo ?', elemento.isupper())

print('Minuscolo? ',elemento.islower())
'''

#Exe005
'''

num = int(input('Digite um número:'))

numantes = num - 1

numdepois = num + 1


print(f'O número anterior é {numantes}, o número é {num}, e o número depois é {numdepois}')
'''

#Exe006
'''

num = int(input('Digite um número: '))

dobro = 2 * num

triplo = 3 * num

raiz = num ** (1/2)

print(f'dobro: {dobro:.2f}, Triplo: {triplo:.2f}, Raiz: {raiz:.2f}')
'''
'''

#Exe007

mediamat1 = 0

mediamat2 = 0

mediamat3 = 0

mediamat4 = 0

mediamat5 = 0

c = 1


for m in range(1, 4):

    if m ==  1:

        materia1 = str(input('Matéria:'))

        nota1 = int(input('Nota 1: '))

        nota2 = int(input('Nota2: '))

        mediamat1 = (nota1 + nota2) / 2

        m += 1

    elif m == 2:

        materia2 = str(input('Matéria:'))

        nota1 = int(input('Nota 1: '))

        nota2 = int(input('Nota2: '))

        mediamat2 = (nota1 + nota2) / 2


    elif m == 3:

        materia3 = str(input('Materia: '))

        nota1 = int(input('Nota1: '))

        nota2 = int(input('Nota2: '))

        mediamat3 = (nota1+nota2) / 2 
    

print(f'{materia1} a média foi: {mediamat1:.2f}')

if mediamat1 >= 5:

    print('Parabéns, Aprovado!')
else:

    print('Reprovado, estude mais !')

print(f'{materia2} a média foi: {mediamat2:.2f}')

if mediamat2 >= 5:

    print('Parabéns, Aprovado!')
else:

    print('Reprovado')

print(f'{materia3} a média foi: {mediamat3:.2f}')

if mediamat >= 5:

    print('Parabens, Aprovado!')
else: 

    print('Reprovado!')    
    '''

#Exe008
'''

num = int(input('Digite uma medida em metros: '))

cm = num * 100

milim = num * 1000

dec = num / 10

micr = num * (10**6)

km = num / 1000


##print(f'''#{num} em cm é: {cm}cm.

#Em milimetros é: {milim}mm.

#Em decimetro é: {dec}dc.

#Em Micrômetro é  {micr}mcr.

#Em Quilometro é {km}KM.''')


#Exe009
'''

n = int(input('Digite um número para saber sua tabuada: '))


for v in range(0, 11):

    res = n * v

    print(f'{n} x {v} = {res}')
    '''


    #Exe10
'''

din = float(input('Quanto tem em Reais $: '))

dolar = din / 3,27


print(f'${din} em dolar é {dolar:}')
'''


#Exe010
'''

l = float(input('Lardura: '))    #entrada de dados (input)

h = float(input('Altura: '))

area = l * h                     # multiplicação para achar a área

tinta = area / 2                 # quantidade de tinta por metro quadrado


print(f'Sua área foi de {area}metros², você vai precisar de {tinta} litros de tinta')
'''

#Ece012
'''

preço = float(input('Qual o valor do produto?'))

desc = preço - (preço * 5 / 100)
print(desc)
'''


#Exe013



'''resp = 'Ss'
aumento = 0

#trabalhador = list()

#salario = list()

empresa = {}

while resp in 'Ss':
        

    #trabalhador.append(str(input('Trabalhador: ')))

    #salario.append(float(input('Salário: ')))

    trabalhador = str(input("Trabalhador: "))

    salario = float(input('Salário: '))

    aumento = salario + salario * 15 / 100

    resp = str(input('Proximo?  [S / N] '))
    


print(trabalhador, salario)

print(f'aumento :{aumento}')
print(empresa)
'''
'''

trabalhador = str(input('Nome do trabalhador'))

salario = float(input('Salário inicial: '))

aumento = 15 / 100 * salario

salarioFinal = aumento + salario

print(f'O Funcionário {trabalhador}, teve 15% de aumento e seu salário foi de ${salario}reais para ${salarioFinal}reais')
'''

#Exe014
'''

celsius = float(input('Temperatura em Celcius: '))

Fahrenheit = (celsius * 9 / 5) + 32

print(f'A Temperatura de {celsius}° Celsius em Fahrenheit é: {Fahrenheit}')
'''


#exe015
'''

print('Olá, Gostaria de Alugar um carro?  \n')

print('== '* 30)

dias = int(input('Quantos dias precisará do carro?'))

km = float(input('Quantos Km irá rodar ? '))

preçoKm = 0.15 * km

preçoDias = 60 * dias

preçoAluguel = preçoDias + preçoKm

print(f'Para {dias} dias e rodando {km} Km, o valor fica ${preçoAluguel} Reais')
'''

#Exe017
'''

num = float(input('Digite um número real: '))

inteiro = num // 1
print(inteiro)
'''
'''

#Exe016

import math

catetoOp = float(input('Cateto Oposto: '))

catetoAd = float(input('Cateto Adjacente: '))


hipotenusa = math.sqrt(catetoAd*catetoAd + catetoOp*catetoOp)


print(f'A Hipotenusa do seu treângulo é: {hipotenusa}')
'''

#Exe018
'''


from math import radians, sin, cos, tan

angulo = float(input('Angulo: '))

seno = sin(radians(angulo))

print(f'O seno do angulo {angulo} é {seno:.2f}')

cosseno = cos(radians(angulo))

print(f'O cosseno do angulo {angulo} é {cosseno:.2f}')

tang = tan(radians(angulo))

print(f'A tangente do angulo {angulo} é {tang:.2f}')
'''


#Exe019
'''
import random

alunos = list()


for c in range(1, 5):

    alunos.append(str(input('Nome do aluno:')))

escolha = random.choice(alunos)

print(escolha)
'''

#Exe020
'''
import random

alunos = []


for c in range(1, 5):

    alunos.append(str(input('Alunos: ')))

random.shuffle(alunos)
print(alunos)
'''

#exe021
'''

import pygame

pygame.init()

pygame.mixer.music.load('exe01.mp3')

pygame.mixer.music.play()

pygame.event.wait()
'''

#Exe022
'''

nome = str(input('Nome completo: ')).strip()

print(nome.upper())

print(nome.lower())

print(len(nome)- nome.count(' '))
'''

#Exe023
'''

num = int(input('Digite um número: '))

milhar = num // 1000 % 10

centena = num // 100 % 10

dezena = num // 10 % 10

unidade = num // 1 % 10


print(f'Unidade {unidade}, Dezena {dezena}, Centena {centena}, Milhar {milhar} ', end='')
'''

#Exe024
'''

cidade = str(input('Em qual Cidade nasceu? ')).strip()

print(cidade[0:5].upper() == 'SANTO')
'''

#Exe025
'''

nome = str(input('Qual seu nome? ')).strip()

print('Seu nome tem Silva ? {}', format('SILVA' in nome.upper()))
'''

#Exe026
'''

frase = str(input('Frase: ')).upper()

print(f'a lentra a aparece {frase.count("A")}')

print(f'A primeira letra a aparece na posição {frase.find("A")+1}')

print(f'A ultima letra a aparece na posição {frase.rfind("A")+1}')
'''
#Exe027


#Exe027
'''
n = str(input('Digite seu nome completo: ')).strip()  #inicia a variável como str, usa a aplicação .strip() que retira todos os espaços entre as palavras
nome = n.split()  #"fatia" uma string em uma lista atribuindo posições a cada palavra da string exe n = olá mundo n.split() = ['Olá', 'Mundo']
print(f'Seu primeiro nome é {nome[0]}') # a formatação {nome[0]} chama a variável da lista na posição '0' 
print(f'Seu ultimo nome é {nome[len(nome)-1]}')  # {nome[len(nome)-1]} faz uma leitura do comprimento da string ou lista, ao chamar será dado o tamanho final da lista e suas posições, sabendo disso o Python chama esse valor para ser aprentado 
#exemplo se str nome = olá mundo outra vez eu uso o .split() tornando uma lista, ['olá[0]', 'mundo[1]', 'outra[2]', 'vez[3]'] meu len(nome) = 4 posições então o python retorna o valor 4, sendo assim a syntaxe {nome[len(nome)]} seria igual a nome[4] 
'''

#Exe028
'''
from time import sleep
from random import randint            #importa a biblioteca Random e a função randint para rodar um número inteiro aleátorio
computador = randint(0, 5)            # cria uma varável com valor aleátorio entre (0, 5)
print('>' * 40)
print(' Pense em um número: ')
print('<' * 40)
jogador = int(input('Em qual número pensei? '))
print("PROCESSANDO !!!")
sleep(2)                              #Função sleep da biblioteca time faz com que o programa "espere" um tempo antes de coninuar rodando
if jogador == computador:             #condição para o usuário vencer é ser = ao randint da função random
    print('Parabéns!! você conseiguiu vencer !!')
else:
    print('Você perdeu!!')
'''

#Exe029
'''
velocidade = int(input('Qual a velocidade do carro? '))
velociMulta = velocidade - 80
multa = velociMulta * 7 
if velocidade <= 80:
    print('Tenha um excelente dia!!')
else:
    print(f'Você foi multado em ${multa} reais por estar a {velociMulta}Km/h acima do limite que é de 80km/h ')
    '''
#Exe030

'''
resp = 'Ss'
while resp in 'Ss':
    
    num = int(input('Digite um úmero inteiro para saber se é par ou impar: '))
    if num % 2 == 0:
        print('Par')
    
    else:
        print('Imparrrr')
    resp = str(input(' quer continuar ? [ S / N ] '))
'''
