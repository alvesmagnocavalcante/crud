import requests
import os


def enviar_msg_whatsapp(tarefa):
    numero = os.getenv('NUMERO')
    key = os.getenv('KEY')
    msg = f'''Nova tarefa cadastrada: \n
    \nTítulo: {tarefa.titulo}
    \nDescrição: {tarefa.descricao}
    \nConcluída: {tarefa.concluida}
    \nData de Criação: {tarefa.data_criacao}
    '''
    url = f'https://api.callmebot.com/whatsapp.php?phone={numero}&text={msg}&apikey={key}'
    response = requests.get(url)
    return response