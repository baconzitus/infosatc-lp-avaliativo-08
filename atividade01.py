def leiaint(numero):
    if numero=="" or numero==None:
            return 0
    verifica=True
    for x in numero:
        if x in ("0","1","2","3","4","5","6","7","8","9"):
            pass
        else:
            return False

    if verifica==True:
        return int(numero)
    else:
        print("erro inesperado!!")
            


numero = input("numero:")
numero_verificado= leiaint(numero)
if (type(numero_verificado)==int):
    print(numero_verificado)
else:
    print("este numero não é inteiro ou sequer é um numero")
    print(numero)
