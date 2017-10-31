from libs.Json_db import Json_db

class Company(object):

    def __init__(self, id):
        self.id = id
        self.company = ''
        self.nif = ''
        self.address = ''
        self.pc = ''
        self.city = ''
        self.email = ''
        self.contact = ''
        self.comments = ''

    def exports(self):
        return self.__dict__

    def imports(self, data):
        self.__dict__ = data


class Companies(object):

    def __init__(self, db_file):
        db_path = './db/'
        self.companies = Json_db(db_path + db_file)

    def add(self, company):
        self.companies.set(company.id, company.exports())
        self.companies.store()

    def list(self):
        l = []
        keys = self.companies.keys()
        for key in keys:
            c = Company(key)
            c.imports(self.companies.get(key))
            l.append(c)
        return l

    def get(self, id):
        c = Company(id)
        c.imports(self.companies.get(id))
        return c

    def exists(self, id):
        return self.companies.exists(id)

