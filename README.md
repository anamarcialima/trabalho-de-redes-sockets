# trabalho-de-redes-sockets

A linguagem escolhida para esse trabalho foi o Python, tomando como base o código apresentado em sala de aula sobre programação de sockets.

Inicialmente em ambos os programas (cliente.py e servidor.py) são atribuídos valores para as varáveis HOST e PORT. 
HOST = '127.0.0.1'
PORT = 5000

Logo em seguida em ambos os programas é definido o protocolo que será utilizada na comunicação, sendo AF_INET a família de endereço IPv4 e SOCK_STREAM o tipo de nesse socket, nesse caso TCP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Assim, no programa servidor.py, o servidor incia a escuta de conexões através da função abaixo:
s.bind((HOST, PORT))

E faz o controle de conexões simultâneas que o servidor suportará:
s.listen()

Já no programa cliente.py o programa realiza a conexão com o servidor:
s.connect((HOST, PORT))

E o programa servidor.py aceita a conexão:
conn, ender = s.accept()


Com isso, o programa cliente.py gera um número aleatório ente o intervalo de 0 e 999999999999999999999999999999, ou seja um número de até 30 casas:
inteiroAleatorio = random.randint(0, 999999999999999999999999999999)

Ademais, o programa cliente.py converte o número gerado para bytes usando a função to_bytes. A mesma recebe como parâmetro o número de bits necessários e a ordem de bytes (little ou big)
inteiroAleatorioEmBytes = inteiroAleatorio.to_bytes((inteiroAleatorio.bit_length() + 7) // 8, byteorder='big')

OBS: Como número de casas pode ser váriavel, o calculo (inteiroAleatorio.bit_length() + 7) // 8) é realizado para se adequar a cada valor gerado.

Tendo em vista isso o programa cliente.py envia o inteiroAleatorioEmBytes para o servidor:
s.sendall(inteiroAleatorioEmBytes)

Já no programa servidor.py a variavel inteiroAleatorioEmBytes armazena o valor recebido pelo cliente:
inteiroAleatorioEmBytes = conn.recv(1024)

Além de converter o dado em bytes em inteiro novamente:
inteiroAleatorio = int.from_bytes(inteiroAleatorioEmBytes, byteorder='big')

Após fazer isso, o programa servidor também verifica se o número de casas do inteiro aleatório que foi recebido possui mais de 10 casas:
if len(str(inteiroAleatorio)) > 10

OBS: A função len verifica o número de casas apenas de strings, com isso, o inteiro foi transformado em string pela função str(), e assim a função len retorna a quantidade de casas que o inteiro trasnformado em string possui.

Se o codição for satisfeita o programa gera uma sequência de caractres maiusculos com o número de casas igual ao inteiroAleatorio 
stringAleatoria = ''.join(random.choices(string.ascii_uppercase, k = len(str(inteiroAleatorio))))

E assim, o programa servidor.py manda a string aleatória para o cliente.py
conn.sendall(str.encode(stringAleatoria))

Se condição não for satisfeita, ou seja se o número de casas do inteiro aleatório for menor que 10, é feito uma verificação se o inteiro é impar ou par e o resultado é enviado para o cliente.py
 else:
        if inteiroAleatorio % 2 == 0:
            conn.sendall(str.encode("PAR"))
        else:
            conn.sendall(str.encode("IMPAR"))


No programa cliente.py, a variavel recebe a resposta do servidor (a string aleatória ou se o inteiro aleatório é par ou ímpar)
resposta = s.recv(1024)

Por fim, no programa cliente.py a resposta é enviada novamente para o servidor
s.sendall(resposta) 

É imprimido uma string "FIM"
print("FIM")

E o socket é fechado
s.close()
