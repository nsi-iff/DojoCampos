#coding:utf-8
from random import randrange

lista_ticket = []
resultado=[]
cont = 0


while len(lista_ticket)!=3:
	numero = input("Entre com o número: ")
	if numero in lista_ticket:
		print("Esse número ja foi selecionado")
	else:
		lista_ticket.append(numero)


while lista_ticket<>resultado:
	resultado = []
	while len(resultado)!=3:
		x = randrange(1,11)
			
	if not (x in resultado):
		resultado.append(x)
	cont += 1

print cont



