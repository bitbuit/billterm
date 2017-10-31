from components.customer.Customer import Customers
from components.supplier.Supplier import Suppliers
from components.sale.Sale import Sales
from components.me.Me import Me

class Model(object):
    me = None
    customers = None
    suppliers = None
    sales = None

    def init():
        Model.customers = Customers('customers.json')
        Model.suppliers = Suppliers('suppliers.json')
        Model.sales = Sales('sales.json')
        Model.me = Me('me.json')
