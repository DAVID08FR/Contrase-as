import string 
import secrets
import os
os.system("cls")

def contiene_mayusculas(password)->bool:
    for letra in password:
        if letra.isupper():
            return True
    return False


def contiene_simbolos(password)->bool:
    for letra in password:
        if letra in string.punctuation:
            return True
    return False


def generar_password(longitud, tiene_simbolos, tiene_mayusculas)->str:
    combinacion= string.ascii_lowercase + string.digits

#se requyieren simbolos
    if tiene_simbolos:
        combinacion += string.punctuation


#se requieren mayusculas

    if tiene_mayusculas:
        combinacion += string.ascii_uppercase


    longitud_combinacion= len(combinacion)

    nuevo_password=""

    for _ in range(longitud):

        nuevo_password+= combinacion[secrets.randbelow (longitud_combinacion)]   
   
    print(combinacion)
    return nuevo_password

if __name__=="__main__":
    nuevo = generar_password(longitud=10, tiene_simbolos=True, tiene_mayusculas =True)
    print(f"tiene mayusculas: {contiene_mayusculas(nuevo)}")
    print(f"tiene simbolos:{contiene_simbolos(nuevo)}")
    print(nuevo)