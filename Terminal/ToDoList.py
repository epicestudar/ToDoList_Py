tarefas = [] # criando um vetor para armazenar as tarefas

def adicionarTarefa():
    tarefa = input("Adicione a tarefa:")
    tarefas.append(tarefa) # adicionará a tarefa digitada no vetor tarefas[]
    print(f"Tarefa: {tarefa} adicionada na lista")

def listarTarefa():
    if not tarefas:
        print("Não há tarefas para serem visualizadas")
    else:
        print("Tarefas: ")
        for index, tarefa in enumerate(tarefas): # adicionando um loop de repetição que percorrerá o indíce da tarefa
            print(f"Tarefa #{index}. {tarefa}")

def  deletarTarefa():
    listarTarefa()
    try:
        tarefaDeletada = int(input("Selecione o número para a tarefa ser deletada"))
        if tarefaDeletada>=0 and tarefaDeletada < len(tarefas):
            tarefas.pop(tarefaDeletada)
            print(f"Tarefa {tarefaDeletada} deletada com sucesso")
        else:
            print(f"Tarefa {tarefaDeletada} não encontrada")

    except:
        print("Erro")


def editarTarefa():
    listarTarefa()
    try:
        indiceTarefa = int(input("Selecione o número da tarefa que deseja editar: "))
        if 0 <= indiceTarefa < len(tarefas):
            novaDescricao = input("Insira a nova descrição da tarefa: ")
            tarefas[indiceTarefa] = novaDescricao
            print(f"Tarefa #{indiceTarefa} editada com sucesso")
        else:
            print("Índice de tarefa inválido")
    except ValueError:
        print("Por favor, insira um número válido.")

def marcarComoConcluida():
    listarTarefa()
    try:
        indiceTarefa = int(input("Selecione o número da tarefa que deseja marcar como concluída: "))
        if 0 <= indiceTarefa < len(tarefas):
            tarefas[indiceTarefa] += " (Concluída)"
            print(f"Tarefa #{indiceTarefa} marcada como concluída")
        else:
            print("Índice de tarefa inválido")
    except ValueError:
        print("Por favor, insira um número válido.")

print("Gerenciador de Tarefas")
while True:
    print("\n")
    print("Selecione uma das opções abaixo!")
    print("--------------------------------")
    print("1. Adicionar Tarefa")
    print("2. Deletar Tarefa")
    print("3. Listar Tarefa")
    print("4. Editar Tarefa")
    print("5. Marcar como Concluída")
    print("6. Sair")
    
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        adicionarTarefa()

    elif escolha == "2":
        deletarTarefa()

    elif escolha == "3":
        listarTarefa()

    elif escolha == "4":
        editarTarefa()

    elif escolha == "5":
        marcarComoConcluida()

    elif escolha == "6":
        break

    else:
        print("Opção Inválida")