from datetime import date

from components.company.Company import Company
from libs.Json_db import Json_db

from pprint import pprint

class Invoice(object):

    def __init__(self, id):
        self.id = id
        self.company = None
        self.date = ''
        self.summary = ''
        self.items = []
        self.vats = []
        self.subtotal = 0
        self.total = 0
        self.paid = None

    def __subtotal(self):
        subtotal = 0
        for i in range(len(self.items)):
            line = self.items[i]
            subtotal = subtotal + line['total']
        return subtotal

    def __total_vats(self):
        vats = {}
        for i in range(len(self.items)):
            line = self.items[i]
            pprint(line['vats'])
            for v in line['vats']:
                key = v
                value = line['vats'][v]
                vats[key] = value if not key in vats else vats[key] + value
        return vats

    def __total(self):
        total = self.subtotal
        vats = self.vats

        pprint(vats)

        for code in self.vats:
            total = total + vats[code]
        return total

    def _recalculate(self):
        self.subtotal = self.__subtotal()
        self.vats = self.__total_vats()
        self.total = self.__total()

    def set_customer(self, company):
        self.company = {
            "address": company.address,
            "nif": company.nif,
            "city": company.city,
            "id": company.id,
            "company": company.company,
            "pc": company.pc
        }

    def add_item(self, description, price, qty, vats):
        total = price * qty
        v = {}
        for vat in vats:
            e = vats[vat]
            v[e['id']] = total * (float(e['value'])/100)

        self.items.append( { 
            'description': description, 
            'price': price,
            'qty': qty,
            'total': total,
            'vats': v
             } )

        self._recalculate()

    def subtotal(self):
        return self.subtotal

    def resume_vats(self):
        return self.vats

    def total(self):
        return self.total

    def get_item(self, n):
        if n > len(self.items) - 1:
            return None
        return self.items[n]

    def get_date(self):
        d = self.date.split("-")
        return date(int(d[0]),int(d[1]),int(d[2]))

    def exports(self):
        return self.__dict__

    def imports(self, data):
        self.__dict__ = data 


class Invoices(object):

    def __init__(self, db_file):
        path_db = './db/'
        self.invoices = Json_db(path_db + db_file)

    def add(self, invoice):
        self.invoices.set(invoice.id, invoice.exports())
        self.invoices.store()

    def list(self, sort='desc', start_date=None, end_date=None):
        l = []
        keys = self.invoices.keys(sort=sort)
        sd = start_date if start_date else date(1970,1,1)
        ed = end_date if end_date else date.today()
        for key in keys:
            i = Invoice(key)
            i.imports(self.invoices.get(key))
            if i.get_date() >= sd and i.get_date() <= ed:
                l.append(i)
        return l

    def get(self, id):
        inv = Invoice(id)
        inv.imports(self.invoices.get(id))
        return inv

    def exists(self, id):
        return self.invoices.exists(id)

#    def list_resume(self):
#        res = []
#        for id in self.invoices.list():
#            t = self.invoices.get(id)
#            res.append( { 
#                'id': t['id'], 
#                'company_id' : t['company_id'],
#                'summary' : t['summary'],
#                'paid': t['paid'],
#                'date': t['date'],
#                'total': t['total'] } )
#
#        return res



