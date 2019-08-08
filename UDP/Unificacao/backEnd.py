import socket

Contas = {'cod' : ["1", "2", "3"], 'saldo' : [500.0, 200.0, 150.0], 'tr' : []}
Clientes = {'cod' : ["1", "2", "3"], 'nome' : ["Douglas", "Willian", "José"], 'tel' : ["9999", "6666", "1111"], 'cc' : ["1", "2", "3"]}
numClientes = 3

UDP_HOST = ''

PORT = 2019

#Criando o socket UDP
udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
orig = (UDP_HOST, PORT)

print("Rodando...")


#Aguardando mensagens pela porta
udpSocket.bind(orig)

while True:
		msg, client = udpSocket.recvfrom(1024)
		
		if msg:
			array = msg.decode().split(', ')
			
			if array[0] == "Cadastro":
				print("cadastrando...")
				Clientes['cod'].append(str(array[1]))
				Clientes['nome'].append(str(array[2]))
				Clientes['tel'].append(str(array[3]))
				Clientes['cc'].append(str(array[4]))
				Contas['cod'].append(str(array[4]))
				Contas['saldo'].append(float(array[5]))
				

				numClientes = numClientes + 1
				response = "\nServer-> Usuário cadastrado!!!!!"
				udpSocket.sendto(response.encode(), client)
			
			if array[0] == "Consultar Cliente":
				if array[1] in Clientes['cod']:
					pos = Clientes['cod'].index(array[1])
					response = "Codigo \t Nome \t\t Telefone \t Conta\n{0} \t {1} \t {2} \t {3} \t {4}".format(Clientes['cod'][pos], 
						Clientes['nome'][pos],Clientes['tel'][pos],Clientes['cc'][pos],Contas['saldo'][pos])
				else:
					response = "\nServer-> Usuário não encontrado"

				udpSocket.sendto(response.encode(), client)

			if array[0] == "Consultar Conta":
				if array[1] in Clientes['cc']:
					pos = Contas['cod'].index(array[1])
					response = "Codigo \t Nome \t\t Telefone \t Conta\n{0} \t {1} \t {2} \t {3} \t {4}".format(Clientes['cod'][pos], 
						Clientes['nome'][pos],Clientes['tel'][pos],Clientes['cc'][pos],Contas['saldo'][pos])
				else:
					response = "\nServer-> Conta não encontrada"

				udpSocket.sendto(response.encode(), client)

			if array[0] == "Atualizar dados":
				print("atulizando...")
				pos = Clientes['cod'].index(array[1])
				print(pos)
				Clientes['nome'][pos] = str(array[2])
				Clientes['tel'][pos] = str(array[3])

				response = "\nServer-> Usuário atualizado!!!!!"
				udpSocket.sendto(response.encode(), client)

			if array[0] == "Remover Cliente":
				if array[1] in Clientes['cod']:
					pos = Clientes['cod'].index(array[1])
					Clientes['cod'].pop(pos)
					Clientes['nome'].pop(pos)
					Clientes['tel'].pop(pos)
					Clientes['cc'].pop(pos)
					Contas['cod'].pop(pos)
					Contas['saldo'].pop(pos)

					numClientes = numClientes - 1

					response = "\nServer-> Usuário Removido"
				else:
					response = "\n Server-> Codigo invalido"
				udpSocket.sendto(response.encode(), client)
			
			if array[0] == "Lista usuarios":
				print("criando tabela")
				response = "Codigo \t Nome \t\t Telefone \t Conta \t Saldo\n"

				usuarios = ''

				for i in range(numClientes):
					usuarios += "{} \t {} \t {} \t {} \t {}\n".format(Clientes['cod'][i],Clientes['nome'][i],
            	Clientes['tel'][i],Clientes['cc'][i], Contas['saldo'][i])

				response = response + usuarios

				udpSocket.sendto(response.encode(), client)

			if array[0] == "Deposito":
				pos = Contas['cod'].index(array[1])
				valor = Contas['saldo'][pos]
				valor = valor + float(array[2])
				Contas['saldo'][pos] = valor

				response = "\nServer-> Deposito realizado"
				udpSocket.sendto(response.encode(), client)

			if array[0] == "Saque":
				pos = Contas['cod'].index(array[1])
				# Atualizando valor da conta
				valor = Contas['saldo'][pos]
				valor = valor - deposito
				Contas['saldo'][pos] = valor

				response = "\nServer-> Saque realizado"
				udpSocket.sendto(response.encode(), client)

			if array[0] == "Transferencia":
				posOrigem = Contas['cod'].index(array[1])
				posDestino = Contas['cod'].index(array[2])

				transfer = array[3]

				ValorOrigem = Contas['saldo'][posOrigem]
				ValorOrigem = Contas['saldo'][posDestino]

				if ValorOrigem > saque:
					ValorOrigem -= transfer
					Contas['saldo'][posOrigem] = ValorOrigem
					ValorDestino += transfer
					Contas['saldo'][posDestino] = ValorDestino
					response = "\nTransferencia concluida"
				else:
					response = "\nSaldo insuficiente na conta origem"

				udpSocket.sendto(response.encode(), client)



		##estado do servidor
		print("Codigo \t Nome \t\t Telefone \t Conta \t Saldo")
		print()
		for i in range(numClientes):              

			print("{} \t {} \t {} \t {} \t {}".format(Clientes['cod'][i],Clientes['nome'][i],
            	Clientes['tel'][i],Clientes['cc'][i], Contas['saldo'][i]))