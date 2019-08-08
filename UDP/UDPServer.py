import socket

UDP_HOST = ''

PORT = 2019

#Criando o socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (UDP_HOST, PORT)

print("Rodando...")

#Aguardando mensagens pela porta
udpSocket.bind(orig, "3000")

while True:
	msg, client = udpSocket.recvfrom(1024)
	print(client, '\n', msg.decode())

	if msg:
		response = ("Resposta da mensagem: " + msg.decode()).encode()
		sent = udpSocket.sendto(response, client)

udpSocket.close()
