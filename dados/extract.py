from datetime import datetime
from kaggle.api.kaggle_api_extended import KaggleApi

def log(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' 
    now = datetime.now() 
    timestamp = now.strftime(timestamp_format)
    with open("dados\logfile.txt","a") as f:
        f.write(message +  ', ' + timestamp + '\n')

def extract():
    log('Iniciando chamada API')
    api = KaggleApi()
    api.authenticate()
    log('Api autenticada')
    api.dataset_download_file('tawfikelmetwally/employee-dataset', file_name = 'Employee.csv', path= 'dados')
    log('Dados Salvos')

extract()
log('Processo finalizado')

