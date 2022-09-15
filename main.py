import os
import time
import random

#Se esta usando tuplas por que la cantidad de preguntas y respuestas es fija
#Las tuplas tambien tienen mejor facilidad de acceso
#Las preguntas tendran niveles de dificultad?
preguntas = (
  "1. ¿Cual es el desierto mas extenso del Perú?\n\ta) Sechura\n\tb) Atacama\n\tc) Nazca\n\td) Huaracanga",
  "2. ¿Qué río sirve de límite natural con Ecuador?\n\ta) Rio Lurin\n\tb) Rio Zarumilla\n\tc) Rio Tumbes\n\td) Rio Chira",
  "3. ¿Cuál es el rio más largo del Perú?\n\ta) Rio Amazonas\n\tb) Rio Putumayo\n\tc) Rio Rimac\n\td) Rio Ucayali",
  "4. En sudamérica ¿Que puesto ocupa el Perú ,respecto al tamaño?\n\ta) 4\n\tb) 5\n\tc) 3\n\td) 1",
  "5. Relieves formados por erosión fluvial, donde los ríos erosionan las cadenas central y oriental de los Andes. Poseen potencial hidroenergético y víal\n\ta) Desiertos\n\tb) Pongos\n\tc) Restingas\n\td) Valles Longitudinales")

respuestas_correctas = ("a","b","d","c","b")
respuestas_disparatadas = ("b","a","c","d","a")
respuestas_casi_correctas = ("d","c","b","a","d")
respuestas_incorrectas = ("c","d","a","b","c")

#Se usan colores para mostrar el acierto de las respuestas
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
MAGENTA = "\033[35m"
RESET = "\033[39m"


# Texto de bienvenida
print("Bienvenido a mi trivia sobre GEOGRAFIA DEL PERU")
time.sleep(1)
print("Pondremos a prueba tus conocimientos")
time.sleep(1)
nombre = input("Para empezar ...\n¿Como te llamas? o.O?: ")
print("Ok {}, comenzamos en ...".format(nombre),end = " ")

for i in range(5,0,-1):
  print("{}, ".format(i), end = "",flush = True)
  time.sleep(1.5)

puntajes = []
jugar_trivia = True
while jugar_trivia:
  os.system ("clear") #Limpia la consola
  #Se define el puntaje inicial mediante un numero aleatorio
  puntaje = random.randint(150, 300)
  # Es importante dar instrucciones sobre cómo jugar:
  print("Tu puntaje inicial es de {} puntos".format(puntaje))
  print("Buena suerte :D")
  time.sleep(3)
  
  i = 0
  for pregunta in preguntas:
    os.system ("clear")
    
    print("Puntaje: {}".format(round(puntaje,2)))
    print("Responde la siguiente pregunta escribiendo la letra de la alternativa y presiona 'Enter' para enviar tu respuesta:")
    print(pregunta)
    rpta = input("Introduce la alternativa correcta: ").lower()
    while rpta not in ("a","b","c","d"):
      print("Ni lo pienses, solo se permite a, b, c o d")
      rpta = input("Introduce la alternativa correcta: ").lower()
  
    rpta = rpta.lower()
  
    if rpta == respuestas_casi_correctas[i]: #Sera de color YELLOW
      print("{}Uff! casi le atinas{}".format(YELLOW,RESET))
      puntos = random.randint(100, 200)
      print("Solo ganaste {} puntos\n".format(puntos),flush = True)
      puntaje += puntos
    elif rpta == respuestas_incorrectas[i]: #Sera de color MAGENTA
      print("{}Que mal, respuesta incorrecta{}".format(MAGENTA,RESET))
      puntos = random.randint(100, 150)
      print("Pierdes {} puntos\n".format(puntos),flush = True)
      puntaje -= puntos
    elif rpta == respuestas_disparatadas[i]: #Sera de color RED
      print("{}Que terrible, una respuesta disparatada{}".format(RED,RESET))
      penalizacion = round(random.random() + 2, 2)
      print("Tu puntaje se divide entre {}\n".format(penalizacion),flush = True)
      puntaje /= penalizacion
    else: #Sera de color GREEN
      print("{}Bien hecho!!!{}".format(GREEN,RESET))
      premio = round(random.random() + 2, 2)
      print("Tu puntaje se multiplica por {}\n".format(premio),flush = True)
      puntaje *= premio

    time.sleep(3)
    i += 1

  os.system ("clear")
  #Al final de cada intento se comprueba si el puntaje baja de cero
  #Cuando suceda eso el jugar perdio en ese intento
  #Caso contrario el jugador pasa al bonus de dado que aumenta su puntaje total
  if puntaje <= 0:
    print("Perdiste. Tus puntos bajaron a 0 o menos")
    print("Puntaje final: {}".format(puntaje))
    puntajes.append(puntaje)
  else:
    puntaje = round(puntaje,2)
    print("Tienes {} puntos pero ...".format(puntaje))
    print("El dado mágico multiplicara tus puntos por ...", end=" ")
    dado = random.randint(1, 6)
    time.sleep(3)
    print(dado)
    puntaje *= dado
    print("Puntaje final: {}".format(puntaje))
    puntajes.append(puntaje)

  #Se da la oportunidad de jugar de nuevo si el jugador escribe si, Si o SI
  jugar_otra = input("\n¿Quieres jugar otra vez? Escribe \"si\" o \"no\": ").lower()
  while jugar_otra not in ("si","no"):
    jugar_otra = input("Escribe \"si\" o \"no\": ").lower()

  if jugar_otra == "no":
    jugar_trivia = False

#Resultados de todos los intentos realizados y despedida al jugador
os.system ("clear")
print("Resumen de intentos:")
intento = 1
for p in puntajes:
  print("\tIntento {}: {} puntos".format(intento,p))

print("Gracias por jugar")
print("Hasta la proxima")
