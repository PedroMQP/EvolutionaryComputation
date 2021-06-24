#Hecho por Pedro Manuel Quiroz Palacios
#0/1 KP with a gredy algortihm

C = 11
wv = [[3,3],[4,4],[5,4],[9,10] ,[4,4]]#[w,v],[peso,valor]
wv.sort(key = lambda x : x[1]/x[0], reverse=True)#Ordenamos la lista por su beneficio mayor
auxC = C
cont = 0
print("Arreglo ordenado")
print(wv)
res = []
auxC = C
for t in wv:
	if auxC - t[0] >= 0:
		auxC =  auxC - t[0]
		res.append(t)
wv = wv[1:]
print("Solucion")
print(res)
