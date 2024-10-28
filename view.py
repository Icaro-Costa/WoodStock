import time
import os

def display_title():
    print("""
░██╗░░░░░░░██╗░█████╗░░█████╗░██████╗░░██████╗████████╗░█████╗░░█████╗░██╗░░██╗
░██║░░██╗░░██║██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░██╔╝
░╚██╗████╗██╔╝██║░░██║██║░░██║██║░░██║╚█████╗░░░░██║░░░██║░░██║██║░░╚═╝█████═╝░
░░████╔═████║░██║░░██║██║░░██║██║░░██║░╚═══██╗░░░██║░░░██║░░██║██║░░██╗██╔═██╗░
░░╚██╔╝░╚██╔╝░╚█████╔╝╚█████╔╝██████╔╝██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝██║░╚██╗
░░░╚═╝░░░╚═╝░░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚═╝░░╚═╝""")

def display_subtitle(msg):
    os.system("cls") if os.name == "nt" else os.system("clear")
    lines = "_" * len(msg)
    print(lines)
    print(f"\n{msg}")
    print(lines)
    
def clear_terminal():
    os.system("cls") if os.name == "nt" else os.system("clear")

def quit():
    print("Encerrando o programa...")
    time.sleep(2)
    print("Ciao!!")
    exit(0)