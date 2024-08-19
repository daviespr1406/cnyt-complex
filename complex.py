import math

def division (x,y):
    real = ((x[0]*y[0])+(x[1]*y[1]))/((y[0]**2)+(y[1]**2))
    imaginaria = ((y[0]*x[1])-(x[0]*y[1]))/((y[0]**2)+(y[1]**2))
    return (real,imaginaria);

def suma (x,y):
    real = ((x[0]+y[0]))
    imaginaria = ((y[1]+x[1]))
    return (real,imaginaria);

def resta (x,y):
    real = ((x[0]-y[0]))
    imaginaria = ((x[1]-y[1]))
    return (real,imaginaria);

def multiplicacion (x,y):
    real = ((x[0]*y[0])-(x[1]*y[1]))
    imaginaria = ((x[0]*y[1])+(x[1]*y[0]))
    return (real,imaginaria);

def modulo(x):
    modu = math.sqrt((x[0]**2)+(x[1]**2))
    return modu
def conjugado(x):
    conju = (x[0],x[1]*-1)
    return conju
def fase(x):
    fas = math.atan2(x[1], x[0])
    return fas
def cartPolar(x):
    return(modulo(x),fase(x))
def polarCart(x):
    real = x[0]*math.cos(x[1])
    imaginaria = x[0]*math.sin(x[1])
    return (real,imaginaria)
def prettyPrintingC(x):
    if x[0] == 0:
        print (x[1],"i")
    elif x[1] == 0:
        print (x[0])
    elif x[1] == 1:
        print (x[0],"+","i")
    else:
        print (x[0],"+",x[1],"i")

def main():
    x = polarCart((8.54400374531753,-1.2120256565243244))
    prettyPrintingC(x)
    print (fase((3,-8)))
main()
