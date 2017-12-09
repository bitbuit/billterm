from app.Model import Model
from libs.Screen import *
from components.customer.Customer import *
from components.customer.Customer_tpl import Customer_tpl

class Customer_ctrl(object):

    @staticmethod
    def list(params):
        cs = Model.customers.list()
        Customer_tpl.list(cs)
 

    @staticmethod
    def view(params):
        id = params[0]
        c = Model.customers.get(id)
        Customer_tpl.view(c)
        

    @staticmethod
    def new(params):
        id = input("Id: ")
        company = Customer(id)
        company.company = input("Company name: ")
        company.nif = input("Fiscal number:" )
        company.address = input("Address: ")
        company.cp = input("Post code: ")
        company.city = input("City: ")
        company.email = input("E-Mail: ")
        company.contact = input("Contact: ")
        company.comments = input("Comments: ")
        Model.customers.add(company)
        print("All alright!")
