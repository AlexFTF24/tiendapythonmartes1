nombreVendedor=None 
productos=[]
producto={}

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(productos)
        
        
        
    elif opcion==2:
       
       #utilizando ciclos FOR python para recorrer LISTAS
       for productoSeleccionado in productos:
           print (productoSeleccionado ["nombre"]) 

    elif opcion==3:
       #0: preguntar a quien quiero editar
       productoCambio=int (input("Digita el id del producto a cambiar: "))
       #1: Encontrar el elemento
       for productoBuscado in productos:
           if productoBuscado["id"]==productoCambio:
               print("OE LO ENCONTRE")
           else: 
               print("PARSE NO LO ENCONTRE")
       #2: SELECCIONO el elemento 
       #3: ACCEDO a las propiedades o atributos que quiero o puedo modificar 
       
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        