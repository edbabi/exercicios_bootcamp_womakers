import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()
#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute('UPDATE clientes SET saldo = 2 WHERE nome="Alessandro"')
saldo_atualizado = cursor.execute('SELECT * FROM clientes WHERE nome="Alessandro"')
for clientes in saldo_atualizado:
    print(clientes)

#b) Remova um cliente pelo seu ID.
cursor.execute('DELETE FROM clientes WHERE nome = "Luiz Fernando"')
clientes_apos_exclusao = cursor.execute('SELECT COUNT(*) FROM clientes WHERE nome = "Luiz Fernando"')
for clientes in clientes_apos_exclusao:
    print(clientes)

conexao.commit()
conexao.close()