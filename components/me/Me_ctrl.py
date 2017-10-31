from libs.Screen import *
from components.company.Company import Company
from Model import Model
from components.me.Me_tpl import Me_tpl
from pprint import pprint

class Me_ctrl(object):

    @staticmethod
    def view(params):
        c = Model.me.get_company()
        Me_tpl.view(c)
        
        vs = Model.me.list_vats()
        ps = Model.me.list_payments()

        vats_table = Table([ "{:^10}", "{:<20}", "{:>10}"])
        vats_table.add_empty_row()
        vats_table.add_header(["Id", "Label", "Value"])

        for k in vs:
            vat = vs[k]
            vats_table.add_row([ [ vat['id'] ], [ vat['label'] ], [ str(vat['value']) + "%" ] ])

        vats_table.render()

        payments_table = Table([ "{:^10}", "{:<20}", "{:<80}"])
        payments_table.add_empty_row()
        payments_table.add_header(["Id", "Label", "Message"])

        for k in ps:
            payment = ps[k]
            payments_table.add_row( [ [ payment["id"] ], [ payment["label"] ], [ payment["msg"] ] ] )

        payments_table.render()
