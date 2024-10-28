import os
import json
from datetime import datetime
from view import clear_terminal, display_title
from database import load_data,write_data

def add_employee():
    employees = load_data("funcionarios")
    cpf = input("Digite o CPF do funcionário (apenas números): ")

    if any(employee['cpf'] == cpf for employee in employees):
        print("CPF já cadastrado! Tente novamente.")
        return

    name = input("Digite o nome do funcionário: ")
    position = input("Digite o cargo do funcionário: ")
    hire_date = datetime.now().strftime("%d/%m/%Y")

    try:
        salary = float(input("Digite o salário do funcionário: "))
    except ValueError:
        print("Salário inválido! Insira um número.")
        return

    new_employee = {
        'cpf': cpf,
        'nome': name,
        'cargo': position,
        'data_contratacao': hire_date,
        'salario': salary
    }
    employees.append(new_employee)
    write_data("funcionarios", employees)
    print("Funcionário adicionado com sucesso.")

def list_employees():
    employees = load_data("funcionarios")
    if employees:
        clear_terminal()
        print("\nLista de Funcionários:")
        print("-" * 50)
        for employee in employees:
            print(f"CPF: {employee['cpf']}")
            print(f"Nome: {employee['nome']}")
            print(f"Cargo: {employee['cargo']}")
            print(f"Data de Contratação: {employee['data_contratacao']}")
            print(f"Salário: R${employee['salario']:,.2f}")
            print("-" * 50)
    else:
        print("Nenhum funcionário cadastrado.")

def update_employee():
    cpf = input("Digite o CPF do funcionário que deseja atualizar: ")
    employees = load_data("funcionarios")
    for employee in employees:
        if employee['cpf'] == cpf:
            new_name = input("Novo nome (ou Enter para manter o atual): ")
            new_position = input("Novo cargo (ou Enter para manter o atual): ")
            new_hire_date = input("Nova data de contratação (DD/MM/AAAA) (ou Enter para manter): ")
            new_salary = input("Novo salário (ou Enter para manter o atual): ")

            if new_name:
                employee['nome'] = new_name
            if new_position:
                employee['cargo'] = new_position
            if new_hire_date:
                try:
                    datetime.strptime(new_hire_date, "%d/%m/%Y")
                    employee['data_contratacao'] = new_hire_date
                except ValueError:
                    print("Data de contratação inválida! Formato esperado: DD/MM/AAAA.")
                    return
            if new_salary:
                try:
                    employee['salario'] = float(new_salary)
                except ValueError:
                    print("Salário inválido! Deve ser um número.")
                    return
            
            write_data("funcionarios", employees)
            print("Funcionário atualizado com sucesso.")
            return
    print("Funcionário não encontrado.")

def delete_employee():
    cpf = input("Digite o CPF do funcionário que deseja excluir: ")
    employees = load_data("funcionarios")
    employees = [emp for emp in employees if emp['cpf'] != cpf]
    write_data("funcionarios", employees)
    print("Funcionário excluído com sucesso.")

def search_employee():
    cpf = input("Digite o CPF do funcionário que deseja buscar: ")
    employees = load_data("funcionarios")
    for employee in employees:
        if employee['cpf'] == cpf:
            clear_terminal()
            print(f"CPF: {employee['cpf']}")
            print(f"Nome: {employee['nome']}")
            print(f"Cargo: {employee['cargo']}")
            print(f"Data de Contratação: {employee['data_contratacao']}")
            print(f"Salário: R${employee['salario']:,.2f}")
            return
    print("Funcionário não encontrado.")

def employee_menu():
    action_list = {
        "1": add_employee,
        "2": list_employees,
        "3": update_employee,
        "4": delete_employee,
        "5": search_employee
    }
    
    while True:
        display_title()
        print("\n==== MENU DE FUNCIONÁRIOS ====")
        print("1. Adicionar Funcionário")
        print("2. Listar Funcionários")
        print("3. Atualizar Funcionário")
        print("4. Excluir Funcionário")
        print("5. Buscar Funcionário")
        print("6. Sair")
        
        option = input("Escolha uma opção: ")

        if option in action_list:
            clear_terminal()
            action_list[option]()  
        elif option == '6':
            print("Saindo do Módulo...")
            break
        else:
            clear_terminal()
            print("Opção inválida! Tente novamente.")

def menu():
    clear_terminal()
    employee_menu()
