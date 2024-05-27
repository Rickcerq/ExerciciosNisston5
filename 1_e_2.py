matriz = [[8, 6, 7, 8, 6], 
          [5, 5, 6, 7, 8], 
          [6, 7, 8, 6, 5], 
          [7, 5, 9, 7, 4]]

soma = []

linha_soma = []
linha_soma1 = []
for j in range(len(matriz[0])):
     elemento_soma = matriz[0][j] + matriz[1][j]
     linha_soma.append(elemento_soma)
     elemento_soma1 = matriz[2][j] + matriz[3][j]
     linha_soma1.append(elemento_soma1)
soma.append(linha_soma)
soma.append(linha_soma1)

print(soma)