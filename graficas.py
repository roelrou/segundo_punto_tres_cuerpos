import numpy as np
import matplotlib.pyplot as plt

d1 = np.loadtxt("caso1.dat", skiprows=2,  unpack=True)
d2 = np.loadtxt("caso2.dat", skiprows=2,  unpack=True)
d3 = np.loadtxt("caso3.dat", skiprows=2,  unpack=True)
d4 = np.loadtxt("caso4.dat", skiprows=2,  unpack=True)


dato1 = d1[1]
dato2 = d1[2]
dato3 = d1[3]
dato4 = d1[4]
dato17 = d1[0]
dato18 = d1[5]
dato19 = d1[6]


dato5 = d2[1]
dato6 = d2[2]
dato7 = d2[3]
dato8 = d2[4]

dato9  = d3[1]
dato10  = d3[2]
dato11 = d3[3]
dato12 = d3[4]

dato13 = d4[1]
dato14 = d4[2]
dato15 = d4[3]
dato16 = d4[4]


#grafica 1
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-3.2, 3.2)
plt.ylim(-2.5, 2.5)
plt.scatter(dato1,dato2,s) # One plot

plt.title(u"Metodo Runge Kutta 4th (a=0.3535533905)")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("runge4(a=0.3535533905).png")
plt.close()


#grafica 2
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-3.2, 3.2)
plt.ylim(-2.5, 2.5)
plt.scatter(dato3,dato4,s) # One plot

plt.title(u"Integrador simplectico 4th (a=0.3535533905)")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("simplectico 4(a=0.3535533905).png")
plt.close()

#grafica 3

s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-2.9, -0.75)
plt.ylim(-0.75, 0.75)
plt.scatter(dato1,dato2,s) # One plot

plt.title(u"Zoom Runge Kutta (a=0.3535533905)")
plt.xlabel("$q_{3}$")
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("Zoom1 Runge Kutta4(a=0.3535533905).png")
plt.close()

#grafica 4

s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-2.9, -0.75)
plt.ylim(-0.75, 0.75)
plt.scatter(dato3,dato4,s) # One plot

plt.title(u"Zoom Simplectico (a=0.3535533905)")
plt.xlabel("$q_{3}$")
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("Zoom1 Simplectico(a=0.3535533905).png")
plt.close()

#grafica 5

s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-0.25, 0.75)
plt.ylim(-0.35, 0.35)
plt.scatter(dato1,dato2,s) # One plot

plt.title(u"Zoom 2 Runge Kutta (a=0.3535533905)")
plt.xlabel("$q_{3}$")
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("Zoom2 Runge Kutta4(a=0.3535533905).png")
plt.close()

#grafica 6

s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-0.25, 0.75)
plt.ylim(-0.35, 0.35)
plt.scatter(dato3,dato4,s) # One plot

plt.title(u"Zoom 2 Simplectico (a=0.3535533905)")
plt.xlabel("$q_{3}$")
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("Zoom2 Simplectico(a=0.3535533905).png")
plt.close()

#grafica 7
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.scatter(dato7,dato8,s) # One plot

plt.title(u"a=0.4325")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("a=0.4325simplectico.png")
plt.close()

#grafica 8
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(0.2, 0.7)
plt.ylim(-0.7, 0.7)
plt.scatter(dato7,dato8,s) # One plot

plt.title(u"zoom1  a=0.4325")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("a=0.4325zoom1.png")
plt.close()

#grafica 9
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-0.08, 0.08)
plt.ylim(-0.1, 0.1)
plt.scatter(dato7,dato8,s) # One plot

plt.title(u" zoom2 a=0.4325)")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("a=0.4325zoom2.png")
plt.close()

#grafica 10
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-2.5, 2.5)
plt.ylim(-2.5, 2.5)
plt.scatter(dato11,dato12,s) # One plot

plt.title(u"a=0.425")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig(" a=0.425.png")
plt.close()

#grafica 11
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(-3.0, 3.0)
plt.ylim(-2.5, 2.5)
plt.scatter(dato15,dato16,s) # One plot

plt.title(u" a=0.46")
plt.xlabel("$q_{3}$") 
plt.ylabel("$p_{3}$")


#plt.show()
fig.savefig("a=0.46.png")
plt.close()


#grafica 12
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(0, 3000)
plt.ylim(-0.4082485, -0.4082481)
plt.scatter(dato17,dato19,s) # One plot

plt.title(u" Energia simplectico")
plt.xlabel("$t$") 
plt.ylabel("$Energia$")


#plt.show()
fig.savefig("energia simplectico.png")
plt.close()

#grafica 13
s=0.03
fig=plt.figure() # Create and empty figure
plt.xlim(0, 3000)
plt.ylim(-0.4082485, -0.4082481)
plt.scatter(dato17,dato18,s) # One plot

plt.title(u" Energia RK")
plt.xlabel("$t$") 
plt.ylabel("$Energia$")


#plt.show()
fig.savefig("energiark.png")
plt.close()
