from libs.Screen import *
from components.company.Company import Company

class Company_tpl(object):

    @staticmethod
    def view(company):
        c = company  

        table = Table([ "{:<20}", "{:<40}", "{:<20}", "{:<40}"])
        table.add_row([
            [ "Id:", Text_style.BOLD ], [ c.id, Text_style.BLUE ]
            ])
        table.add_row([
            [ "Company:", Text_style.BOLD ], [ c.company ], 
            [ "Fiscal nº:", Text_style.BOLD ], [ c.nif, Text_style.YELLOW ]
            ])
        table.add_row([
            [ "Address:", Text_style.BOLD ], [ c.address ]
            ])
        table.add_row([
            [ "City:", Text_style.BOLD ], [ c.city ],
            [ "Post Code:", Text_style.BOLD ], [ c.pc ]
            ])
        table.add_empty_row()
        table.add_row([
            [ "Contact:", Text_style.BOLD ], [ c.contact ],
            [ "Mail:", Text_style.BOLD ], [ c.email, Text_style.MAGENTA ]
            ])
        table.add_empty_row()
        table.add_row([
            [ "Comments:", Text_style.BOLD ], [ c.comments ]
            ])
        table.add_empty_row()

        table.render()

    @staticmethod
    def list(companies):
        table = Table([ "{:^10}", "{:^60}", "{:^10}", "{:^30}"])
        table.add_header(["Id", "Company name", "Nif", "Mail"])

        for c in companies:
            table.add_row([
                [c.id, Text_style.BLUE], 
                [c.company],
                [c.nif, Text_style.YELLOW],
                [c.email, Text_style.MAGENTA],
                ])

        table.render()  
