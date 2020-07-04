import matplotlib.pyplot as plt

def B_spline(t, var):
	if(t<4):
		if var == 'x':
			return  -t**3/6 + 3*t**2/2 - 5*t/2 - 1/2
		else:
			return 7*t**3/2 - 73*t**2/2 + 247*t/2 - 805/6
	else:
		if var == 'x':
			return  t**3/3 - 9*t**2/2 + 43*t/2 - 65/2
		else:
			return -3*t**3 + 83*t**2/2 - 377*t/2 + 1691/6
		

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

xi = [-1,1,3,4,6]
yi = [0,4,-2,3,1]

x = []
y = []

for i in points(3,5.01,0.01):
	i= float(i)
	x.append(B_spline(i,'x'))
for i in points(3,5.01,0.01):
	i=float(i)
	y.append(B_spline(i,'y'))
plt.plot(x,y, color = 'b', label = 'Curva de B-Spline')
plt.plot(xi,yi, 'k--')
plt.title("Curva de B-Spline")
plt.scatter(xi[0],yi[0],label='P0 = (-1,0)',s=18)
plt.scatter(xi[1],yi[1],label='P1 = (1,4)',s=18)
plt.scatter(xi[2],yi[2],label='P2 = (3,2)',s=18)
plt.scatter(xi[3],yi[3],label='P3 = (4,3)',s=18)
plt.scatter(xi[4],yi[4],label='P3 = (6,1)',s=18)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
