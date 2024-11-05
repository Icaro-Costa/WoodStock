import re
from time import sleep
from view import clear_terminal, display_subtitle
from database import load_data, write_data

def format_cpf(cpf):
   #remove caracter especial
    return re.sub(r'\D', '', cpf)

def create_worker(name, age, cpf, job):
    workers = load_data("users")
    cpf = format_cpf(cpf)  # Formata o CPF digitado

    # Verifica se o CPF já existe 
    if any(format_cpf(worker['cpf']) == cpf for worker in workers):
        print("CPF já cadastrado! Tente novamente.")
        return None
    
    # Adiciona o trabalhador ao JSON com CPF no formato padrão
    workers.append({"name": name, "age": age, "cpf": cpf, "job": job})
    write_data("users", workers)

    print("✅ Registro concluído com sucesso!")
    input("\nDigite qualquer tecla para voltar ao módulo de funcionários")
    worker_menu()

def list_workers():
    workers = load_data("users")
    #lista trabalhador
    if workers:
        max_len = max(len(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}") for worker in workers)
        display_subtitle("Lista de funcionários")
        for worker in workers:
            print("*" * max_len)
            print(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}")
            print("*" * max_len)
        print("=" * max_len)
    else:
        print("Nenhum usuário registrado.")
        sleep(2)
        worker_menu()
        return None

def update_worker(old_name, new_name, new_age, new_cpf, new_job):
    workers = load_data("users")
    #atualiza trabalhador
    updated = False
    for worker in workers:
        if worker['name'] == old_name:
            worker['name'] = new_name
            worker['age'] = new_age
            worker['cpf'] = format_cpf(new_cpf)  # Formata o CPF atualizado
            worker['job'] = new_job
            updated = True
            break
    if updated:
        write_data("users", workers)
        print("✅ Usuário atualizado com sucesso!")
        input("\nDigite qualquer tecla para voltar para o módulo de usuários")
        worker_menu()
    else:
        print("Usuário não encontrado.")
        sleep(2)
        worker_menu()
        return None

def remove_worker(name):
    workers = load_data("users")
    #remove trabalhador
    new_workers = [worker for worker in workers if worker['name'] != name]
    if len(new_workers) != len(workers):
        write_data("users", new_workers)
        print("✅ Usuário removido com sucesso!")
        input("\nDigite qualquer tecla para voltar ao módulo de estoque")
        worker_menu()
    else:
        print("Usuário não encontrado.")
        sleep(2)
        worker_menu()
        return None

def search_worker(name):
    workers = load_data("users")
    #busca trabalhador
    found = False
    for worker in workers:
        if worker['name'] == name:
            print(f"NOME: {worker['name']}, IDADE: {worker['age']}, CPF: {worker['cpf']}, CARGO: {worker['job']}")
            found = True
            input("\nDigite qualquer tecla para voltar ao módulo de usuários")
            worker_menu()
            break
    
    if not found:
        print("Usuário não encontrado.")
        sleep(2)
        worker_menu()
        return None

def worker_menu():
    clear_terminal()
    while True:
        display_subtitle("Módulo de Funcionários")
        
        action = input("""
[1] Cadastrar Funcionário 
[2] Listar funcionários
[3] Atualizar cadastro de funcionário
[4] Desligar funcionário
[5] Procurar funcionário
[6] Voltar ao menu principal
""")

        if action == '1':
            clear_terminal()
            name = input("Nome: ")
            age = input("Idade: ")
            cpf = input("CPF (formato 000.000.000-00): ")
            job = input("Cargo: ")
            create_worker(name, age, cpf, job)
            break
        elif action == '2':
            clear_terminal()
            list_workers()
            break
        elif action == '3':
            clear_terminal()
            old_name = input("Nome do usuário para atualizar: ")
            new_name = input("Novo nome: ")
            new_age = input("Nova idade: ")
            new_cpf = input("Novo CPF (formato 000.000.000-00): ")
            new_job = input("Novo cargo: ")
            update_worker(old_name, new_name, new_age, new_cpf, new_job)
            break
        elif action == '4':
            clear_terminal()
            name = input("Nome do usuário para excluir: ")
            remove_worker(name)
            break
        elif action == '5':
            clear_terminal()
            name = input("Nome do usuário para buscar: ")
            search_worker(name)
            break
        elif action == '6':
            clear_terminal()
            break
        else:
            print("Opção inválida! Tente novamente.")
