tasks = {"todo": [], "doing": [], "done": []}

def mostrar_quadro():
    print("\n=== TASKTRACKER ===")
    for coluna in tasks:
        print(f"\n[{coluna.upper()}]")
        for i, tarefa in enumerate(tasks[coluna]):
            print(f"  {i}. {tarefa}")
    print("\n===================")

while True:
    mostrar_quadro()
    print("1. Adicionar | 2. Editar | 3. Mover | 4. Limpar | 5. Sair")
    opcao = input("Escolha uma opcao: ")

    if opcao == '1':
        texto = input("Digite a tarefa: ")
        coluna = input("Qual coluna (todo, doing, done)? ")
        if coluna in tasks:
            tasks[coluna].append(texto)

    elif opcao == '2':
        coluna = input("Qual coluna (todo, doing, done)? ")
        if coluna in tasks:
            idx = int(input("Numero da tarefa (veja no painel): "))
            novo_texto = input("Novo texto: ")
            tasks[coluna][idx] = novo_texto

    elif opcao == '3':
        origem = input("De qual coluna? ")
        destino = input("Para qual coluna? ")
        if origem in tasks and destino in tasks:
            idx = int(input("Numero da tarefa: "))
            tarefa = tasks[origem].pop(idx)
            tasks[destino].append(tarefa)

    elif opcao == '4':
        coluna = input("Qual coluna limpar (todo, doing, done, todas)? ")
        if coluna in tasks:
            tasks[coluna].append(texto) # isso tava errado na logica mental, vou corrigir pra [] no print
            tasks[coluna] = []
        elif coluna == 'todas':
            tasks = {"todo": [], "doing": [], "done": []}

    elif opcao == '5':
        break