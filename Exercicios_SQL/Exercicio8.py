import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). 
cursor.execute('CREATE TABLE compras(id INTEGER PRIMARY KEY, cliente_id INTEGER, produto TEXT, valor REAL, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')

#Insira algumas compras associadas a clientes existentes na tabela "clientes".

cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(1,7,"Iphone 13",5570)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(2,7,"Mala de viagem",200)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(3,1,"Ventilador",150)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(4,1,"Relógio",550)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(5,3,"Vestido",224.99)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(6,3,"Scarpin couro",99.15)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(7,2,"Vara de pescar",355.60)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(8,2,"Bota",450)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(9,6,"Moto Yamaha ",18000)')
cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) values(10,6,"Capacete",179.99)')

#Escreva uma consulta para exibir o nome do cliente, o produto e o #valor de cada compra.

compra_cliente = cursor.execute('SELECT nome, produto, valor FROM clientes INNER JOIN compras ON clientes.id = compras.cliente_id')
for clientes in compra_cliente:
   print(clientes)

conexao.commit()
conexao.close()
