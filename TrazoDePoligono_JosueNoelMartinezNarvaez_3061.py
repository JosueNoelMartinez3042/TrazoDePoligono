import turtle as t

def DDA():
   
        x1=2
        y1=2
        x2=2
        y2=6
        n=0

        dx = abs(x2 - x1)
        dy = abs(y2 - y1)
        steps = 0
    
        if (dx) > (dy):
            steps = (dx)
        else:
            steps = (dy)
          
        xInc = float(dx / steps)
        yInc = float(dy / steps)

        xInc = round(xInc,1)
        yInc = round(yInc,1)

        ln = steps 
        print("ALGORITMO DDA")
        GRAFICA()

def BRESENHAMS():
    
    x1=4
    y1=2
    x2=4
    y2=6
    n=0

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2*dy - x1

    x = x1
    y = y1

    ln = (p)

    t.setx(x)
    t.sety(y)

    print("ALGORITMO BRESENHAM")
    GRAFICA()
    while (x <= x2):
            x+=1
            if p < 0:
                p=p + 2 * dy
            else:
                p=p + (2*dy) -(2*dx)
                y+=1

def GRAFICA():
    t.title("Poligono de N lados")
    t.pencolor('blue')
    t.speed(1)
    t.setup(700, 700)
    t.penup()
    t.fd(-50) 
    t.right(90)
    t.fd(200)
    t.right(-90)
    t.pendown()
    t.pensize(3)
    n = int(input("Ingresa el numero de lados: "))
    angle = 180*(n-2)/n
    print("Coordenadas")
    for i in range(n):
        t.fd(40)
        t.dot('Black')
        t.left(180-angle)
        p=t.pos ()
        print('\n'+str(p))
        t.done  
        
def error():
   print ("Opcion Invalida")

def menu():
   print("--SELECCIONE UN METODO--")
   print("1. DDA")
   print("2. BRESENHAMS")
   
def switch(case):
    if case == 1:
        DDA()
    elif case == 2:
        BRESENHAMS()
    else:
        return error()

if __name__=='__main__':
   a=1
   b=1
   menu()
   case=0
   case = int(input("SELECCIONE EL METODO: ")) 
   switch(case)
   t.mainloop()