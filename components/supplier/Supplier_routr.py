from libs.Routes import Routes
from components.supplier.Supplier_ctrl import Supplier_ctrl

class Supplier_routr(Routes):
    _routes = [  
                [ ['list', 'suppliers'], Supplier_ctrl.list ],
                [ ['view', 'supplier'], Supplier_ctrl.view ],
                [ ['new', 'supplier'], Supplier_ctrl.new ]
    ]
