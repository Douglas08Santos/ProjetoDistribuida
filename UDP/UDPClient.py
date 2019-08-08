import socket

UDP_HOST = '127.0.0.1'

PORT = 2019
#Criando o socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Destino para onde a mensagem será enviada
dest = (UDP_HOST, PORT)
print()
print("Ctrl + X p/ sair\n")

msg = "Hello, World"

#Enquanto a msg não for vazio, a aplicação continua

	#Enviando mensagem
	udpSocket.sendto(msg.encode(), dest)

	#Recebendo resposta
	response, server = udpSocket.recvfrom(1024)
	print(response.decode())
	#Nova mensagem
	msg = input()

udpSocket.close()
