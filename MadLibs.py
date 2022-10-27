"""MadLibs : Consiste en que el jugador acierte las preguntas hechas por el entrevistador. y por ultimo adivinar 
en que pais se encuentra el entrevistador"""

"""El jugador debe acertar las preguntas que el entrevistador le hara, si acierta mas de cuatro estara dentro, 
si no, estara fuera"""

# Prueba de comienzo:
print("BIENVENIDO A MI MADLIBS. TE HARE UNA SERIE DE PREGUNTAS Y VERE SI TE CONTRATARE PARA TRABAJAR CONMIGO :)")

Comienzo = str(input("\nPara estar dentro deberas acertar 4 de 6 preguntas! Estas list@? (yes/no):   "))
while Comienzo == "no":
    print("\nO ERES UN MIEDOSO O ESTAS EMPEZANDO CON ERRORES. Por favor VUELVE a iniciar!!")

    Comienzo = str(input("\nPara estar dentro deberas acertar 4 de 6 preguntas! Estas list@? (yes/no):   "))

#PREGUNTAS SOBRE EL JUGADOR:

nombre = str(input("\nDime tu nombre: "))
edad = int(input("\nEdad: "))

#excepciones:
if edad < 5 or edad > 110:
    raise ValueError('La edad introducida no es REAL !!')
elif len(nombre) <= 1:
    raise ValueError('El nombre no esta completo !!')
else:
    print(f"\nTienes {edad} years y te llamas {nombre} WELCOME TO THE GAME")

# Creamos un contador de respuestas correctas e incorrectas:

numerosNo = 0 
numeroSi = 0

# Empezamos con las preguntas :
print("-----------------------------------------------------------------------------------------------------------")

HTML = input("\nHTML es un lenguaje de programacion? (yes/no):  ")
if HTML == "no":
    numerosNo += 1

JavaScript = input("\nJavaScript sirve solamente para crear paginas web? (yes/no):  ")
if JavaScript == "no":
    numerosNo += 1

GitHub = input("\nGitHub es un controlador de versiones? (yes/no):  ")
if GitHub == "no":
    numerosNo += 1

FrontEnd = input("\nEl FrontEnd es la parte del servidor? (yes/no):  ")
if FrontEnd == "no":
    numerosNo += 1

Seguridad = input("\nLas url con HTTP son seguras? (yes/no):  ")
if Seguridad == "no":
    numerosNo += 1

python = input("\nPython es un lenguaje de alto nivel? (yes/no):  ")
if python == "yes":
    numeroSi +=1

# creamos las condiciones de juego : 
print("-----------------------------------------------------------------------------------------------------------")
aviso = f"\nHaz acertado {numerosNo + numeroSi} preguntas Bien!! Te queda solo un reto y ya seras contratado"
if numerosNo == 5 and numeroSi == 1:
    print("\nHaz acertado todas las pregutnas bien!! Te queda un solo reto y ta seras contratado")
elif numerosNo == 5 and numeroSi == 0:
    print(aviso)
elif numerosNo == 4 and numeroSi == 1:
    print(aviso)
elif numerosNo == 3 and numeroSi == 1:
    print(aviso)
elif numerosNo == 4 and numeroSi == 0:
    print(aviso)
else:
    print("\nNo haz acertado 4 preguntas! Quedas fuera del puesto. Gracias por participar.")


# Si el jugador gano tendra un reto mas que pasar, si no quedara fuera : 

if numeroSi == 5 or numeroSi == 4 or numeroSi + numerosNo == 4 or numeroSi + numerosNo == 5 or  numeroSi + numerosNo == 6 :
    print("\nDeberas adivinar en que pais me encuentro ahorita...")

    PaisResidente = "Argentina"

    paisresidente = ""
    while paisresidente != PaisResidente:    
        paisresidente = input("\nEn que pais piensas que me encuetro? (PISTA: Es un pais sudamericano):  ").capitalize()

# Felicitamos al jugador por haber ganado el juego y quedar contratado
        
    print(f"\nHaz acertado mi paiz de residencia!! Quedas contratado {nombre}")

