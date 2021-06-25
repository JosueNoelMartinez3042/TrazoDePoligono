import turtle as t

lados = int(input("Ingresa los lados: "))
def DDA():
        angulo=0
        x1=1
        y1=1
        x2=2
        y2=6
        n=lados

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
        print('DDA')
        print('dx: '+str(dx))
        print('dy: '+str(dy))
        print('Steps: '+str(steps))
        print('Xincremeto: '+str(xInc))
        print('Yincremento: '+str(yInc))

        for i in range(steps, int(steps+1)):
            t.setx(x1)
            t.sety(y1)

            angulo=float(180-(((n-2)/n)*180))
            print('Angulo: '+str(angulo))
            print('X         Y')
            for i in range(n):
                t.left(angulo)
                t.fd(0)
                for i in range(ln):
                    t.fd(25)
                    t.color("blue")
                    p=t.pos()
                    print('\n'+str(p))
                    for i in range(4):
                        t.forward(25)
                        t.left(90)
                t.forward(25)

def BRESENHAMS():
    angulo=0
    x1=4
    y1=2
    x2=4
    y2=6
    n=lados

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2*dy - x1
    x = x1
    y = y1
    ln = (p)

    t.setx(x)
    t.sety(y)

    print('Bresenhams')
    print('dx: '+str(dx))
    print('dy: '+str(dy))
    print('p: '+str(p))
    print('X   Y')
    angulo=float(180-(((n-2)/n)*180))
    print('Angulo: '+str(angulo)+'\n')
    while (x <= x2):
            x+=1
            if p < 0:
                p=p + 2 * dy
            else:
                p=p + (2*dy) -(2*dx)
                y+=1
                angulo=float(180-(((n-2)/n)*180))
                for i in range(n):
                    t.left(angulo)
                    t.fd(0)
                    for i in range(ln):
                        t.fd(25)
                        t.color("red")
                        ps=t.pos()
                        print('\n'+str(ps))
                        for i in range(4):
                            t.forward(25)
                            t.left(90)
                    t.forward(25)             
def menu():
   print("---SELECCIONE UN METODO---")
   print("1. DDA")
   print("2. BRESENHAMS")
def switch(case):
    if case == 1:
        DDA()
    elif case == 2:
        BRESENHAMS()

if __name__=='__main__':
   a=1
   b=1
   menu()
   case=0
   case = int(input("SELECCIONE EL METODO: ")) 
   switch(case)
t.mainloop()