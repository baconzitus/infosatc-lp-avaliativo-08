def leiaInt(numero):
    try:
        numero_int=int(numero)
        print(numero_int)
        return numero_int
    except(ValueError,TypeError):
        print("o numero digitado não é um inteiro")
    return 

def leiaFloat(numero):
    try:
        numero_flaot=float(numero)
        print(numero_flaot)
        return numero_float
    except(ValueError,TypeError):
        print("o numero digitado não é um real")
    return


while True:
    numero_int=input("\nnumero inteiro: ")
    leiaInt(numero_int)

    numero_float=input("\nnumero real: ")
    leiaFloat(numero_float)


