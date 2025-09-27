# practica-3


SE USO PYTHON 3.10
SE IMPLEMENTO EL USO DE IA PARA RESOLVER PROBLEMAS DE SINTAXIS Y ORTOGRAFIA DEL README 

python
import turtle
Importa la librería para dibujar.

python
pantalla = turtle.Screen()
tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.penup()
Prepara la pantalla y la tortuga para dibujar rápido.

python
f = open("matriz.txt", "w")
for i in range(100):
    linea = ""
    for j in range(100):
        num = (i + j) % 10
        linea += str(num)
    f.write(linea + "\n")
f.close()
Crea el archivo con 100 filas de 100 números cada una.

python
f = open("matriz.txt", "r")
matriz = []
for linea in f:
    fila = []
    for char in linea:
        if char != "\n":
            fila.append(int(char))
    matriz.append(fila)
f.close()
Lee el archivo y guarda los números en una matriz.

python
x = 200
y = 200
tamaño = 5
Posición inicial y tamaño de cada cuadrito.

python
for i in range(100):
    for j in range(100):
        tortuga.goto(x + j*tamaño, y - i *tamaño)
Mueve la tortuga a la posición correcta para cada cuadrito.

python
num = matriz[i][j]
if num == 0: tortuga.color("purple")
elif num == 1: tortuga.color("gold")
# ... (asigna colores del 2 al 9)
Elige el color según el número leído.

python
tortuga.pendown()
tortuga.begin_fill()
for k in range(4):
    tortuga.forward(tamaño)
    tortuga.right(90)
tortuga.end_fill()
tortuga.penup()
Dibuja un cuadrito relleno con el color elegido.

python

pantalla.exitonclick()
