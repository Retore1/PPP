def sum(x,y):
  suma= x + y
  return suma
def mul(x,y):
  multiplicacion=x*y
  return multiplicacion
def poten(x,y):
  potencia = x^y
  return potencia
def resta (x,y):
  resta=x-y
  return resta
def div(x,y):
    division=x/y
    return division

x=int(input("insertar numero :"))
y=int(input("insertar numero:"))
insertarsigno=input("insertarsigno:")
if insertarsigno == "+":
    sum(x,y)
    print(sum(x,y))
if insertarsigno == "-":
    resta(x,y)
    print(resta(x,y))
if insertarsigno == "*":
    mul(x,y)
    print(sum(x,y))
if insertarsigno == "/":
    div(x,y)
    print(div(x,y))
