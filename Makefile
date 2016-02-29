runge4(caso1).png : graficas.py caso1.dat caso2.dat caso3.dat caso4.dat 
	python graficas.py




caso1.dat : 2punto.x
	./2punto.x  0.35355339059327376220 0.4325 0.425 0.46 

2punto.x : 2punto.c 
	gcc 2punto.c -lm -o 2punto.x

 
	
	



