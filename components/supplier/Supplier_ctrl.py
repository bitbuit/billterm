from libs.Screen import *
from components.supplier.Supplier import Supplier
from components.supplier.Supplier_tpl import Supplier_tpl

from app.Model import Model


class Supplier_ctrl(object):

    @staticmethod
    def list(params):
        ss = Model.suppliers.list()
        Supplier_tpl.list(ss)

    @staticmethod
    def view(params):
        id = params[0]
        s = Model.suppliers.get(id)
        Supplier_tpl.view(s)

    @staticmethod
    def new(params):
        id = input("Id: ")
        company = Supplier(id)
        company.company = input("Company name: ")
        company.nif = input("Fiscal number:" )
        company.address = input("Address: ")
        company.cp = input("Post code: ")
        company.city = input("City: ")
        company.email = input("E-Mail: ")
        company.contact = input("Contact: ")
        company.comments = input("Comments: ")
        Model.suppliers.add(company)
        print("All alright!")
