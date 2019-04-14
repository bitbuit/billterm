from components.company.Company import Company
from libs.Json_db import Json_db

class Me(object):

    def __init__(self, db_file):
        self._me = Json_db(db_file)
        self._company = Company('ME')
        self._company.imports(self._me.get('ME'))

    def get_company(self):
        return self._company

    def get_vat(self, id):
        vats = self._me.get('vats')
        if id in vats:
            return vats[id]
        else:
            return None

    def list_vats(self):
        return self._me.get('vats')

    def get_payments(self, id):
        payments = self._me.get('payments')
        if id in payments:
            return payments[id]
        else:
            return None

    def list_payments(self):
        return self._me.get('payments')
