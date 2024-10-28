import os
import json

def load_data(dbname):
    file  = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{dbname}.json"
    if os.path.exists(file):
        with open(file, 'r') as file:
            return json.load(file)
        
def write_data(dbname, list):
    file = f"{os.path.dirname(__file__)}{os.sep}database{os.sep}{dbname}.json"
    with open(file, "w") as file:
        json.dump(list, file, indent=4, ensure_ascii=False)