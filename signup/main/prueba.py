def verificarPassword(password):
    letras = 0
    mayus = 0
    minus = 0
    numeros = 0
    for i in range(len(password)):
        if ((password[i] >= 'a' and password[i] <= 'z')):
            letras += 1
            minus += 1
        elif (password[i] >= 'A' and password[i] <= 'Z'):
            letras += 1
            mayus += 1
        elif (password[i] >= '0' and password[i] <= '9'):
            numeros += 1
        else:
            print("Caracter '"+password[i]+"' invalido.")
            return False
    if (len(password) >= 8):
        if(len(password) <= 16):
            if letras >= 3:
                if minus >= 1: 
                    if mayus >= 1:
                        if numeros >= 1:
                            return True
                        else:
                            print('La contrasena debe contener al menos 1 numero')
                            return False
                    else:
                        print('La contrasena debe contener al menos 1 mayuscula')
                        return False
                else:
                    print('La contrasena debe contener al menos 1 minuscula')
                    return False
            else:
                print('La contrasena debe contener al menos 3 letras')
                return False
        else:
            print('La contrasena debe contener maximo 16 caracteres')
            return False
    else:
        print('La contrasena debe tener al menos 8 caracteres')
        return False
print(verificarPassword('abvMsdasd'))