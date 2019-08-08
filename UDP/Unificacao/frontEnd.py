import socket

UDP_HOST = '127.0.0.1'

PORT = 2019
#Criando o socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#Destino para onde a mensagem será enviada
dest = (UDP_HOST, PORT)

##----------------------------------
#	Lado cliente do banco
##----------------------------------

ok = True
while ok:
	
	# Menu Inicio 
	print ("")
	print ("1 - Cliente")
	print ("2 - Transaçao")
	print ("3 - Sair")

	menuop = input("Digite o numero da opção desejada: ")

	#Fecha aplicação
	if menuop == '3':
		ok = False

	#Menu cliente
	if menuop == '1':
		ok1 = True
		while ok1:
			print("")
			print("1 - Inserir novo cliente")
			print("2 - Consultar dados de um cliente")
			print("3 - Atualizar cadastro de um cliente")
			print("4 - Remover um clientes")
			print("5 - Imprimir lista de clientes")
			print("6 - Voltar")

			menuCliente = input ("\nDigite o numero da opçao desejada: ")

			#Sair do menu cliente
			if menuCliente == '6':
				ok1 = False
			
			## 1 - Inserir novo cliente
			if menuCliente == '1':
				cod = input ("\nInforme o codigo do cliente: ")
				nome = input ("Informe o nome do cliente: ")
				tel = input ("Informe o telefone do cliente: ")
				cc = input ("Informe o numero da conta corrente do cliente: ")
				pdeposito = input ("Informe o valor do deposito inicial: ")
				pdeposito = float(pdeposito)

				#Enviar dados para o servidor para realizar o cadastro

				#Criando a mensagem a ser enviada
				msg = 'Cadastro, {}, {}, {}, {}, {}'.format(cod, nome, tel, cc, pdeposito)

				#Enviando a mensagem
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta - Usuuário cadastrado
				response, server = udpSocket.recvfrom(1024)
				print(response.decode())

			## 2 - Consultar dados de um cliente
			if menuCliente == '2':
				search = input("\nInforme o codigo do cliente: ")

				#Criando a mensagem
				msg = "Consultar Cliente, {}".format(search)

				#Enviando a requisição de consultar usuário
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta
				response, server = udpSocket.recvfrom(1024)
				if response:
					print(response.decode())
				

			## 3 - Atualizar dados do cliente
			if menuCliente == '3':
				search = input("\nInforme o codigo do cliente: ")

				#Criando a mensagem
				msg = "Consultar Cliente, {}".format(search)

				#Enviando a requisição de consultar usuário
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta
				response, server = udpSocket.recvfrom(1024)

				if response.decode() != "\nServer-> Usuário não encontrado":
					print(response.decode())
					newName = input("\nInforme o novo nome do cliente: ")
					newPhone = input("Informe o novo telefone do cliente: ")

					# Criando mensagem para atualizar os dados do cliente
					msg = "Atualizar dados, {}, {}, {}".format(search, newName, newPhone)

					#Enviando mensagem
					udpSocket.sendto(msg.encode(), dest)

					#Resposta
					response, server = udpSocket.recvfrom(1024)

					if response:
						print(response.decode())
				else:
					print(response.decode())

			## 4 - Remover clientes
			if menuCliente == '4':
				search = input("\nInforme o codigo do cliente: ")

				#Criando a mensagem
				msg = "Remover Cliente, {}".format(search)

				#Enviando a requisição de consultar usuário
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta
				response, server = udpSocket.recvfrom(1024)

				if response:
					print(response.decode())

			## 5 - Imprimir lista de clientes
			if menuCliente == '5':
				
				#Criando mensagem
				msg = "Lista usuarios, 0"

				#Enviando mensagem
				udpSocket.sendto(msg.encode(), dest)

				#Resposta
				response, server = udpSocket.recvfrom(10000)

				if response:
					print(response.decode())

	if menuop == '2':
		ok2 = True
		print("")
		print("1 - Deposito")
		print("2 - Saque")
		print("3 - Transferencia")
		print("4 - Imprimir lista de transaçoes")
		print("5 - Voltar")

		opmenu = input("\nInforme o numero da opção desejada")

		## 5 - Sair do menu de transações
		if opmenu == '5':
			ok2 = False

		## 1 - Deposito
		if opmenu == '1':
			search = input("\nInforme o codigo em que deseja realizar o deposito: ")

			#Criando a mensagem
			msg = "Consultar Cliente, {}".format(search)

			#Enviando a requisição de consultar usuário
			udpSocket.sendto(msg.encode(), dest)

			#Recebendo a resposta
			response, server = udpSocket.recvfrom(1024)

			if response.decode() != "\nServer-> Usuário não encontrado":
				pos = Contas['cod'].index(search)
				deposit = input("\n Informe o valor do deposito: ")
				deposit = float(deposit)
				
				# Criando mensagem de deposito
				msg = "Deposito, {}, {}".format(search, deposit)

				#Enviando a requisição de consultar usuário
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta
				response, server = udpSocket.recvfrom(1024)
				if response:
					print(response.decode())
			
			else:
				print(response.decode())

		## 2 - Saque
		if opmenu == '2'
			search = input("\nInforme o codigo em que deseja realizar o saque: ")
			#Criando a mensagem
			msg = "Consultar Cliente, {}".format(search)

			#Enviando a requisição de consultar usuário
			udpSocket.sendto(msg.encode(), dest)

			#Recebendo a resposta
			response, server = udpSocket.recvfrom(1024)

			if response.decode() != "\n Server-> Codigo invalido":
				pos = Contas['cod'].index(search)
				saque = input("\n Informe o valor do saque: ")
				saque = float(saque)

				# Criando mensagem de deposito
				msg = "Deposito, {}, {}".format(search, deposit)

				#Enviando a requisição de consultar usuário
				udpSocket.sendto(msg.encode(), dest)

				#Recebendo a resposta
				response, server = udpSocket.recvfrom(1024)
				if response:
					print(response.decode())			
			else:
				print(response.decode())

		## 3 - Tranferencia

		if opmenu == '3'
			#Confirmação da conta Origem
			searchOrigem = input("\nInforme o codigo eda conta origem: ")
			#Criando a mensagem
			msg = "Consultar Conta, {}".format(searchOrigem)

			#Enviando a requisição de consultar usuário
			udpSocket.sendto(msg.encode(), dest)

			#Recebendo a resposta
			response, server = udpSocket.recvfrom(1024)

			if response != "\nServer-> Conta não encontrada":
				print("Origem \n", response.decode())
			else:
				print(response.decode())
				break

			#Confirmação da conta destino
			searchDestino = input("\nInforme o codigo eda conta origem: ")
			#Criando a mensagem
			msg = "Consultar Conta, {}".format(searchDestino)

			#Enviando a requisição de consultar usuário
			udpSocket.sendto(msg.encode(), dest)

			#Recebendo a resposta
			response, server = udpSocket.recvfrom(1024)

			if response != "\nServer-> Conta não encontrada":
				print("Origem \n", response.decode())
			else:
				print(response.decode())
				break

			tranfer = input("\n Informe o valor para transferencia: ")
			transfer = float(saque)

			# Criando mensagem de deposito
			msg = "Transferencia, {}, {}".format(searchOrigem, searchDestino, valor)

			#Enviando a requisição de consultar usuário
			udpSocket.sendto(msg.encode(), dest)

			#Recebendo a resposta
			response, server = udpSocket.recvfrom(1024)
			
			if response:
				print(response.decode())			
			




udpSocket.close()