# importando bibliotecas para plotagem de grafico, tabelas e uso de funcoes matematicas

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#################################################################################

def serie_e_sequencia(kmin, kmax, soma = 0, tolerancia = 0, opcao = 0):
   pares_ordenados_sequencia = [] # lista vazia para armazenar os pares ordenados (k, a(k))
   pares_ordenados_serie = []   # lista vazia para armazenar os pares ordenados (k, S(k))
   somatorio = 0    # variável que representa a soma da serie
   
   for n in range(kmax+1):
      # Questão 2 (b) uma serie geometrica convergente, a(k) = 1/2^n
      
      somatorio += 1/(2 ** (kmin + n))  # somando os valores da sequencia a variavel somatorio
      pares_ordenados_sequencia.append([n, 1/(2 ** (kmin + n))]) # adicionando os pares (k,a(k)) a lista
      pares_ordenados_serie.append([n, somatorio])  # adicionando os pares (k,S(k)) a lista
    

   tabela_sequencia = pd.DataFrame(pares_ordenados_sequencia, columns = ['k', 'a(k)'])  # criando um DataFrame para a exibicao da tabela_sequencia e plotagem do grafico
   tabela_serie = pd.DataFrame(pares_ordenados_serie, columns = ['k', 'S(k)'])  # criando um DataFrame para a exibicao da tabela_serie e plotagem do grafico
   tabela_conjunta = pd.DataFrame({'k': tabela_sequencia['k'], 'a(k)': tabela_sequencia['a(k)'], 'S(k)': tabela_serie['S(k)']}) # unindo as tabelas

   print("~ TABELA SEQUÊNCIA ~")
   print(tabela_sequencia) # exibindo a tabela_sequencia
   
   print('\n')

   print("~ TABELA SÉRIE ~")
   print(tabela_serie)  # exibindo a tabela_serie

   plotagem_grafico(tabela_conjunta, opcao, soma, tolerancia) # chamada da funcao para plotar graficos

def plotagem_grafico(data_frame, opcao, soma, tolerancia): # funcao feita com auxilio do DeepSeek, nao estava lembrado como unir dois eixos em um so grafico
    # criando eixo y_esquerdo, o qual representa os valores da sequência

    eixo_sequencia = plt.subplot()
    eixo_sequencia.plot(data_frame['k'], data_frame['a(k)'], 'bo', label='Sequência')
    eixo_sequencia.set_ylabel('Sequência', color='blue')
    eixo_sequencia.tick_params(axis='y', labelcolor='blue')
    eixo_sequencia.set_xticks(data_frame['k'])

    # criando eixo y_direito, o qual representa os valores da série
    
    eixo_serie = eixo_sequencia.twinx()
    eixo_serie.plot(data_frame['k'], data_frame['S(k)'], 'ro', label='Série')
    eixo_serie.set_ylabel('Série', color='red')
    eixo_serie.tick_params(axis='y', labelcolor='red')
    eixo_sequencia.set_xlabel('Números Naturais')

    # caso o usuario escolha a opcao (1) do programa, para adicao das linhas horizontais para a soma e a regiao de tolerancia

    if opcao == 1:
       eixo_serie.axhline(y = soma, color = 'black', linestyle ='-')
       eixo_serie.axhline(y = (soma - tolerancia), color = 'gray', linestyle ='--')
       eixo_serie.axhline(y = (soma + tolerancia), color = 'gray', linestyle ='--')

    plt.show()
   
#################################################################################

def main():
   opcao = int(input('Digite (1) caso saiba que a série é convergente, digite (2) caso contrário: '))

   while(opcao != 1 and opcao != 2): # tratamento de erro caso o usuário digite uma opcao diferente do requisitado
      opcao = int(input('Digite (1) caso saiba que a série é convergente, digite (2) caso contrário: '))

   kmin = int(input('Digite um número natural mínimo: '))

   while(kmin < 0): # tratamento de erro caso o usuário digite um número não natural
      kmin = int(input('Números negativos não são naturais. Digite um número natural mínimo: '))

   kmax = int(input('Digite um número natural máximo maior igual ou natural mínimo: '))

   while(kmax < kmin): # tratamento de erro caso o usuário digite um número não natural
      kmin = int(input('Digite um número natural máximo maior igual ou natural mínimo: '))
   
   # caso o usuário tenha digitado a opcao 1, o programa perguntara a soma e a tolerancia
   
   if opcao == 1:
      soma = float(input('Digite o valor da soma: '))

      tolerancia = float(input('Digite uma tolerância positiva: '))
      
      while(tolerancia < 0): # tratamento de erro caso o usuário digite uma tolerância negativa
         tolerancia = float(input('Tolerância inválida. Digite uma tolerância positiva: '))
      
      serie_e_sequencia(kmin, kmax, soma, tolerancia, opcao)
   else:
      serie_e_sequencia(kmin, kmax)

#################################################################################

if (__name__ == '__main__'):
    main()
