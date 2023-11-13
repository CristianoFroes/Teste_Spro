# Importações

import pandas as pd
from pymongo import MongoClient

# Dados

carros = {"Carro": ["Onix", "Polo", "Sandero", "Fiesta", "City"],
        "Cor": ["Prata", "Branco", "Prata", "Vermelho", "Preto"],
        "Montadora": ["Chevrolet", "Volkswagen", "Renault", "Ford", "Honda"]}

montadoras = {"Montadora": ["Chevrolet", "Volkswagen", "Renault", "Ford", "Honda"],
             "País": ["EUA", "Alemanhã", "França", "EUA", "Japão"]}

# Criando pandas dataframes

carros = pd.DataFrame(carros)
montadoras = pd.DataFrame(montadoras)

# Criando conexão python com Mongodb

client = MongoClient("localhost", 27017)

print(client.list_database_names())


# Criando base de dados

db = client.banco_de_dados


# populando as collections

db.Carros.insert_many(carros.to_dict("records"))

db.Montadoras.insert_many(montadoras.to_dict("records"))