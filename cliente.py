import socket
import random

HOST = '127.0.0.1'
PORT = 5000

inteiroAleatorio = random.randint(0, 999999999999999999999999999999) # gera um número aleatório de até 30 casas

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(inteiroAleatorio.to_bytes(inteiroAleatorio.bit_length() + 7 // 8, byteorder='big')) # converte o número aleatório gerado em bytes para mandar para o servidor. encode converte string. inteiroAleatorio.bit_length() + 7 // 8 faz o calculo do número de bytes necessários para aquele número aleatório
data = s.recv(1024)

print('Mensagem ecoada:', int.from_bytes(data, byteorder='big')) # converte o número de bytes em inteiro