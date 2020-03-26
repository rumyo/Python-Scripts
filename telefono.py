#Programa para encontrar numeros telefonicos con el formato 000-000-0000

def search_number(text):
    if len(text) !=12:     #reviso que el texto tenga una longitud de 12 caracteres
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True #si el formato del telefono es correcto retorna true

message = "Hello, I'm Nathaly. Call me at 621-453-1254 tomorrow. If I don't answer try 321-654-7521, which is my office number"

for i in range(len(message)):
    number = message[i:i+12] #Corto el mensaje en 12 caracteres
    if search_number(number):
        print("Phone number found: "+ number)
print("Finalizado")
