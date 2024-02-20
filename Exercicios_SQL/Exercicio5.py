import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela
cursor.execute('CREATE TABLE clientes2(id INTEGER PRIMARY KEY, nome VARCHAR(100),idade INTEGER,saldo FLOAT)')

#inserindo registros na tabela clientes
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(1,"Alessandro",46,1550.12)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(2,"Angelo",45,3599)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(3,"Jaqueline",42,10000.05)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(4,"Jorge",73,223455.89)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(5,"Helio",89,500000)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(6,"Isaque",23,29250.07)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(7,"Italo",21,22000)')
cursor.execute('INSERT INTO clientes2(id,nome,idade,saldo) VALUES(8,"Luiz Fernando",27,5500)')

dados_aluno = cursor.execute('SELECT * FROM clientes')
for alunos in dados_aluno:
    print(alunos)

conexao.commit()
conexao.close()