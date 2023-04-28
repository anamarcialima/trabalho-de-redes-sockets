import socket
import random
import string

HOST = 'localhost'
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

print ('Aguardando conexão de um cliente')

conn, ender = s.accept()
print ('Conectado em ', ender)

data = conn.recv(1024) # recebe número aleatório em bytes 
dataConvertido = int.from_bytes(data, byteorder='big') # número em bytes covertido para inteiro
print("Número aleatório recebido:", dataConvertido)

tamanhoData = len(str(dataConvertido))

if tamanhoData > 10:
    stringAleatoria = ''.join(random.choices(string.ascii_uppercase, k = len(str(dataConvertido)))) # gerar string aleatória
    print("String aleatória gerada: ", stringAleatoria)
    
    s.sendall(str.encode(stringAleatoria)) # enviar para o cliente
    
else:
    if dataConvertido % 2 == 0:
        print("PAR")
        #mandar para cliente
    else:
        print("IMPAR")
        #mandar para cliente

if not data:
    print ('Fechando a conexão')
    conn.close()
        
conn.sendall(data)