import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#3. Consultas Básicas
#   Escreva consultas SQL para realizar as seguintes tarefas:
#   a) Selecionar todos os registros da tabela "alunos".

alunos_full = cursor.execute('SELECT * FROM alunos')
#for alunos in alunos_full:
#    print(alunos)

#   b) Selecionar o nome e a idade dos alunos com mais de 20 anos.

dados_maior_20 = cursor.execute('SELECT * FROM alunos where idade > 20')
#for alunos in dados_maior_20:
#    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.

alunos_enge = cursor.execute('SELECT * FROM alunos where curso like "Engenharia%" order by nome')
#for alunos in alunos_enge:
#    print(alunos)

conexao.commit()
conexao.close()