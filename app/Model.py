from components.customer.Customer import Customers
from components.supplier.Supplier import Suppliers
from components.sale.Sale import Sales
from components.me.Me import Me

import os

class Model(object):
    using_db = None
    me = None
    customers = None
    suppliers = None
    sales = None

    @staticmethod
    def init(db = "default"):
        path = "./db/" + db + "/"
        if not os.path.isdir(path):
            print("Database not exists.")
            return
        Model.customers = Customers(path + 'customers.json')
        Model.suppliers = Suppliers(path + 'suppliers.json')
        Model.sales = Sales(path + 'sales.json')
        Model.me = Me(path + 'me.json')
        Model.using_db = db

    @staticmethod
    def using():
        return Model.using_db
