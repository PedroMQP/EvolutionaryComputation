#La codificación de los cromosomas sera una lista de listas donde cada elemento de la lista repre-
# sentara la cantidad monedas seleccionadas de cada moneda correspondiente a su ubicacón
#La longitud de los cromosomas sera fija, pero la longitud de sus elementos no
import math
import random
from  random import randint
import functools
N_chromosomes=8
F0=[]
F1=[]
fitness_values=[]
prob_m = 0.5
C = 8 # Cambio a devolver
wv = [7,5,2,1]#[w,v],[peso,valor]
wv.sort(reverse = True)
iteraciones = 500
L_chromosome = len(wv)
L_num_in = 4	  
Lwheel=N_chromosomes*10
it = 0


def random_chromosome():
	chromosome=[]
	for j in range(L_chromosome):
		bnumber = []
		for i in range(randint(2,L_num_in)):
			if random.random()<0.4:
				bnumber.append(0)
			else:
				bnumber.append(1)
		chromosome.append(bnumber)
	return chromosome


def decode_chromosome(chromosome):
	#print("Cromosoma cod: ",chromosome)
	decode = []
	for c in range(L_chromosome):
		suma = 0 
		for i in range(len(chromosome[c])):
			suma += chromosome[c][i]*(2**i)
		decode.append(suma)
	return decode 

def f(chromosome):
	x = decode_chromosome(chromosome)
	caux = C
	val = 0
	cant = 0
	for e in range(L_chromosome):
		cant += x[e]
		val += x[e]*wv[e]#Cantidad de monedas multiplicada por su denominación
	caux = caux - val
	cant = cant * 2  
	if caux > 0:
		return val - cant  # Solución incompleta 
	elif caux == 0:
		return val*10 - cant# Ya que se alcanzo el objetivo se hace que este en el tope de la genereción
	else:
		return -val - cant # Penalización por si la solución se sale de las restricciones del problema  

def evaluate_chromosomes():
    global F0
    for p in range(N_chromosomes):
        fitness_values[p]=f(F0[p])

def compare_chromosomes(chromosome1,chromosome2):
    fvc1=f(chromosome1)
    fvc2=f(chromosome2)
    if fvc1 > fvc2:
        return 1
    elif fvc1 == fvc2:
        return 0
    else: #fvg1<fvg2
        return -1

def create_wheel():
    global F0,fitness_values

    maxv=max(fitness_values)
    acc=0
    for p in range(N_chromosomes):
        acc=acc + maxv-fitness_values[p]
    fraction=[]
    for p in range(N_chromosomes):
        fraction.append( float(maxv-fitness_values[p])/acc)
        if fraction[-1]<=1.0/Lwheel:
            fraction[-1]=1.0/Lwheel
    fraction[0]-=(sum(fraction)-1.0)/2
    fraction[1]-=(sum(fraction)-1.0)/2

    wheel=[]

    pc=0

    for f in fraction:
        Np=int(f*Lwheel)
        for i in range(Np):
            wheel.append(pc)
        pc+=1

    return wheel
def peso(x):
	v = 0
	for e in range(L_chromosome):
		v += x[e]*wv[e][0]
	return v
def nextgeneration():
    F0.sort(key=functools.cmp_to_key(compare_chromosomes),reverse=True)
    if(it%10 == 0 ):
        print("iteration",it)
        #for e in F0:
        #	print(e) 
        print( "Best solution so far:" )
        print( "f("+str(decode_chromosome(F0[0]))+")= "+
           str(f(F0[0]))) 
    #print("Cambio deuelto: ",peso(F0[0]))
    #elitism, the two best chromosomes go directly to the next generation
    F1[0]=F0[0]
    F1[1]=F0[1]
    for i in range(0,(N_chromosomes-2)//2):
        roulette=create_wheel()
        #Two parents are selected
        p1=random.choice(roulette)
        p2=random.choice(roulette)
        #Two descendants are generated
        o1 = []
        o2 = []
        for i in range(L_chromosome):#Mezclamos cada elemento de ambos cromosomas.
        	l_p1 = len(F0[p1][i])
	        l_p2 = len(F0[p2][i])
	        elem1 = []
	        elem2 = []
	        elem1=F0[p1][i][0:round(l_p1/2)]
	        elem1.extend(F0[p2][i][round(l_p1/2):l_p2])
	        elem2=F0[p2][i][0:round(l_p2/2)]
	        elem2.extend(F0[p1][i][round(l_p2/2):l_p1])
	        o1.append(elem1)
	        o2.append(elem2)

        #Each descendant is mutated with probability prob_m
        if random.random() < prob_m:
            ind = randint(0,L_chromosome-1)# Escogemos la parte del cronosoma a mutar aleatoriamente
            o1[ind][int(random.random()*(len(o1[ind])-1))]^=1
        if random.random() < prob_m:
            ind = randint(0,L_chromosome-1)
            o2[ind][int(random.random()*(len(o2[ind])-1))]^=1
        if random.random() < prob_m:
            ind = randint(0,L_chromosome-1)
            o1[ind].insert(len(o1[ind])-1,randint(0,1))
        if random.random() < prob_m:
            ind = randint(0,L_chromosome-1)
            o2[ind].insert(len(o2[ind])-1,randint(0,1))
        if random.random() < 0.2:
            ind = randint(0,L_chromosome-1)
            if len(o1[ind]) > 2:
            	v = randint(1,len(o1[ind])-1)
            	a = o1[ind][0:v]
            	b = o1[ind][v+1:len(o1[ind])]
        if random.random() < 0.2:
            ind = randint(0,L_chromosome-1)
            if len(o2[ind]) > 2:
            	v = randint(1,len(o1[ind])-1)
            	a = o2[ind][0:v]
            	b = o2[ind][v+1:len(o1[ind])]
        #The descendants are added to F1
        F1[2+2*i]=o1
        F1[3+2*i]=o2

 
    #The new generation replaces the old one
    F0[:]=F1[:]

if __name__=='__main__':
	L_chromosome = len(wv)
	for i in range(0,N_chromosomes):
		rc = random_chromosome()
		F0.append(rc)
		fitness_values.append(f(rc))
		F1=F0[:]
	F0.sort(key=functools.cmp_to_key(compare_chromosomes),reverse = True)
	for i in range(iteraciones):
		it += 1
		nextgeneration()