import socket
import random

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Aguardando conexão de um cliente')

conn, ender = s.accept()
print ('Conectado em ', ender)

while True:
    data = conn.recv(1024)
    dataConvertido = int.from_bytes(data, byteorder='big')
    
    if(len(str(dataConvertido)) > 10):


    if not data:
        print ('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)