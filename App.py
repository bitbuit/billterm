import shlex
from pprint import pprint

from components.customer.Customer_routr import Customer_routr
from components.supplier.Supplier_routr import Supplier_routr
from components.me.Me_routr import Me_routr
from components.sale.Sale_routr import Sale_routr

class App(object):

    @staticmethod
    def init():
        return;

    @staticmethod
    def start():
        print("Hello!")
        print("Write 'help' if you are lost :)")
        while True:
            exp = input(": ")
            exp = shlex.split(exp)
            Commands.do(exp)
#            try:
#                Commands.do(exp)
#            except:
#                print("Unknow command! Type: help")

    @staticmethod
    def help(params):
        #pprint(Commands.get_routes())
        pass

    @staticmethod
    def exit(params):
        quit()



class Commands(object):
    _ROUTES = [  

                [ ['help'], App.help],
                [ ['exit'], App.exit ],
     ]

    _routes_map = [ 
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


