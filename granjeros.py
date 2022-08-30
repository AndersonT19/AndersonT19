arch = open('datos.txt','r')
arch2 = open('facturacion.txt','w')
contenido = arch.readlines()
cd = 0
mayor = 0
linea = 0
for linea in  range(len(contenido)):
	datos = contenido[linea].split(',')
	linea += 1
	nombre = datos[0]
	tipo = int(datos[1])
	hecta = int(datos[2])
	if hecta > 50:
		if tipo == 1:
			descuento = 100*hecta*0.05
			MT = (100*hecta) - descuento
			cd += 1
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		elif tipo == 2:
			descuento = 200*hecta*0.05
			MT = (200*hecta) - descuento
			cd += 1
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		elif tipo == 3:
			descuento = 300*hecta*0.05
			MT = (300*hecta) - descuento
			cd += 1
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		else:
			descuento = 500*hecta*0.05
			MT = (500*hecta)- descuento
			cd += 1
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
	else:
		if tipo == 1:
			MT = 100*hecta
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		elif tipo == 2:
			MT = 200*hecta
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		elif tipo == 3:
			MT = 300*hecta
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
		else:
			MT = 500*hecta
			arch2.write(f'{nombre} fumigo {hecta} hectareas y pago en total {MT}bs' + '\n')
	if hecta > mayor:
		mayor = hecta
		nombremayor = nombre
porc = cd/len(contenido)*100
print(f'el porcentaje es {porc}%')
print(f'{nombremayor} fue el que fumigo mas con {mayor} hectareas')