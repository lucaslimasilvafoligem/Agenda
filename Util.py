from datetime import datetime
from datetime import date
from datetime import datetime, timedelta
import calendar
import re

class DataUtil:    
    
    # Lista de nomes dos dias da semana
    nomes_dias_da_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']

    # Obtém o dia da semana (0 = segunda-feira, 1 = terça-feira, ..., 6 = domingo)
    @staticmethod
    def dia_semana(): 
        return datetime.now().weekday()

    @staticmethod
    def dias_no_mes(ano, mes):
        return calendar.monthrange(ano, mes)[1]
    
    @staticmethod
    def dia_no_mes():
        return datetime.today().day

    @staticmethod
    def data_hoje():
        return date.today()
    
    @staticmethod
    def proximo_dia(data):
        return data + timedelta(days=1)
    
    @staticmethod
    def proximo_mes(data):
        return data.day(0) + timedelta(moth=1) 



class Validador:

    @staticmethod
    def validarString(string):
        return string != None and string.replace(" ", "") != ""
    
    @staticmethod
    def validarId(id):
        return id != None and isinstance(id, int) and id > 0
