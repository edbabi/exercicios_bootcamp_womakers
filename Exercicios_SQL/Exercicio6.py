import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
#6. Consultas e Funções Agregadas
#   Escreva consultas SQL para realizar as seguintes tarefas:
#    a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.

dados_cliente_30 = cursor.execute('SELECT nome,idade FROM clientes WHERE idade>30')
for clientes in dados_cliente_30:
    print(clientes)

#   b) Calcule o saldo médio dos clientes.
media_saldo = cursor.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes;')
for clientes in media_saldo:
    print(clientes)

# c) Encontre o cliente com o saldo máximo
saldo_max = cursor.execute('SELECT MAX(saldo) FROM clientes')
for clientes in saldo_max:
    print(clientes)

# d) Conte quantos clientes têm saldo acima de 1000.
qtd_acima_mil = cursor.execute('SELECT count(*) FROM clientes WHERE saldo >1000')
for clientes in qtd_acima_mil:
    print(clientes)
    
conexao.commit()
conexao.close()