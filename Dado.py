import random
import time
numero = random.randint(1,6)
while True:
    user = input("que herramienta quieres usar")
    if user == "Dado":
        print("Lanzando dado...")
        time.sleep(2)
        print("el resultado del dado fue:",numero)
        numero = random.randint(1,6)
    else:
        print("no contamos con esa herramienta")
   