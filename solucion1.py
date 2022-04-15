resp = "0"

def lista():  
    lista = []      
    for i in range (1,101):          
        palabra = ""
        if( i % 3 == 0):             
            palabra='cyber'
        if( i % 5 == 0):
            palabra+='click'                       
        if(palabra == ""):
            palabra = i
        lista.append(palabra)
    print(lista)

while (resp!= '2'):	
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