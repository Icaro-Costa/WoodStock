import os
import json
from typing import List

def load_data(dbname: str) -> List[dict] | list:
    file  = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{dbname}.json"
    if not os.path.exists(file):
        with open(file, 'w') as file:
            json.dump([], file, indent=4)

    with open(file, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo JSON.")
            return []
        
def write_data(dbname: str, list: List[dict]) -> bool:
    file = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{dbname}.json"
    with open(file, "w") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)
        return True

def search_by_id(dict_list: List[dict], id: int) -> dict | IndexError:
    low = 0
    high = len(dict_list) - 1

    while (low <= high):
        mid = int((low + high) / 2)

        if dict_list[mid]["id"] == id:
            return dict_list[mid]
        elif dict_list[mid]["id"] < id:
            low = mid + 1
        else:
            high = mid - 1
    raise IndexError