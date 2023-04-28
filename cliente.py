import socket
import random
import string
from time import sleep

HOST = '127.0.0.1'
PORT = 5000

while True:

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    inteiroAleatorio = random.randint(0, 999999999999999999999999999999) # gera um número aleatório de até 30 casas
    inteiroAleatorioEmBytes = inteiroAleatorio.to_bytes(inteiroAleatorio.bit_length() + 7 // 8, byteorder='big') # converte o número aleatório gerado em bytes | (inteiroAleatorio.bit_length() + 7 // 8) faz o calculo do número de bytes necessários para aquele número aleatório
    s.sendall(inteiroAleatorioEmBytes)  # manda número aletório convertido em bytes para o servidor 
    print('Inteiro aleatório gerado', inteiroAleatorio)

    resposta = s.recv(1024) # recebe resposta do servidor 
    print("Resposta", resposta)

    s.sendall(resposta) # devolve valor recebido do servidor

    print("FIM")

    s.close() # fecha a conexão

    sleep(10)

