from database import load_data, write_data, search_by_id
from view import display_subtitle, clear_terminal
from time import sleep
from datetime import datetime

def validate_date_format(prompt):
    while True:
        input_value = input(prompt)
        try:
            datetime.strptime(input_value, "%d/%m/%Y")
            break
        except ValueError:
            print("Data inválida. Por favor, tente novamente no formato DD/MM/YYYY.")
    return input_value

def display_product_list():
    clear_terminal()
    display_subtitle("Tabela de produtos")
    
    products = load_data("products")
    
    if products:
        print(f"\n{'Código'.ljust(10)} | {'Nome'.ljust(10)} | {'Descrição'.ljust(10)} | {'Data de entrada'.ljust(10)} | {'Data de validade'.ljust(10)}")
    
        for product in products:
            print(f"{str(product['id']).ljust(10)} | {product['name']} | {product['description']} | {product['entry_date']} | {product['expiration_date']}")
        
        input("\nDigite qualquer tecla para voltar para o módulo de estoque")
        stock_menu()
    else:
        print("Nenhum produto registrado.")
        sleep(2)
        stock_menu()
        return None

def search_product():
    clear_terminal()
    display_subtitle("Informações do produto")
    id = int(input("\nDigite o código do produto que deseja buscar: "))

    products = load_data("products")
    try:
        product = search_by_id(products, id)
    except IndexError:
        print("\nNão conseguimos encontrar nenhum produto com este código...")
        sleep(2)
        stock_menu()
        return None     

    print(f"\nCódigo: {product['id']} | Nome: {product['name']} | Descrição: {product['description']} | Data de entrada: {product['entry_date']} | Data de validade: {product['expiration_date']}")

    input("\nDigite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()

def create_product():
    clear_terminal()
    display_subtitle("Cadastro de produtos")
    
    products = load_data("products")

    name = input("\nDigite o nome do produto: ")
    description = input("Forneça a descrição do produto: ")
    entry_date = validate_date_format("Forneça a data de entrada do produto: (DD/MM/AAAA)")
    expiration_date = validate_date_format("Forneça a data de validade do produto: (DD/MM/AAAA)")
    
    current_id = products[-1]["id"] + 1 if products != [] else 1
    
    products.append({"id": current_id, "name": name, "description": description, "entry_date": entry_date, "expiration_date": expiration_date})
    write_data("products", products)
    
    print("\n✅ Produto criado com sucesso!")
    input("Digite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()

def update_product():
    clear_terminal()
    display_subtitle("Atualizar Produto")

    id = int(input("\nDigite o código do produto que deseja atualizar: "))

    products = load_data("products")
    try:
        product = search_by_id(products, id)
    except IndexError:
        print("\nNão conseguimos encontrar nenhum produto com este código...")
        sleep(2)
        stock_menu()
        return None

    name = input("Digite o nome do produto (Enter caso não queira atualizar): ") or product["name"]
    description = input("Forneça a descrição do produto (Enter caso não queira atualizar): ") or product["description"]
    entry_date = input("Forneça a data de entrada do produto (Enter caso não queira atualizar): (DD/MM/AAAA)") or product["entry_date"]
    expiration_date = input("Forneça a data de validade do produto (Enter caso não queira atualizar): (DD/MM/AAAA)") or product["expiration_date"]
    
    inputs = {
        "name": name, 
        "description": description, 
        "entry_date": entry_date, 
        "expiration_date": expiration_date,
    }
    
    for input_key, input_value in inputs.items():
        product[input_key] = input_value
    
    index_of_product = products.index(product)
    products[index_of_product] = product
    
    write_data("products", products)

    print("\n✅ Produto atualizado com sucesso!")
    input("Pressione qualquer tecla para voltar ao módulo de estoque")
    stock_menu()          

def remove_product():
    clear_terminal()
    display_subtitle("Cadastro de produtos")
    
    id = int(input("\nDigite o código do produto: "))
    products = load_data("products")
    
    try:
        product = search_by_id(products, id)
    except IndexError:
        print("\nNão conseguimos encontrar nenhum produto com este código...")
        sleep(2)
        stock_menu()
        return None
    
    products.remove(product)
    write_data("products", products)
    
    print("\n✅ Produto removido com sucesso!")
    input("Digite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()

def stock_menu():
    action_list = {
        "1": display_product_list, 
        "2": search_product, 
        "3": create_product, 
        "4": update_product, 
        "5": remove_product
        }
    while True:
        display_subtitle("Módulo de Estoque")
        
        action = input("""
[1] Ver lista de produtos
[2] Procurar produto
[3] Cadastrar produto 
[4] Atualizar cadastro de produto
[5] Descontinuar produto
[6] Voltar ao menu principal
""")
        if action in action_list:
            action_list[action]()
            break
        elif action == "6":
            clear_terminal()
            break
        else:
            clear_terminal()
            print("A ação escolhida é inválida!")
