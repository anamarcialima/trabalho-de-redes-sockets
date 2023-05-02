import socket
import random
import string
from time import sleep

HOST = 'localhost'
PORT = 5000

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))

    s.listen()
    print ('Aguardando conexão de um cliente')

    conn, ender = s.accept() # aceita a conexão com cliente
    print ('Conectado em', ender)
    print("")
    
    inteiroAleatorioEmBytes = conn.recv(1024) # recebe número aleatório em bytes 
    inteiroAleatorio = int.from_bytes(inteiroAleatorioEmBytes, byteorder='big') # número em bytes covertido para inteiro
    print("Inteiro aleatório recebido:", inteiroAleatorio)

    if len(str(inteiroAleatorio)) > 10:
        stringAleatoria = ''.join(random.choices(string.ascii_uppercase, k = len(str(inteiroAleatorio)))) # gera string aleatória
        print("String aleatória gerada:", stringAleatoria)
        print("")
        
        conn.sendall(str.encode(stringAleatoria)) # enviar string aleatória para o cliente
        
    else:
        if inteiroAleatorio % 2 == 0:
            conn.sendall(str.encode("PAR"))
        else:
            conn.sendall(str.encode("IMPAR"))

