import numpy
# Inicialización 
cadena2 = "compnting"
cadena1 = "school"
lc1 = []
lc2 = []
tabla = numpy.array([[0]*(len(cadena1)+1)]*(len(cadena2)+1))
for i in range(1,len(cadena1)+1):
	lc1.append(cadena1[i-1])
	tabla[0][i] = i
for j in range(1,len(cadena2)+1):
	lc2.append(cadena2[j-1])
	tabla[j][0] = j
#Distacia de levenshtein
for i in range(len(cadena2)):
	for j in range(len(cadena1)):
		if cadena2[i] != cadena1[j]:
			val = 1
		else:
			val = 0
		tabla[i+1][j+1] =min(tabla[i+1][j]+1,tabla[i][j+1]+1,tabla[i][j]+val)
print(tabla)