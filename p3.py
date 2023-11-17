# a) Função para marcar as regiões atacadas
def marque_atacadas(tab):
    # Criando uma nova matriz vazia para representar as regiões atacadas
    new_tab = [[' ' for _ in range(8)] for _ in range(8)]
    
    # Iterando sobre as posições do tabuleiro
    for i in range(8):
        for j in range(8):
            # Se encontrar uma rainha ('R'), marca as regiões atacadas
            if tab[i][j] == 'R':
                # Marcando horizontal e vertical
                for k in range(8):
                    new_tab[i][k] = 'X'
                    new_tab[k][j] = 'X'
                
                # Marcando diagonais
                for k in range(1, 8):
                    if i-k >= 0 and j-k >= 0:
                        new_tab[i-k][j-k] = 'X'
                    if i-k >= 0 and j+k < 8:
                        new_tab[i-k][j+k] = 'X'
                    if i+k < 8 and j-k >= 0:
                        new_tab[i+k][j-k] = 'X'
                    if i+k < 8 and j+k < 8:
                        new_tab[i+k][j+k] = 'X'
    
    # Imprimindo o tabuleiro com as regiões atacadas
    print("+---+---+---+---+---+---+---+---+")
    for i in range(8):
        print("|", end="")
        for j in range(8):
            print(" {} |".format(new_tab[i][j]), end="")
        print("\n+---+---+---+---+---+---+---+---+")

# b) Lendo o número de rainhas e suas posições
n = int(input())
queens = []
for i in range(n):
    row, col = map(int, input().split())
    queens.append((row-1, col-1))

# Inicializando o tabuleiro com as posições das rainhas
tab = [[' ' for _ in range(8)] for _ in range(8)]
for i, j in queens:
    tab[i][j] = 'R'

# Imprimindo o tabuleiro inicial
print("+---+---+---+---+---+---+---+---+")
for i in range(8):
    print("|", end="")
    for j in range(8):
        print(" {} |".format(tab[i][j]), end="")
    print("\n+---+---+---+---+---+---+---+---+")

# Chamando a função para marcar as regiões atacadas e imprimindo o novo tabuleiro
marque_atacadas(tab)
