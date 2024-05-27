matriz = [[8, 6, 7, 8, 6], 
          [5, 5, 6, 7, 8], 
          [6, 7, 8, 6, 5], 
          [7, 5, 9, 7, 4]]

soma = []
somador = 0
linha_soma = []

for j in range (len(matriz)):
 for i in range (len(matriz[j])):
   somador = somador + matriz[j][i]
   linha_soma.append(somador)
     
soma.append(linha_soma)


print(soma)