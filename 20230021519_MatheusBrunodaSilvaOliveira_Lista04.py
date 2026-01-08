# importando bibliotecas para plotagem de grafico, tabelas e uso de funcoes matematicas

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#################################################################################

def listaSequencia(limite, qindices, tolerancia):
   pares_odernados = [] # lista vazia para armazenar os pares ordenados (nk, ank) que satisfacam |ank - L| < e
   contador = 0 # variavel de controle para estabelecer uma condicao de parada
   natural = 0 # variavel para representar os numeros naturais
   
   while(1):
      if (contador == qindices):    # verifica se a quantidade de indices desejados foi atingida
         break  # caso tenha alcancado, o loop e encerrado
      else:
        if (abs(np.cos(natural) - limite) < tolerancia):    # verifica se |ank - L| < e
           pares_odernados.append([natural, np.cos(natural)])   # caso seja verdadeiro, o numero natural e o seu respectivo valor na sequencia sao armazenados
           contador += 1    # varivael de controle incrementada
      natural += 1  # incremento para o seguinte numero natural
    

   tabela = pd.DataFrame(pares_odernados, columns = ['nk', 'ank = cos(nk)'])  # criando um DataFrame para a exibicao da tabela e plotagem do grafico

   print(tabela) # exibindo a tabela

   plt.scatter(tabela['nk'], tabela['ank = cos(nk)']) # criando o grafico com o eixo x sendo os naturais encontrados e o eixo y os seus valores correspondentes
   
   # exibicao do limite e toleranca

   plt.axhline(y = limite, color = 'green', linestyle ='-')
   plt.axhline(y = (limite - tolerancia), color = 'red', linestyle ='--')
   plt.axhline(y = (limite + tolerancia), color = 'red', linestyle ='--')
   
   # legendas para o eixo x e eixo y, respectivamente

   plt.xlabel('nk')
   plt.ylabel('ank = cos(nk)')

   plt.show() # exibicao do grafico

#################################################################################

def main():
   limite = float(input('Digite um limite dentro do intervalo [-1, 1]: '))

   while(limite < -1 or limite > 1): # tratamento de erro caso o usuário digite um limite fora do intervalo requisitado
      limite = float(input('Limite inválido. Digite um limite dentro do intervalo [-1, 1]: '))
   
   numnatural = int(input('Digite um número natural: '))

   while(numnatural < 0): # tratamento de erro caso o usuário digite um número não natural
      numnatural = int(input('Números negativos não são naturais. Digite um número natural: '))

   tolerancia = float(input('Digite uma tolerância positiva: '))

   while(tolerancia < 0): # tratamento de erro caso o usuário digite uma tolerância negativa
      tolerancia = float(input('Tolerância inválida. Digite uma tolerância positiva: '))

   listaSequencia(limite, numnatural, tolerancia)

#################################################################################

if (__name__ == '__main__'):
    main()



      