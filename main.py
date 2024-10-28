from view import display_title, quit, clear_terminal
from stock import stock_menu
from employee import employee_menu
from sales import sales_menu
import os

def main():
  
    action_list = {"1": stock_menu, "2": employee_menu, "3": sales_menu, "4": quit}
    while True:
        
        action = input("""Seja bem vindo ao WoodStock! escolha uma ação:
[1] Módulo de Estoque
[2] Módulo de Funcionários
[3] Módulo de Vendas
[4] Sair
""")
        if action in action_list:
            action_list[action]() #Chama a ação escolhida
        else:
            clear_terminal()
            print("A ação escolhida é inválida!")
            
    
if __name__ == "__main__":
    display_title()
    main()