#Hecho por Pedro Manuel Quiroz Palacios
#CMP KP with dynamic programming

import numpy

C = 21

wv = [1,2,5]#Valor de las monedas
wv.sort()
tabla = numpy.array([[0]*(C+1)]*(len(wv)))
for i in range(len(wv)):
	for j in range(1,C+1):
		if i == 0:
			tabla[i][j] = j/wv[i] 
		elif wv[i] > j:
			tabla[i][j] = tabla[i-1][j]
		else:
			tabla[i][j] = min(tabla[i-1][j], 1 + tabla[i][j - wv[i]])
for fila in tabla:
	print(fila)
i = len(wv) - 1
j = C
res = []
while j != 0:
	if i == 0 and j ==1:
		j -= wv[i]
		res.append(wv[i])
	elif tabla[i][j] != tabla[i-1][j]:
		res.append(wv[i])
		j -= wv[i]
	else:
		i -= 1

print("La respuesta es: \n",res)
'''
'''