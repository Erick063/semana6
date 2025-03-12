#Suma de Diagonales en una Matriz Cuadrada: Escribe un programa que tome una matriz cuadrada de 5 x 5
#  y calcule la suma de sus diagonales (principal y secundaria). 
matriz=[[1,2,3,4,5],
        [1,2,3,4,5],
        [1,2,3,4,5],
        [1,3,3,4,5],
        [2,2,3,4,5]]
j=0
sum1=0
sum2=0
for i in range(5):
    sum1+=matriz[i][j]
    sum2+=matriz[i][4-j]
    j+=1

print(f"la diagonal principal suma {sum1} y la secudaria suma {sum2}")