from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi


def log(message):
    timestamp_format = "%Y-%h-%d-%H:%M:%S"
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("dados\logfile.txt", "a") as f:
        f.write(message + ", " + timestamp + "\n")


def extract(page, dataset):
    log(f"Iniciando chamada API para o dataset {dataset}")
    api = KaggleApi()
    api.authenticate()
    log(f"Api autenticada para o dataset {dataset}")
    try:
        api.dataset_download_file(page, file_name=dataset, path="dados")
        log(f"Dados Salvos para o dataset {dataset}")
    except:
        log("Falha ao obter dataset")
    log(f"Processo finalizado para o dataset {dataset}")


extract(
    "pavansubhasht/ibm-hr-analytics-at",
    "WA_Fn-UseC_-HR-Employee-Attrition.csv",
)
