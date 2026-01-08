import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# funcao para o calculo dos autovalores e autovalores da matriz

def Autovet():
    # solicita ao usuário o tamanho da matriz e pede para o mesmo preenche-la
    
    m = int(input("Informe a altura/largura da matriz: "))

    matriz = [[int(input(f"Digite o valor de a[{i}][{j}]: ")) for j in range (m)] for i in range (m)]

    # calcula os autovalores e autovetores, juntamente com a multiplicidade de cada autovalor

    autovalores, autovetores = np.linalg.eig(matriz)
    multiplicidade = Counter(autovalores)

    # exibicao dos a autovalores, multiplicidade e autovetores, respectivamente

    print("\n~ Autovalores ~\n")
    print(autovalores)

    print("\n~ Multiplicidade dos Autovalores ~\n")

    for a in autovalores:
        print(f"A multiplicidade do autovalor {a} é {multiplicidade[a]}\n") 

    print("~ Autovetores ~\n")
    print(autovetores)

    # exibicao do grafico

    PlotGraf(m, autovalores, autovetores)

    # caso o usuario queira adicionar um vetor ao grafico na direcao de algum autovetor escolhido

    resposta = input("\nDigite (1) caso queira adicionar um vetor ao gráfico: ")

    if (resposta == '1'):
        indice = int(input("Informe o índice do autovetor que possui a direção que o novo vetor seguirá: "))
        vetorextra = [int(input(f"Digite o valor de v[{i}]: ")) for i in range (m)]

        PlotGraf(m, autovalores, autovetores, vetorextra, indice)

# funcao para plotagem dos graficos

def PlotGraf(m, autovalores, autovetores, vetorextra = None, indice = 0.5):
    # caso para uma matriz 2x2

    if (m == 2):
        origem = [0],[0]
        cores = ['b','r']

        plt.figure()

        for i in range(len(autovalores)):
            vetor = autovetores[:,i]
            plt.quiver(origem[0], origem[1], vetor[0], vetor[1], angles='xy', scale_units='xy', scale=1, label=f'λ = {autovalores[i]}', color = cores[i])
        
        # adicao do vetor extra ao grafico

        if (indice != 0.5):
            plt.quiver(origem[0], origem[1], vetorextra[0], vetorextra[1], angles='xy', scale_units='xy', scale=1, label='vetor adicionado', color= cores[indice])
        
        plt.axhline(0, color='gray', linewidth=0.5)
        plt.axvline(0, color='gray', linewidth=0.5)
        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.gca().set_aspect('equal')
        plt.grid(True)
        plt.legend()
        plt.show()
    
    # caso para uma matriz 3x3

    elif (m == 3):
        origem = [0],[0],[0]
        cores = ['b','r','g']

        figura = plt.figure()
        ax = figura.add_subplot(111, projection='3d')

        for i in range(len(autovalores)):
            vetor = autovetores[:, i]
            ax.quiver(origem[0], origem[1], origem[2], vetor[0], vetor[1], vetor[2], length=1.0, label=f'λ = {autovalores[i]}', color=cores[i])
        
        # adicao do vetor extra ao grafico

        if (indice != 0.5):
            plt.quiver(origem[0], origem[1], origem[2], vetorextra[0], vetorextra[1], vetorextra[2], length=1.0, label='vetor adicionado', color= cores[indice])

        ax.set_xlim([-2, 2])
        ax.set_ylim([-2, 2])
        ax.set_zlim([-2, 2])

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        ax.legend()
        plt.show()

# funcao main

def main():
    Autovet()

if (__name__ == '__main__'):
    main()