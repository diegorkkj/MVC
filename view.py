from controller import *
from model import *
from dao import *

sair = True

while sair == True:
    limpar()
    print("Software de gerenciamento de tarefas")
    print("[1] - Adicionar tarefa")
    print("[2] - Excluir tarefa")
    print("[3] - Listar tarefas")
    print("[4] - Listar tarefas concluidas")
    print("[5] - Concluir tarefa")
    print("[6] - Alterar tarefa")
    print("[7] - Sair")
    print("Digite o numero equivalente a opção que deseja")

    opcao = obter_opcao()

    match opcao:
        case 1:
            limpar()
            tarefa = input("Digite a tarefa: ")
            adicionartarefa=ControllerAdicionarTarefa(tarefa)
            adicionar_tarefa(tarefa)
            parar()
            limpar()

        case 2:
            limpar()
            listarTarefa=ControllerListarTarefa()
            excluir = (input("Digite o número da tarefa que deseja excluir: "))
            excluirTarefa=ControllerExcluirTarefa(excluir)
            listarTarefa=ControllerListarTarefa()
            parar()
            limpar()

        case 3:
            limpar()
            print("TAREFAS")
            print("")
            listar_tarefas()
            print("")
            parar()
            limpar()

        case 4:
            limpar()
            print("Ta em obras deve")
            parar()

        case 5:
            limpar()
            print("Ta em obras deve")
            parar()

        case 6:
            limpar()
            print("Ta em obras deve")
            parar()

        case 7:
            limpar()
            print("Saindo...")
            parar()
            sair=False    
    
        case _:
            limpar()
            print("Opção inválida")
            parar()
            limpar()