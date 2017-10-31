from libs.Screen import *
from components.invoice.Invoice import Invoice

from pprint import pprint

class Invoice_tpl(object):

    @staticmethod
    def view(invoice):
        info_table = Table(["{:>10}", "{:^10}", "{:^10}", "{:^10}"])
        info_table.add_header(["Id", "Date", "Company Id", "Paid"])
        info_table.add_row([
            [invoice.id, Text_style.BLUE],
            [invoice.date, Text_style.YELLOW],
            [invoice.company['id']],
            ["x" if invoice.paid is None else invoice.paid,
            Text_style.BOLD + Text_style.RED if invoice.paid is None else '']          
            ])
        info_table.add_empty_row()
        info_table.render()
        Screen.render_line( [ ["Summary:", "{:<20}", Text_style.BOLD], [invoice.summary, "{:<80}"] ])

        items_table = Table(["{:<3}", "{:<40}", "{:^16}", "{:>8}", "{:>8}", "{:>8}"])
        items_table.add_header(["#", "Item", "Vats", "Qty", "Price", "Total"])

        i = 0
        while not invoice.get_item(i) == None:
            line = invoice.get_item(i)
            vats_code = []
            
            for k in line['vats']:
                vats_code.append(k)
            items_table.add_row([
                [ str(i+1), Text_style.BLUE ],
                [ line['description'] ],
                [ ' '.join(vats_code) ],
                [ line['qty']], 
                [ line['price']],
                [ line['total']],
                ])
            i += 1
       
        items_table.add_empty_row()
        items_table.render()
        resume_table = Table(["{:<16}","{:>10}"])
        resume_table.add_row([ ["Subtotal", Text_style.BOLD], [invoice.subtotal] ])
        vats = invoice.resume_vats()
        for code in vats:
            value = vats[code]
            resume_table.add_row([ [code, Text_style.BOLD ], [str(value)] ])
        resume_table.add_row([ ["Total", Text_style.BOLD], [invoice.total, Text_style.UNDERLINE] ])
        resume_table.render()

    @staticmethod
    def list(invoices):
        table = Table(["{:>10}", "{:^10}", "{:^10}", "{:<60}", "{:^10}", "{:>10}"])
        table.add_header(["Id", "Date", "Customer", "Summary", "Paid", "Total"])

        for inv in invoices:
            
            table.add_row([
                [inv.id, Text_style.BLUE], 
                [inv.date, Text_style.YELLOW],
                [inv.company['id'], Text_style.BLUE],
                [inv.summary],
                ["x" if inv.paid is None else inv.paid,
                Text_style.BOLD + Text_style.RED if inv.paid is None else ''],
                [inv.total, Text_style.UNDERLINE ] 
            ])

        table.render()

