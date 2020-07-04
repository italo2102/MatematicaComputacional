import matplotlib.pyplot as plt

def Bezier(t, var):
	if var == 'x':
		return  -2*t**3 + 3*t**2 + 6*t - 3
	else:
		return 4*t**3 - 15*t**2 + 12*t

#Definimos una funcion que de mas puntos dentro del grafico
def points(start, stop=None, step= None):
	if stop == None:
		stop = start + 0.0
		start = 0.0
	if step == None:
		step = 1.0

	while True:
		if step > 0 and start >= stop:
			break
		elif step < 0 and start <= stop:
			break
		yield ("%g" % start) 
		start = start + step

xi = [-3,-1,2,4]
yi = [0,4,3,1]

x = []
y = []

for i in points(0,1.01,0.01):
	i= float(i)
	x.append(Bezier(i,'x'))
for i in points(0,1.01,0.01):
	i=float(i)
	y.append(Bezier(i,'y'))
plt.plot(x,y, color = 'k', label = 'Curva de Bezier')
plt.title("Curva de Bezier")
plt.scatter(xi[0],yi[0],label='P0 = (-3,0)',s=18)
plt.scatter(xi[1],yi[1],label='P1 = (-1,4)',s=18)
plt.scatter(xi[2],yi[2],label='P2 = (2,3)',s=18)
plt.scatter(xi[3],yi[3],label='P3 = (4,1)',s=18)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
