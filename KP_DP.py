#Hecho por Pedro Manuel Quiroz Palacios
#0/1 KP with dynamic programming

import numpy

C = 10
wv = [[5,3],[4,3],[3,1],[2,3]]#[w,v],[peso,valor]
tabla = numpy.array([[0]*(C+1)]*(len(wv) + 1))
for i in range(1,len(wv)+1):
	for j in range(1,C+1):		
		if wv[i-1][0] > j:
			tabla[i][j] = tabla[i-1][j]
		else:
			tabla[i][j] = max(tabla[i-1][j],wv[i-1][1] + tabla[i-1][j-wv[i-1][0]])
for fila in tabla:
	print(fila)
i = len(wv)
j = C
res = []

while i != 0:
	if tabla[i][j] != tabla[i-1][j]:
		res.append(wv[i-1])
		j  = j - wv[i-1][0] 
	i -= 1

print("La respuesta es: \n",res)