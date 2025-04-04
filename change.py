def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos)*100)
    print ("Ingresar gasto:\n {expense}")
    print (f"Dinero recibido\n {money}\n")
    print (" \nVuelto\n")
    print (f"Pesos:\n{money})
    print (f"Centavos:\n{centavos}")
    change()
