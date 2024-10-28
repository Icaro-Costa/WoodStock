from database import load_data, write_data
from view import display_subtitle, clear_terminal

def display_product_list():
    clear_terminal()
    display_subtitle("Tabela de produtos")
    
    products = load_data("products")
    for product in products:
        print(f"Código: {product['id']} | Nome: {product['name']} | Descrição: {product['description']} | Data de entrada: {product['entry_date']} | Data de validade: {product['expiration_date']} | Data de saída: {product['exit_date']}")
        
    input("Digite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()
def create_product():
    clear_terminal()
    display_subtitle("Cadastro de produtos")
    
    products = load_data("products")
    name = input("Digite o nome do produto: ")
    description = input("Forneça a descrição do produto: ")
    entry_date = input("Forneça a data de entrada do produto: ")
    expiration_date = input("Forneça a data de validade do produto: ")
    exit_date = input("Forneça a data de saída do produto: ")
    
    current_id = products[-1]["id"] + 1 if products != [] else 1
    
    products.append({"id": current_id, "name": name, "description": description, "entry_date": entry_date, "expiration_date": expiration_date, "exit_date": exit_date})
    write_data("products", products)
    
    input("Digite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()
def update_product():
    pass
def remove_product():
    clear_terminal()
    display_subtitle("Cadastro de produtos")
    
    id = int(input("Digite o código do produto: "))
    products = load_data("products")
    product_to_remove = products[id - 1]
    products.pop(products.index(product_to_remove))
    write_data("products", products)
    
    input("Digite qualquer tecla para voltar para o módulo de estoque")
    stock_menu()

def stock_menu():
    action_list = {"1": display_product_list, "2": create_product, "3": update_product, "4": remove_product}
    while True:
        display_subtitle("Módulo de Estoque")
        
        action = input("""
[1] Ver lista de produtos
[2] Cadastrar produto
[3] Atualizar cadastro de produto 
[4] Descontinuar produto
[5] Voltar ao menu principal
""")
        if action in action_list:
            action_list[action]()
        elif action == "5":
            clear_terminal()
            break
        else:
            clear_terminal()
            print("A ação escolhida é inválida!")