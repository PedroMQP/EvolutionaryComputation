#Hecho por Pedro Manuel Quiroz Palacios
#CMP with a gredy algortihm
T=9
auxT = T
d =[5,2,1]
cont = 0
res = []
while(auxT > 0 ):
	if auxT - d[cont] >= 0:
		auxT =  auxT - d[cont]
		res.append(d[cont])
	else:
		cont = cont + 1
print(res)