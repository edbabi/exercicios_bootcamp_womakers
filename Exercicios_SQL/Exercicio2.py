import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1,"Alexandre",19,"Ciência da Computação")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2,"Luiza",39,"Ciência de Dados")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3,"Aline",18,"Estatística")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4,"Vitória",26,"Arquitetura")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5,"Tayná",27,"Arquitetura")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(6,"Isaque",23,"Engenharia Elétrica")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(7,"Italo",21,"Engenharia da Computação")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(8,"Luiz Fernando",27,"Engenharia de Produção")')

conexao.commit()
conexao.close()