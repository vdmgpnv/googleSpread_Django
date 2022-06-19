import httplib2
import requests
import apiclient
from oauth2client.service_account import ServiceAccountCredentials
import re
from datetime import datetime
from requests.exceptions import HTTPError


class WorkWithData:
    
    """Класс для получения данных из гугл таблиц, а так же курса доллара из цб рф"""
    
    def __init__(self, CREDENTIALS_FILE = 'concrete-fabric-353506-e1786c8afe6f.json',
                 spreadsheetId = '1zRFmvrujT03J-pzbK77WF5HXXj-8-zS1lWjkNvf7yS0',
                 url = ''):
        self.CREDENTIALS_FILE = CREDENTIALS_FILE
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
        self.httpAuth = self.credentials.authorize(httplib2.Http()) 
        self.service = apiclient.discovery.build('sheets', 'v4', http = self.httpAuth) 
        self.spreadsheetId = spreadsheetId
        self.ranges = ["Лист1"]
        self.url = url

    def get_data_from_sheet(self):
        """Метод подключается к таблице и выбирает все данные из нее,
        затем берется срез только значений строк из таблицы и возвращает список состоящий из списков значений"""
        raw_data = self.service.spreadsheets().values().batchGet(spreadsheetId = self.spreadsheetId, 
                                     ranges = self.ranges, 
                                     valueRenderOption = 'FORMATTED_VALUE',
                                     majorDimension = 'ROWS',  
                                     dateTimeRenderOption = 'FORMATTED_STRING').execute()
        result = raw_data['valueRanges'][0]['values'][1::]
        
        return result
    
    
    def get_exchange_rate(self, id='R01235'):
        '''Метод запрашивает курс валюты по ID(по умолчанию доллар) на данный момент'''
        try:
            req = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
        
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')  # Python 3.6
        except Exception as err:
            print(f'Other error occurred: {err}')  # Python 3.6
        
        course_info = re.search(fr'<Valute ID="{id}">.+?</Valute>', req.text)
        course = re.search('\d+,\d+', course_info[0])
        return course[0]
    

        
        


   
