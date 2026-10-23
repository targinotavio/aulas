with open("notas.txt","r", encoding="utf-8") as arquivo:
    soma_notas = 0.0
    total_alunos = 0
    for linha in arquivo:
        dados = linha.strip().split(", ")
        nome = dados[0]
        nota = float(dados[1])
        print(f"Aluno: (nome), nota: (nota.1f)")
        soma_notas = soma_notas + nota
        total_alunos = total_alunos + 1

media = soma_notas/total_alunos
print (f"A media da turma é: {media:.1f}")