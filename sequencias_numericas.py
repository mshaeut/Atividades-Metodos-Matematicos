# importando bibliotecas para plotagem de gráfico e tabelas

import pandas as pd
import matplotlib.pyplot as plt
import math

#################################################################################

# função para o caso onde o limite não é conhecido
def sequenciaA(nmin, nmax):
    pares_ordenados = [] # lista vazia para armazenar os números naturais e sua imagem correspondente

    for n in range(nmin, nmax+1):
        num = 3 * n * math.sqrt(n) + 1
        dom = 7 - (2 * n * math.sqrt(n))
    
        pares_ordenados.append([n, num/dom]) # o argumento num/dom refere-se à formula geral da sequencia

    tabela = pd.DataFrame(pares_ordenados, columns = ['n', 'termo geral']) # construindo um dataframe para exibir a tabela
    
    print(tabela) # exibindo a tabela com os números naturais e sua imagem correspondente

    plt.scatter(tabela['n'], tabela['termo geral']) # plotando o gráfico da sequência
    
    plt.xticks(range(nmin, nmax + 1)) # comando para exibir os números naturais de forma discreta no gráfico
    
    # definindo título do gráfico e dos eixos x e y

    plt.title('Representação Gráfica')
    plt.xlabel('n')
    plt.ylabel('termo geral')

    plt.show() # exibindo o gráfico

# função para o caso onde o limite é conhecido
def sequenciaB(nmin, nmax, limite, N, tolerancia = 10**(-3)):
    pares_ordenados = [] # lista vazia para armazenar os números naturais e sua imagem correspondente
  
    for n in range(nmin, nmax+1):
        num = 3 * n * math.sqrt(n) + 1
        dom = 7 - (2 * n * math.sqrt(n))

        pares_ordenados.append([n, num/dom]) # o argumento num/dom refere-se à formula geral da sequencia

    tabela = pd.DataFrame(pares_ordenados, columns = ['n', 'termo geral']) # construindo um dataframe para exibir a tabela
    
    print(tabela) # exibindo a tabela com os números naturais e sua imagem correspondente

    plt.scatter(tabela['n'], tabela['termo geral']) # plotando o gráfico da sequência
    
    # traçando retas horizontais que representam o y = limite, y = limite - e, y = e - limite, respectivamente

    plt.axhline(y = limite, color = 'green', linestyle ='-')
    plt.axhline(y = (limite - tolerancia), color = 'red', linestyle ='--')
    plt.axhline(y = (limite + tolerancia), color = 'red', linestyle ='--')

    plt.axvline(x = N, color = 'blue', linestyle ='--') # traçando uma reta vertical que representa o N(e)

    plt.xticks(range(nmin, nmax + 1)) # comando para exibir os números naturais de forma discreta no gráfico

    # definindo título do gráfico e dos eixos x e y

    plt.title('Representação Gráfica')
    plt.xlabel('n')
    plt.ylabel('termo geral')

    plt.show() # exibindo o gráfico

#################################################################################

# função main
def main():
    opcao = input('O limite da sequência numérica é conhecido?\n') # variável para saber se o usuário conhece o limite da sequência numérica 

    if (opcao == 'SIM'): # caso onde o usuário conhece o limite
        min = int(input('Informe o valor mínimo: '))
        max = int(input('Informe o valor máximo: '))
        lim = float(input('Informe o limite: '))
        natural = int(input('Informe o N(e): '))

        sequenciaB(min, max, lim, natural) # chamada da função

    elif (opcao == 'NÃO'): # caso onde o usuário desconhece o limite
        min = int(input('Informe o valor mínimo: '))
        max = int(input('Informe o valor máximo: '))
        
        sequenciaA(min, max) # chamada da função

#################################################################################

if (__name__ == '__main__'):
    main()

    

      
