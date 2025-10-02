import csv
from pathlib import Path
import pandas as pd 

def Users_loader():
    contact_list = []
    list_file_path = Path("data") / "list.xlsx"
    rows_limit = 400

    try:
        # check if list.xlsx exists ( Verifica se o list.xlsx existe )
        if not list_file_path.exists():
            raise FileNotFoundError("Não encontrado o arquivo list.xlsx")
        
        # skip empty line and head ( Pula células em branco e cabeçalho ) 
        df = pd.read_excel(list_file_path, skiprows=1, names=["name", "phone"])
        df = df.dropna(how="all")

        # validate rows limit ( Valida o limite de linhas )
        if len(df) > rows_limit:
            raise ValueError(f"A lista excede o limite de {rows_limit} linhas")
        
        # clean and format name ( Limpa e formata o nome )
        df["name"] = df["name"].astype(str).str.strip()

        # clean and format phone ( Limpa e formata o telefone )
        df["phone"] = df["phone"].astype(str).str.replace(r"[\(\)\-\s]", "", regex=True)

        # convert dataframe to list of dicts ( Converte dataframe em lista de dicionários )
        contact_list = df.to_dict(orient="records")

        return contact_list

    except Exception as e:
        # error loading list ( Erro ao carregar lista )
        print(f"Erro ao carregar lista: {e}")
        return []
