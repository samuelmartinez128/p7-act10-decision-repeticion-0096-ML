#Samuel Martinez NC 0096
# IF
print("+-+-IF+-+-")
#EJEMPLO 1
print("EJEMPLO 1")
a = 33
b = 200
if b > a:
  print("b es mas grande que a")
#EJEMPLO 2
print("EJEMPLO 2")
number = 15
if number > 0:
  print("El numero es positivo")
# ELIF
print("+-+-ELIF+-+-")
#EJEMPLO 1
print("EJEMPLO 1")
a = 33
b = 33
if b > a:
  print("b es mas grande a")
elif a == b:
  print("a y b son iguales")
#EJEMPLO 2
print("EJEMPLO 2")
score = 75
if score >= 90:
  print("Cali: A")
elif score >= 80:
  print("Cali: B")
elif score >= 70:
  print("Cali: C")
elif score >= 60:
  print("Cali: D")
# ELSE
print("+-+-ELSE+-+-")
#EJEMPLO 1
print("EJEMPLO 1")
a = 200
b = 33
if b > a:
  print("b mayor que a")
elif a == b:
  print("a y b son iguales")
else:
  print("a mayor que b")
#EJEMPLO 2  
print("EJEMPLO 2")
a = 200
b = 33
if b > a:
  print("b mayor que a")
else:
  print("b mo es mayor que a")
# CICLO FOR
print("+-+-FOR LOOPS+-+-")
#EJEMPLO 1
print("EJEMPLO 1")
fruits = ["manzana", "banana", "coco"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#EJEMPLO 2
print("EJEMPLO 2")
fruits = ["manzana", "banana", "snadia"]
for x in fruits:
  if x == "banana":
    break
  print(x)
# CICLO WHILE
print("+-+-While Loops+-+-")
#EJEMPLO 1
print("EJEMPLO 1")
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
#EJEMPLO 2
print("EJEMPLO 2")
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print("Samuel Martinez NC 0096")