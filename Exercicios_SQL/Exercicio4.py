import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#4. Atualização e Remoção
#   a) Atualize a idade de um aluno específico na tabela.
cursor.execute('UPDATE alunos SET idade = 20 WHERE nome = "Tayná"')
#dados_aluno = cursor.execute('SELECT * FROM alunos2 WHERE nome = "Tayná"')
#for alunos in dados_aluno:
#    print(alunos)

#   b) Remova um aluno pelo seu ID.
cursor.execute('DELETE FROM alunos WHERE id=8')
dados_aluno = cursor.execute('SELECT * FROM alunos')
for alunos in dados_aluno:
    print(alunos)

conexao.commit()
conexao.close()