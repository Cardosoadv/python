import mysql.connector
from mysql.connector import errorcode
try:
	banco = mysql.connector.connect(host='localhost', user='root', password='root', database='myauth')
#	print("conectado com Sucesso!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("O Banco de Dados não existe")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Usuário ou Senha incorreto")
	else:
		print(error)