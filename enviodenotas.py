with open("notas.txt", "w", encoding="utf-8") as arquivo:

 for nomes in range(1,4):
    nome = input("Digite o nome do aluno:\n")
    nota = input("Digite a nota do aluno:\n")

    arquivo.write(f"NOME | {nome}\n NOTA| {nota}\n")