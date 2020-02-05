option = int(input('Seleccciona una opción: '))
conjunto1 = [1,2,4,5,6]
conjunto2 = [1,2,4,5,6]

def menu():
  if (option  == 1 ):
      print('Elementos del cojunto 1')
      for i in range(len(conjunto1)):
        print(i)

      print('Elementos del cojunto 2')
      for i in range(len(conjunto2)):
        print(i)
  elif (option == 2):
     # agregamos los elementos al primer cojunto
      print('Ingresa los elementos del cojunto1: ')
      print('Si deseas ya no agregar elementos pon 0')
  
      bandera = True

      while(bandera):
        entrada = int( input(''))
        if entrada == 0:
          bandera = False
        else:
          conjunto1.append(entrada)

      # agregamos los elemetos al segundo conjunto
      print('Ingresa los elementos del cojunto2: ')
      print('Si deseas ya no agregar elementos pon 0')
  
      bandera = True

      while(bandera):
        entrada = int( input(''))
  
        if entrada == 0:
          bandera = False
        else:
          conjunto1.append(entrada)

  elif (option == 3):
    print('Selecciona una opcion:')
    print('1. intersección')
    print('2. Union')
    print('3. Diferencia')
    print('4. salir')
    # Conjunto auxiliar donde almacenaremos nuestros datos
    aux = []
    bandera = True
    while(bandera):
      entrada = int(input())
      if (entrada == 1):
        #relalizamos la intersección
        for i in range(len(conjunto1)):
          if  i in conjunto2:
            aux.append(i)   
        bandera = False    
      elif(entrada == 2):
        # Operación union
        #agregamos a nuestro cojunto auxiliar nuestro primeros elementos
        for i in range(conjunto1):
          if i not in aux:
            aux.append(i)
        bandera = False  
        # Agregamos los elementos de nuestro segundo cojunto
        for i in range(conjunto2):
          if i not in aux:
            aux.append(i)
          bandera = False

      elif(entrada == 3):
        # realizamos la diferencia para A/B
        for i in range(len(conjunto1)):
          if i not in conjunto2:
            aux.append(i)
        bandera = False
        
        

      elif(entrada == 4):
        bandera = False
    
    """
      Imprimimos los elementos de nuestro arreglo auxiliar
    """
    for i in range(len(aux)):
      print(i)
menu()
