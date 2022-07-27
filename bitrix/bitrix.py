from pprint import pprint
import requests

def get_deal_details(self):
    url = 'https://mirni.bitrix24.ru/rest/23/rpgxs100qycfzutf/'
    method = 'crm.deal.get'
    params = {'id': 31}
    url = f'{url}/{method}'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return response.json()['error_description']

def get_user_deals(self):
    url = 'https://mirni.bitrix24.ru/rest/23/rpgxs100qycfzutf'
    method = 'crm.deal.list'
    params = {
        'order[]': {'ID': 'ASC'},
        'filter[STAGE_ID]': ['C5:WON'],
        'filter[STAGE_ID]': ['C5:UC_LRLFKL'], #Закрытие документов 
        'filter[UF_CRM_1588922563]': [0], # Комиссионные выплачены?
        'filter[ASSIGNED_BY_ID]': self.user.bitrix_user_id,
        'select[]': ['ID', 'TITLE', 'ASSIGNED_BY_ID', 'STAGE_ID', 'OPPORTUNITY']
    }
    url = f'{url}/{method}'
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['result']
    else:
        return response.json()['error_description']