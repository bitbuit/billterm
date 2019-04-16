import shlex
from pprint import pprint

from components.app.App_routr import App_routr
from components.customer.Customer_routr import Customer_routr
from components.supplier.Supplier_routr import Supplier_routr
from components.me.Me_routr import Me_routr
from components.sale.Sale_routr import Sale_routr
from libs.Screen import Screen

class App(object):

    @staticmethod
    def init():
        return;

    @staticmethod
    def start():
        Commands.do(["hello!"])
        while True:
            exp = Screen.prompt()
            exp = shlex.split(exp)
            Commands.do(exp)
#            try:
#                Commands.do(exp)
#            except:
#                print("Unknow command! Type: help")


class Commands(object):

    _routes_map = [ 
                    App_routr,
                    Customer_routr, 
                    Supplier_routr,
                    Sale_routr,
                    Me_routr
    ]
    
    @staticmethod
    def do(inputs):
        action = None
        params = []

        for route_map in Commands._routes_map:
            action, params = route_map.find(inputs)
            if not action is None:
                break;

        if not action is None:
            action(params)


