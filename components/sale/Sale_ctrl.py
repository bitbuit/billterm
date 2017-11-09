from pprint import pprint
from datetime import date
import shlex
import csv

from components.sale.Sale import *
from components.sale.Sale_tpl import Sale_tpl

from libs.Screen import *
from app.Model import Model

class Sale_ctrl(object):

    @staticmethod
    def list(params):
        sort = 'desc'
        sd = None
        ed = None
        for i in range(len(params)):
            token = params[i]
            if token == 'between':
                if i+1 in range(len(params)) and not params[i+1] == 'past':
                    print('p1')
                    sd = params[i+1].split("-")
                    sd = date(int(sd[0]),int(sd[1]),int(sd[2]))

                if i+2 in range(len(params)) and not params[i+2] == 'now':
                    print('p2')
                    ed = params[i+2].split("-")
                    ed = date(int(ed[0]),int(ed[1]),int(ed[2]))
                    
            elif token == 'asc' or token == 'desc':
                sort = token

        sales = Model.sales.list(sort=sort, start_date=sd, end_date=ed)
        Sale_tpl.list(sales)


    @staticmethod
    def view(params):
        sales = Model.sales
        if not sales.exists(params[0]):
            print("Not found")
            return
        invoice = sales.get(params[0])

        Sale_tpl.view(invoice)
          

    @staticmethod
    def new(params):
        if len(params) == 0:
            print("Please especify a customer ID")
            return
        customer_id = params[0]
        if not Model.customers.exists(customer_id):
            print("Customer not exists!")
            return
        print("New sale to " + customer_id + ":")
        id = input("Invoice number: ")
        inv = Sale(id)
        inv.set_customer(Model.customers.get(customer_id))
        inv.date = str(date.today())
        t = input("Invoice date ("+ inv.date + "): ")
        inv.date = inv.date if t == '' else t
        inv.summary = input("Summary: ")
        Model.sales.add(inv)        
        
    @staticmethod
    def add_item(params):
        if len(params) == 0:
            print("Please especify a sale invoice ID")
            return

        invoice_id = params[0]
        if not Model.sales.exists(invoice_id):
            print("Sale invoice not exists!")
            return
        
        desc = input("Descripion: ")
        price = float(input("Unit price: "))
        qty = float(input("Quantity: "))
        vatsid = input("Vats separated by comma: ")
        vats = {}

        for vat in vatsid.split(','):
            v = Model.me.get_vat(vat)
            vats[vat] = v

        inv = Model.sales.get(invoice_id)
        inv.add_item(desc, price, qty, vats)
        Model.sales.add(inv)
            

    @staticmethod
    def export(params):
        print('Exporting sales.csv ...')
        sales = Model.sales.list()

        with open('documents/sales.csv', 'w') as csvfile:
            fieldnames = ['id', 'date', 'company', 'nif', 'summary']
            fieldnames = fieldnames + list(Model.me.list_vats().keys())
            fieldnames = fieldnames + ['subtotal', 'total', 'paid']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()

            for s in sales:
                row = {
                    'id': s.id,
                    'date': s.date,
                    'company': s.company['company'],
                    'nif': s.company['nif'],
                    'summary': s.summary,
                    'subtotal': s.subtotal,
                    'total': s.total,
                    'paid': "x" if s.paid is None else s.paid
                }
                vats = s.resume_vats()
                for code in vats:
                    value = vats[code]
                    row[code] = value

                writer.writerow(row)

            print('Finished!')
