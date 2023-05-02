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

Com isso, o programa cliente.py gera um número aleatório ente o intervalo de 0 e 999999999999999999999999999999, ou seja um número de até 30 casas:
inteiroAleatorio = random.randint(0, 999999999999999999999999999999)

Ademais, o programa cliente.py converte o número gerado para bytes usando a função to_bytes. A mesma recebe como parâmetro o número de bits necessários e a ordem de bytes (little ou big)
inteiroAleatorioEmBytes = inteiroAleatorio.to_bytes((inteiroAleatorio.bit_length() + 7) // 8, byteorder='big')

OBS: Como número de casas pode ser váriavel, o calculo (inteiroAleatorio.bit_length() + 7) // 8) é realizado para se adequar a cada valor gerado.

Tendo em vista isso o programa cliente.py envia o inteiroAleatorioEmBytes para o servidor:
s.sendall(inteiroAleatorioEmBytes)

Já no programa servidor.py a variavel inteiroAleatorioEmBytes armazena o valor recebido pelo cliente
inteiroAleatorioEmBytes = conn.recv(1024)
