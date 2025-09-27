import turtle

# Configurar la pantalla y la tortuga
pantalla = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.penup()

# Crear archivo con números del 0 al 9
archivo = open("matriz.txt", "w")
for fila in range(100):
    linea = ""
    for columna in range(100):
        numero = (fila + columna) % 10
        linea += str(numero)
    archivo.write(linea + "\n")
archivo.close()

# Leer el archivo creado
archivo = open("matriz.txt", "r")
matriz = []
for linea in archivo:
    fila = []
    for caracter in linea:
        if caracter in "0123456789":
            fila.append(int(caracter))
    matriz.append(fila)
archivo.close()

# Posición inicial para dibujar
x = -200
y = 200
tamaño = 4

# Dibujar cada número de la matriz
for i in range(100):
    for j in range(100):
        # Mover a la posición correspondiente
        tortuga.goto(x + j * tamaño, y - i * tamaño)
        
        # Obtener el número de la matriz
        numero = matriz[i][j]
        
        # Asignar color según el número
        if numero == 0:
            color = "black"
        elif numero == 1:
            color = "red"
        elif numero == 2:
            color = "green"
        elif numero == 3:
            color = "blue"
        elif numero == 4:
            color = "yellow"
        elif numero == 5:
            color = "orange"
        elif numero == 6:
            color = "purple"
        elif numero == 7:
            color = "pink"
        elif numero == 8:
            color = "brown"
        else:
            color = "cyan"
        
        # Dibujar el cuadrito de color
        tortuga.pendown()
        tortuga.fillcolor(color)
        tortuga.begin_fill()
        
        for lado in range(4):
            tortuga.forward(tamaño)
            tortuga.right(90)
            
        tortuga.end_fill()
        tortuga.penup()

# Esperar click para cerrar
pantalla.exitonclick()
