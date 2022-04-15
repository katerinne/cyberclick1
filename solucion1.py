resp = "0"

while (resp!= '2'):	
	print("\n**  Menú  ***")
	print("1.- Imprimir lista ")	
	print("2.- Salir")
	resp = input("Opcion: ")
	if (resp == '1'):
		pass
	elif (resp == '2'):
		print("Adios...")
	else:
		print("Opcion incorrecta")