#Bibliotecas:
#Bibliotecas sao como extensoes, funcoes extras possiveis de adicionar no Python.
#Python ja vem com algumas bibliotecas
import time, random, qrcode
from decimal import Decimal

# print("Um momento..")
# time.sleep(3)
# print("YaY!")

# while True:
#     random_number = random.randint(1,100)  #Random+int numero inteiro aleatorio
#     print(random_number)
#     time.sleep(1)
#     if random_number %2 == 0:
#         break

# img = qrcode.make("https://www.youtube.com/@lyvvoc")
# img.save("qr_canal.png")


numero_decimal = Decimal(input("Digite um numero decimal:"))
print(type(numero_decimal))