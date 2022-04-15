#Este programa genera un listado de numero, 
# a los multiples de 3, 5 y ambos le agrega la palabra cyber, click y cyberclick respectimante
# Tiene de salida la lista

resp = "0"  # variable para el ciclo del menú

def lista(): # Metodo que genera la lista continua y verifica los multiples
    lista = []      
    for i in range (1,101):          
        palabra = ""
        if( i % 3 == 0): 
            palabra='cyber'
        if( i % 5 == 0): 
            palabra+='click'                       
        if(palabra == ""): 
            palabra = i
        lista.append(palabra) #agrega a la lista
    print(lista) 

while (resp!= '2'):	# Menú
	print("\n**  Menú  ***")
	print("1.- Imprimir lista ")	
	print("2.- Salir")
	resp = input("Opcion: ")
	if (resp == '1'):
		lista()
	elif (resp == '2'):
		print("Adios...")
	else:
		print("Opcion incorrecta")