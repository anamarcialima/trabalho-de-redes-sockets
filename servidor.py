import socket
import random
import string

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Aguardando conexão de um cliente')

conn, ender = s.accept() # aceita a conexão com cliente
print ('Conectado em ', ender)

inteiroAleatorio = conn.recv(1024) # recebe número aleatório em bytes 
inteiroAleatorioEmBytes = int.from_bytes(inteiroAleatorio, byteorder='big') # número em bytes covertido para inteiro
print("Número aleatório recebido:", inteiroAleatorioEmBytes)

if len(str(inteiroAleatorioEmBytes)) > 10:
    stringAleatoria = ''.join(random.choices(string.ascii_uppercase, k = len(str(inteiroAleatorioEmBytes)))) # gerar string aleatória
    print("String aleatória gerada: ", stringAleatoria)
    
    conn.sendall(str.encode(stringAleatoria)) # enviar string aleatória para o cliente
    
else:
    if inteiroAleatorioEmBytes % 2 == 0:
        conn.sendall(str.encode("PAR"))
    else:
        conn.sendall(str.encode("IMPAR"))