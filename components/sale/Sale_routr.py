from libs.Routes import Routes
from components.sale.Sale_ctrl import Sale_ctrl

class Sale_routr(Routes):
    _routes = [  
                [ ['list', 'sales'], Sale_ctrl.list ],
                [ ['export', 'sales'], Sale_ctrl.export ],
                [ ['export', 'sale'], Sale_ctrl.pdf ],
                [ ['view', 'sale'], Sale_ctrl.view ],
                [ ['new', 'sale'], Sale_ctrl.new ],
                [ ['add', 'sale', 'item'], Sale_ctrl.add_item ],
                [ ['paid', 'sale'], Sale_ctrl.paid ]
    ]
