from time import sleep
from datetime import datetime
from database import load_data, write_data, search_by_id
from view import display_subtitle, clear_terminal

def validate_date_format(date_str):
    """Verifica se a data está no formato DD/MM/AAAA."""
    try:
        datetime.strptime(date_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def display_sales_list():
    """Exibe a lista de vendas com detalhes formatados."""
    clear_terminal()
    display_subtitle("Tabela de vendas")
    
    sales_data = load_data("sales")  # Carrega os dados de vendas
    if sales_data:
        for sale in sales_data:
            print(f"\nCódigo: {sale['id']} | Nome: {sale['name']} | Valor da venda: {sale['sale_value']} | Data da venda: {sale['sale_date']}")
    else:
        print("Nenhuma venda registrada.")
        sleep(2)
        sales_menu()
        return None
        
    input("\nDigite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()  # Chama o menu de vendas

def create_product():
    """Cria um novo registro de venda."""
    clear_terminal()
    display_subtitle("Cadastro de vendas")
    
    sales_data = load_data("sales")
    name = input("Digite o nome da venda: ")
    sale_value = input("Digite o valor da venda: ")
    
    while True:
        sale_date = input("Forneça a data da venda (DD/MM/AAAA): ")
        if validate_date_format(sale_date):
            break
        print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
    
    current_id = sales_data[-1]["id"] + 1 if sales_data else 1
    
    sales_data.append({"id": current_id, "name": name, "sale_value": sale_value, "sale_date": sale_date})
    write_data("sales", sales_data)
    
    print("✅ Venda registrada com sucesso!")
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def update_sale():
    """Atualiza um registro de venda existente."""
    clear_terminal()
    display_subtitle("Atualização de vendas")
    
    sales_data = load_data("sales")
    id = int(input("Digite o código da venda que deseja atualizar: "))
    
    for sale in sales_data:
        if sale['id'] == id:
            sale['name'] = input(f"Digite o novo nome da venda (atual: {sale['name']}): ") or sale['name']
            sale['sale_value'] = input(f"Digite o novo valor da venda (atual: {sale['sale_value']}): ") or sale['sale_value']
            
            while True:
                sale_date = input(f"Digite a nova data de venda (atual: {sale['sale_date']}) [DD/MM/AAAA]: ") or sale['sale_date']
                if validate_date_format(sale_date):
                    sale['sale_date'] = sale_date
                    break
                print("Data inválida! Por favor, insira no formato DD/MM/AAAA.")
            break
    else:
        print("Venda não encontrada!")
        sleep(2)
        sales_menu()
        return None
    
    write_data("sales", sales_data)
    print("✅ Venda atualizada com sucesso!")
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def remove_sale():
    """Remove um registro de venda."""
    clear_terminal()
    display_subtitle("Exclusão de vendas")
    
    id = int(input("Digite o código da venda que deseja excluir: "))
    sales_data = load_data("sales")
    
    sales_data = [sale for sale in sales_data if sale['id'] != id]
    write_data("sales", sales_data)
    
    print("✅ Venda removida com sucesso!")
    input("Digite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()

def search_sale():
    clear_terminal()
    display_subtitle("Informações da venda")
    
    id = int(input("\nDigite o código da venda que deseja buscar: "))
    
    sales = load_data("sales")
    try:
        sale = search_by_id(sales, id)
    except IndexError:
        print("\nNão conseguimos encontrar nenhuma venda com este código...")
        sleep(2)
        sales_menu()
        return None
    
    print(f"\nCódigo: {sale['id']} | Nome: {sale['name']} | Valor da venda: {sale['sale_value']} | Data da venda: {sale['sale_date']}")
    
    input("\nDigite qualquer tecla para voltar para o módulo de vendas")
    sales_menu()
        
def sales_menu():
    """Exibe o menu de opções do módulo de vendas."""
    action_list = {
        "1": display_sales_list,
        "2": create_product,
        "3": update_sale,
        "4": remove_sale,
        "5": search_sale
    }
    
    while True:
        clear_terminal()
        display_subtitle("Módulo de vendas")
        
        action = input("""
[1] Ver lista de vendas
[2] Cadastrar venda
[3] Atualizar cadastro de venda
[4] Excluir venda
[5] Procurar venda
[6] Voltar ao menu principal
Escolha uma opção: """)
        
        if action in action_list:
            action_list[action]()
            break
        elif action == "6":
            clear_terminal()
            break
        else:
            clear_terminal()
            print("A ação escolhida é inválida!")
