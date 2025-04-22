import time
import os

tarefas = {
   1: {"titulo": "Comprar leite", "descricao": "Comprar 2 litros de leite", "status": "pendente"},
    2: {"titulo": "Estudar Python", "descricao": "Estudar funções em Python", "status": "concluída"}
}

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def imprimir_separador():
    print("=" * 50)
   
def adicionar_tarefa(tarefas):
    limpar_tela()
    imprimir_separador()
    print("[ADICIONAR TAREFA]")
    imprimir_separador()
    titulo = input('[TITULO]: ')
    descricao = input('[DESCRIÇÃO]: ')
    imprimir_separador()
    
    id_tarefa = len(tarefas) + 1
    tarefas[id_tarefa] = {"titulo": titulo, "descricao": descricao, "status": "pendente"}
    limpar_tela()
    imprimir_separador()
    print("[ADICIONANDO TAREFA...]")
    imprimir_separador()
    time.sleep(2)
    limpar_tela()
    imprimir_separador()
    print(f"TAREFA ['{titulo}'] ADICIONADA COM SUCESSO!")
    imprimir_separador()
 

def listar_tarefas(tarefas):
    imprimir_separador()

    for i in tarefas:
        print(f"TAREFA [ID {i}]")
        print(f" TITULO:      {tarefas[i]['titulo']}")
        print(f" DESCRIÇÃO:   {tarefas[i]['descricao']}")
        print(f" STATUS:      {tarefas[i]['status']}")
        imprimir_separador()
 
def listar_tarefas_por_status(tarefas):
    pendentes = {}
    concluidos = {}

    imprimir_separador()
    print("[EXIBIR TAREFAS]\n[1]PENDENTES [2]CONCLUÍDAS [3]SAIR")
    imprimir_separador()
    opcao = int(input('DIGITE A OPÇÃO:'))

    while opcao not in [1,2,3]:
        imprimir_separador()
        print('[FAVOR INSIRA A OPÇÃO CORRETA]')
        
        print("[EXIBIR TAREFAS]\n[1]PENDENTES [2]CONCLUÍDAS [3]SAIR")
        imprimir_separador()
        opcao = int(input('DIGITE A OPÇÃO:'))

    for id_tarefa, info in tarefas.items():
        if info['status'] == 'pendente':
            pendentes[id_tarefa] = {"titulo": tarefas[id_tarefa]['titulo'], "descricao": tarefas[id_tarefa]['descricao'], "status":tarefas[id_tarefa]['status']}
        elif info['status'] == 'concluída':
            concluidos[id_tarefa] = {"titulo": tarefas[id_tarefa]['titulo'], "descricao": tarefas[id_tarefa]['descricao'], "status":tarefas[id_tarefa]['status']}
    limpar_tela()
    imprimir_separador()
    
    if opcao == 1:
        print('[PENDENTES]')
        listar_tarefas(pendentes)
    elif opcao == 2:
        print('[CONCLUÍDOS]')
        listar_tarefas(concluidos) 
    elif opcao == 3:
        menu()
        
    try:
        print("[1]VOLTAR")
        imprimir_separador()
        opcao_rodape = int(input("DIGITE A OPÇÃO:"))
        
        if opcao_rodape == 1:
            limpar_tela()
            listar_tarefas_por_status(tarefas)  
        else:
            print("[OPÇÃO INVÁLIDA]")
            time.sleep(2)
            limpar_tela()    
            listar_tarefas_por_status(tarefas)
                  
        opcao_rodape = 0
    except ValueError:
        print("[OPÇÃO INVÁLIDA]")
        
def alterar_status(tarefas):
    while True:
        try:
            imprimir_separador()
            print('[ALTERAÇÃO DE STATUS]')
            imprimir_separador()
            print("[1]ID DA TAREFA [2]LISTAR TODAS AS TAREFAS [3]SAIR")
            imprimir_separador()
            opcao_rodape = int(input("DIGITE A OPÇÃO:"))

            if opcao_rodape in [1, 2,3]:
                if opcao_rodape == 1:
                    try:
                        imprimir_separador()
                        id_selecionado = int(input('DIGITE O ID DA TAREFA: '))

                        if id_selecionado in tarefas:
                            listar_tarefas({id_selecionado: tarefas[id_selecionado]})
                            time.sleep(3)
                            limpar_tela()
                            imprimir_separador()
                            print('[ALTERANDO STATUS...]')
                            imprimir_separador()
                            time.sleep(2)
    
                            if tarefas[id_selecionado]['status'] == 'pendente':
                                tarefas[id_selecionado]['status'] = 'concluída'
                            else:
                                tarefas[id_selecionado]['status'] = 'pendente'
                            
                            limpar_tela()
                            imprimir_separador()
                            print(f"[STATUS ATUALIZADO!]")
                            imprimir_separador()
                            listar_tarefas({id_selecionado: tarefas[id_selecionado]})
                            time.sleep(3)
                            limpar_tela()
                        else:
                            limpar_tela()
                            print("[ID NÃO ENCONTRADO]")
                            
                    except ValueError:
                        print("[ERRO] Digite um número válido para o ID.")         
                elif opcao_rodape == 2:
                    limpar_tela()
                    imprimir_separador()
                    print('[TAREFAS]')
                    listar_tarefas(tarefas)
                    try:
                        print("[1]VOLTAR")
                        imprimir_separador()
                        opcao_rodape = int(input("DIGITE A OPÇÃO:"))
        
                        if opcao_rodape == 1:
                            limpar_tela()
                            alterar_status(tarefas)
                        else:
                            print("[OPÇÃO INVÁLIDA]")
                            time.sleep(2)
                            limpar_tela()
                            alterar_status(tarefas)
                       
                        opcao_rodape = 0
                    except ValueError:
                        print("[OPÇÃO INVÁLIDA]")
                    
                elif opcao_rodape == 3:
                    limpar_tela()
                    menu()
            else:
                print("[OPÇÃO INVÁLIDA 1 ou 2]")
                
        except ValueError:
            print("Erro: Digite um número válido.")

def excluir_tarefa(tarefas):
    while True:
        try:
            imprimir_separador()
            print('[EXCLUIR TAREFA PELO ID]')
            imprimir_separador()
            print("[1]DIGITAR ID DA TAREFA [2]LISTAR TODAS AS TAREFAS\n[3]SAIR")
            imprimir_separador()
            opcao = int(input("DIGITE A OPÇÃO:"))

            if opcao in [1, 2, 3]:
                if opcao == 1:
                    try:
                        imprimir_separador()
                        id_selecionado = int(input('DIGITE O ID:'))
                        if id_selecionado in tarefas:
                            listar_tarefas({id_selecionado: tarefas[id_selecionado]})
                            time.sleep(2)
                            limpar_tela()
                            imprimir_separador()
                            print('[EXCLUINDO TAREFA...]')
                            imprimir_separador()
                            
                            time.sleep(2)
                            
                            tarefas.pop(id_selecionado)
                            print("TAREFA EXCLUÍDA COM SUCESSO!")
                        else:
                            limpar_tela()
                            print("[ID NÃO ENCONTRADO]")
                    except ValueError:
                        print("[ERRO] Digite um número válido para o ID.")   
                elif opcao == 2:
                    limpar_tela()
                    imprimir_separador()
                    print('[TAREFAS]')
                    listar_tarefas(tarefas)  
                    try:
                        print("[1]VOLTAR")
                        imprimir_separador()
                        opcao_rodape = int(input("DIGITE A OPÇÃO:"))
                                
                        if opcao_rodape == 1:
                            limpar_tela()
                            excluir_tarefa(tarefas)
                        else:
                            print("[OPÇÃO INVÁLIDA]")
                            time.sleep(2)
                            limpar_tela()
                            excluir_tarefa()
                        
                        opcao_rodape = 0
                                
                    except ValueError:
                        print("[OPÇÃO INVÁLIDA]")
                elif opcao == 3:
                    limpar_tela()
                    menu()
                     
                opcao == 0                 
            
            else:
                print("[OPÇÃO INVÁLIDA]")
                limpar_tela()
                time.sleep(3)
                excluir_tarefa()
                
                
        except ValueError:
            print("Erro: Digite um número válido.")
            

def menu():
    while True:
        imprimir_separador()
        print("[MENU]")
        imprimir_separador()
        print("[1]ADICIONAR TAREFA\n[2]LISTAR TODAS AS TAREFAS\n[3]LISTAR TAREFAS POR STATUS\n[4]ALTERAR STATUS\n[5]EXCLUIR TAREFA\n[6]SAIR")
        imprimir_separador()
        opcao = int(input(f"DIGITE A OPÇÃO:"))
        limpar_tela()
        
        #adicionar tarefa
        if opcao == 1:
            adicionar_tarefa(tarefas)
            time.sleep(3)
            limpar_tela()
            
        #listar todas as tarefas
        elif opcao == 2:
            imprimir_separador()
            print('[TAREFAS]')
            listar_tarefas(tarefas)
            try:
                print("[1]SAIR")
                imprimir_separador()
                opcao_rodape = int(input("DIGITE A OPÇÃO:"))
                
                if opcao_rodape == 1:
                    limpar_tela()
                    menu()
                else:
                    print("[OPÇÃO INVÁLIDA]")
                    time.sleep(2)
                    limpar_tela()
                    menu()
                opcao_rodape = 0
                
            except ValueError:
                print("[OPÇÃO INVÁLIDA]")
                
            opcao = 0
            
        #listar tarefas por status
        elif opcao == 3:
            listar_tarefas_por_status(tarefas)
            time.sleep(3)
            limpar_tela()
            
        #alterar status
        elif opcao == 4:
            alterar_status(tarefas)
            time.sleep(3)
            limpar_tela()
            
        #excluir tarefa
        elif opcao == 5:
            time.sleep(2)
            excluir_tarefa(tarefas)
            
        elif opcao == 6:
            break
        

#main
if __name__ == '__main__':
    menu()